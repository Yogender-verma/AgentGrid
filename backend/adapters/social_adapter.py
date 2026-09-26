import time
from typing import Dict, Any

class MockSocialAdapter:
    @staticmethod
    def generate_recruitment_posts(role: str, salary_info: str = "₹6L - ₹9L / year", criteria: str = "3+ years experience") -> Dict[str, Any]:
        linkedin_post = f"""🚀 We are hiring a {role} at AgentGrid!

We are expanding our core team to build the autonomous AI executive workforce for founders worldwide.

✨ What you will work on:
• Architecting ultra-fast, resilient interfaces with React and TypeScript
• Working directly with our autonomous AI backend pipeline
• High ownership, zero bureaucracy, rapid deployment cycles

💰 Compensation: {salary_info} + Generous Founder Equity
📍 Location: Remote / Hybrid
⚡ Experience: {criteria}

👉 Interested? Apply directly or DM with your portfolio/GitHub!"""

        telegram_post = f"""🔥 HIRING ALERT: {role} @ AgentGrid

• Role: {role}
• Compensation: {salary_info} + Equity
• Stack: React, TypeScript, Tailwind, REST APIs
• Work Mode: Remote / Flexible

Apply via DM @AgentGrid_Talent or reply to this message."""

        return {
            "role": role,
            "salary_info": salary_info,
            "linkedin_post": linkedin_post,
            "telegram_post": telegram_post,
            "twitter_post": f"We just opened a {role} role at @AgentGrid ({salary_info} + equity). DM your GitHub/portfolio if you love building AI-powered systems! RTs appreciated 🚀",
            "recommended_channels": ["LinkedIn Talent Solutions", "Telegram Dev Hub", "X Tech Community", "Wellfound"]
        }

    @staticmethod
    def publish_linkedin(content: str) -> Dict[str, Any]:
        return {
            "platform": "LinkedIn",
            "status": "PUBLISHED",
            "post_id": f"urn:li:share:{int(time.time())}",
            "live_url": "https://www.linkedin.com/feed/update/urn:li:share:719829410",
            "published_at": time.strftime("%Y-%m-%d %H:%M:%S UTC")
        }

    @staticmethod
    def publish_telegram(content: str, channel: str = "@AgentGrid_Announcements") -> Dict[str, Any]:
        return {
            "platform": "Telegram",
            "status": "BROADCASTED",
            "channel": channel,
            "message_id": int(time.time()) % 100000,
            "published_at": time.strftime("%Y-%m-%d %H:%M:%S UTC")
        }
