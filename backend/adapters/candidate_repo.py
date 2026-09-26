from typing import List, Dict, Any

class MockCandidateRepository:
    """
    Candidate repository interface for ATS (Greenhouse, Lever, Ashby) integrations.
    Provides realistic candidate ranking and scoring based on the evaluated role.
    """
    @staticmethod
    def screen_and_rank_candidates(role: str, criteria: str = "3+ years", salary_band: str = "₹6L - ₹9L") -> List[Dict[str, Any]]:
        role_lower = role.lower()
        if any(k in role_lower for k in ["front", "react", "ui", "web", "developer", "engineer", "software"]):
            return [
                {
                    "id": "cand_01",
                    "name": "Rahul Sharma",
                    "match_score": 94,
                    "status": "Interview Recommended",
                    "experience": "4.5 years",
                    "current_company": "HyperScale Labs",
                    "core_skills": ["React 18", "TypeScript", "Tailwind CSS", "Next.js", "Redux/Zustand"],
                    "github_summary": "Top 5% open-source contributor; created widely used React animation library (2.4k stars)",
                    "expected_salary": "₹8.5L / year",
                    "notice_period": "Immediate (15 days)",
                    "interview_recommendation": "Strong Hire - Outstanding frontend systems design and UI component velocity."
                },
                {
                    "id": "cand_02",
                    "name": "Ananya Rao",
                    "match_score": 91,
                    "status": "Interview Recommended",
                    "experience": "3.8 years",
                    "current_company": "FinTech Matrix",
                    "core_skills": ["React", "TypeScript", "GraphQL", "WebSockets", "Vite"],
                    "github_summary": "Architected low-latency trader dashboard with 60fps real-time data streaming",
                    "expected_salary": "₹9.0L / year",
                    "notice_period": "30 days",
                    "interview_recommendation": "Strong Hire - Deep performance optimization and API integration expertise."
                },
                {
                    "id": "cand_03",
                    "name": "Arjun Kumar",
                    "match_score": 73,
                    "status": "Review",
                    "experience": "2.5 years",
                    "current_company": "DigitalCraft Agency",
                    "core_skills": ["JavaScript", "React", "HTML/CSS", "Bootstrap"],
                    "github_summary": "Solid portfolio of client landing pages and e-commerce frontends",
                    "expected_salary": "₹6.5L / year",
                    "notice_period": "Immediate",
                    "interview_recommendation": "Potential Hire - Good styling skills, requires mentorship on complex state management."
                }
            ]
        elif any(k in role_lower for k in ["market", "growth", "lead"]):
            return [
                {
                    "id": "cand_11",
                    "name": "Pooja Verma",
                    "match_score": 93,
                    "status": "Interview Recommended",
                    "experience": "5.0 years",
                    "current_company": "SaaS ScaleX",
                    "core_skills": ["Product-Led Growth", "LinkedIn Inbound", "Performance Ads", "HubSpot"],
                    "github_summary": "Grew B2B SaaS ARR from $200k to $1.8M via viral content loops",
                    "expected_salary": "₹9.5L / year",
                    "notice_period": "Immediate",
                    "interview_recommendation": "Strong Hire - Proven organic distribution and founder storytelling playbook."
                },
                {
                    "id": "cand_12",
                    "name": "Vikram Sethi",
                    "match_score": 85,
                    "status": "Interview Recommended",
                    "experience": "3.2 years",
                    "current_company": "GrowthPad",
                    "core_skills": ["SEO Optimization", "Community Building", "Email Nurturing"],
                    "github_summary": "Managed 45k+ member developer community and technical newsletter",
                    "expected_salary": "₹7.5L / year",
                    "notice_period": "15 days",
                    "interview_recommendation": "Solid Hire - High output on developer marketing."
                }
            ]
        else:
            return [
                {
                    "id": "cand_21",
                    "name": "Siddharth Mehta",
                    "match_score": 92,
                    "status": "Interview Recommended",
                    "experience": "4.0 years",
                    "current_company": "Apex Dynamics",
                    "core_skills": [f"{role} Mastery", "System Design", "Agile Execution"],
                    "github_summary": "Proven track record delivering mission-critical startup objectives",
                    "expected_salary": salary_band,
                    "notice_period": "Immediate",
                    "interview_recommendation": "Strong Hire - Exceptional domain problem solving."
                }
            ]
