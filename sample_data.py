#!/usr/bin/env python3
"""
Sample Data Generator for Email Vector Database
Adds sample emails to the database for testing and demonstration.
"""

import requests
import json
from datetime import datetime, timedelta

def add_sample_emails():
    """Add sample emails to the database"""
    
    sample_emails = [
        {
            "subject": "Project Kickoff Meeting",
            "sender": "manager@company.com",
            "recipient": "team@company.com",
            "content": "Hi team,\n\nI'm excited to announce the kickoff of our new project. We'll be meeting tomorrow at 2 PM to discuss the initial requirements and timeline.\n\nPlease come prepared with your ideas and questions.\n\nBest regards,\nSarah",
            "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "Budget Approval Required",
            "sender": "finance@company.com",
            "recipient": "director@company.com",
            "content": "Dear Director,\n\nWe need your approval for the Q4 budget allocation. The total amount requested is $50,000 for new equipment and software licenses.\n\nPlease review the attached budget proposal and let us know if you have any questions.\n\nRegards,\nFinance Team",
            "date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "Deadline Extension Request",
            "sender": "developer@company.com",
            "recipient": "project.lead@company.com",
            "content": "Hi Project Lead,\n\nI'm requesting a 3-day extension for the API integration task. We've encountered some unexpected compatibility issues with the third-party service.\n\nI believe this extra time will ensure we deliver a robust solution.\n\nThanks,\nAlex",
            "date": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "Client Meeting Tomorrow",
            "sender": "sales@company.com",
            "recipient": "account.manager@company.com",
            "content": "Hello,\n\nJust a reminder about our client meeting tomorrow at 10 AM. The client is interested in our new product features and pricing options.\n\nPlease bring the latest demo materials and pricing sheets.\n\nBest,\nSales Team",
            "date": (datetime.now() - timedelta(days=4)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "System Maintenance Notice",
            "sender": "it@company.com",
            "recipient": "all@company.com",
            "content": "Important Notice:\n\nWe will be performing system maintenance this weekend from 2 AM to 6 AM on Sunday. During this time, some services may be temporarily unavailable.\n\nWe apologize for any inconvenience.\n\nIT Department",
            "date": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "New Employee Welcome",
            "sender": "hr@company.com",
            "recipient": "team@company.com",
            "content": "Welcome to the team!\n\nWe're excited to announce that John Smith has joined our development team as a Senior Developer. John brings 5 years of experience in web development and will be working on our new product features.\n\nPlease make him feel welcome!\n\nHR Team",
            "date": (datetime.now() - timedelta(days=6)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "Quarterly Review Meeting",
            "sender": "ceo@company.com",
            "recipient": "management@company.com",
            "content": "Dear Management Team,\n\nOur quarterly review meeting is scheduled for next Friday at 3 PM. We'll be discussing Q3 results and Q4 objectives.\n\nPlease prepare your department reports and be ready to present your key achievements and challenges.\n\nRegards,\nCEO",
            "date": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M")
        },
        {
            "subject": "Security Update Required",
            "sender": "security@company.com",
            "recipient": "all@company.com",
            "content": "URGENT: Security Update\n\nWe've identified a potential security vulnerability in our email system. Please update your passwords immediately and enable two-factor authentication if you haven't already.\n\nThis is a critical security measure.\n\nSecurity Team",
            "date": (datetime.now() - timedelta(days=8)).strftime("%Y-%m-%dT%H:%M")
        }
    ]
    
    print("📧 Adding sample emails to the database...")
    
    for i, email in enumerate(sample_emails, 1):
        try:
            response = requests.post(
                "http://localhost:8000/add_email",
                data=email
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    print(f"✅ Added email {i}: {email['subject']}")
                else:
                    print(f"❌ Failed to add email {i}: {result.get('message', 'Unknown error')}")
            else:
                print(f"❌ HTTP error {response.status_code} for email {i}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Error: Could not connect to the application.")
            print("💡 Make sure the application is running on http://localhost:8000")
            return
        except Exception as e:
            print(f"❌ Error adding email {i}: {e}")
    
    print("\n🎉 Sample data added successfully!")
    print("🌐 Open http://localhost:8000 to view and search the emails")

if __name__ == "__main__":
    print("=" * 50)
    print("Email Vector Database - Sample Data Generator")
    print("=" * 50)
    print()
    print("This script will add sample emails to your database.")
    print("Make sure the application is running on http://localhost:8000")
    print()
    
    input("Press Enter to continue...")
    add_sample_emails() 