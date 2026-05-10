import numpy as np
import shap
import logging
from sklearn.ensemble import VotingClassifier

logger = logging.getLogger(__name__)

class ShapExplainer:
    def __init__(self, model, model_type="classical", background_data=None, feature_names=None):
        self.model = model
        self.model_type = model_type
        self.background_data = background_data
        self.feature_names = feature_names
        self.shap_explainer = self._init_shap_explainer()

    def _init_shap_explainer(self):
        try:
            # Check if model is a VotingClassifier (not supported by TreeExplainer)
            if isinstance(self.model, VotingClassifier):
                logger.info("VotingClassifier detected, using KernelExplainer")
                pred_fn = self.model.predict_proba if hasattr(self.model, 'predict_proba') else self.model.predict
                # Create synthetic background data if not provided
                if self.background_data is None:
                    # Use a simple zero-filled background
                    n_features = self.model.estimators_[0].n_features_in_ if hasattr(self.model.estimators_[0], 'n_features_in_') else 100
                    self.background_data = np.zeros((10, n_features))
                return shap.KernelExplainer(pred_fn, self.background_data[:10])
            elif self.model_type == "classical":
                # Try TreeExplainer first for tree-based models
                try:
                    return shap.TreeExplainer(self.model)
                except:
                    # Fallback to KernelExplainer
                    logger.info("TreeExplainer not supported, using KernelExplainer")
                    pred_fn = self.model.predict_proba if hasattr(self.model, 'predict_proba') else self.model.predict
                    if self.background_data is None:
                        n_features = self.model.n_features_in_ if hasattr(self.model, 'n_features_in_') else 100
                        self.background_data = np.zeros((10, n_features))
                    return shap.KernelExplainer(pred_fn, self.background_data[:10])
            elif self.background_data is not None:
                pred_fn = self.model.predict_proba if hasattr(self.model, 'predict_proba') else self.model.predict
                return shap.KernelExplainer(pred_fn, self.background_data[:10])
            else:
                return None
        except Exception as e:
            logger.error(f"SHAP init failed: {e}")
            return None

    def get_explanation(self, features, top_k=10):
        try:
            if self.shap_explainer is None:
                return self._fallback_feature_importance(features, top_k)
            shap_values = self.shap_explainer.shap_values(features)
            if isinstance(shap_values, list):
                values = shap_values[1][0] if len(shap_values) > 1 else shap_values[0][0]
            elif isinstance(shap_values, np.ndarray):
                # Handle 3D arrays (multi-output models)
                if shap_values.ndim == 3:
                    values = shap_values[0, :, 1] if shap_values.shape[2] > 1 else shap_values[0, :, 0]
                else:
                    values = shap_values[0]
            else:
                values = np.array(shap_values.values[0]) if hasattr(shap_values, 'values') else np.zeros(len(self.feature_names or []))
            
            if len(values) == 0:
                return self._fallback_feature_importance(features, top_k)
            
            names = self.feature_names or [f"feature_{i}" for i in range(len(values))]
            indices = np.argsort(np.abs(values))[::-1][:top_k]
            return [{"feature": names[idx] if idx < len(names) else f"feature_{idx}",
                     "importance": round(float(np.abs(values[idx])), 6),
                     "direction": "phishing" if values[idx] > 0 else "legitimate"} for idx in indices]
        except Exception as e:
            logger.error(f"SHAP failed: {e}")
            return self._fallback_feature_importance(features, top_k)

    def _fallback_feature_importance(self, features, top_k):
        """Fallback to permutation importance or aggregate estimator importances."""
        try:
            # For VotingClassifier, aggregate importances from tree-based estimators
            if isinstance(self.model, VotingClassifier):
                importances = []
                for estimator in self.model.estimators_:
                    if hasattr(estimator, 'feature_importances_'):
                        importances.append(estimator.feature_importances_)
                
                if importances:
                    imp = np.mean(importances, axis=0)
                    names = self.feature_names or [f"feature_{i}" for i in range(len(imp))]
                    indices = np.argsort(imp)[::-1][:top_k]
                    return [{"feature": names[i] if i < len(names) else f"feature_{i}", 
                             "importance": round(float(imp[i]), 6),
                             "direction": "phishing" if features[0][i] > 0 else "legitimate"} 
                            for i in indices]
            
            # For other models with feature_importances_
            if hasattr(self.model, 'feature_importances_'):
                imp = self.model.feature_importances_
                names = self.feature_names or [f"feature_{i}" for i in range(len(imp))]
                indices = np.argsort(imp)[::-1][:top_k]
                return [{"feature": names[i] if i < len(names) else f"feature_{i}", 
                         "importance": round(float(imp[i]), 6),
                         "direction": "phishing" if features[0][i] > 0 else "legitimate"} 
                        for i in indices]
        except Exception as e:
            logger.error(f"Fallback feature importance failed: {e}")
        
        # Last resort: use abs feature values as proxy for importance
        try:
            values = np.abs(features[0])
            names = self.feature_names or [f"feature_{i}" for i in range(len(values))]
            indices = np.argsort(values)[::-1][:top_k]
            return [{"feature": names[i] if i < len(names) else f"feature_{i}",
                     "importance": round(float(values[i]), 6),
                     "direction": "phishing" if features[0][i] > 0 else "legitimate"}
                    for i in indices]
        except Exception:
            pass
        
        return [{"feature": "unavailable", "importance": 0.0, "direction": "unknown"}]

    def visualize(self, features):
        """Placeholder for visualization function"""
        pass
