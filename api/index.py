"""
Vercel Serverless API Entry Point for PhishShield-XAI
This wraps the FastAPI application for Vercel's Python runtime
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Import the main app
from src.api.app import app

# Configure logging
logging.basicConfig(level=logging.INFO)

# Ensure CORS is configured for Vercel deployment
if not any(isinstance(m, CORSMiddleware) for m in app.user_middleware):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

# Export app for Vercel
export = app
