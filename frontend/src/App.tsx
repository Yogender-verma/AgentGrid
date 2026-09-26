import { useState, Component } from 'react';
import type { ReactNode, ErrorInfo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Preloader } from './components/Preloader';
import { HomePage } from './pages/HomePage';
import { ContactPage } from './pages/ContactPage';
import { AuthPage } from './pages/AuthPage';
import { DashboardPage } from './pages/DashboardPage';
import { AssessmentPage } from './pages/AssessmentPage';
import { CandidateDetailPage } from './pages/CandidateDetailPage';

interface ErrorBoundaryProps {
  children: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("Uncaught React ErrorBoundary catch:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-[#0B0813] text-white flex items-center justify-center p-6 text-center">
          <div className="bg-[#120E1E] border border-[#251B38] p-8 rounded-3xl max-w-md space-y-4 shadow-2xl">
            <h2 className="text-xl font-black text-red-400">Application Runtime Notice</h2>
            <p className="text-xs text-gray-400 leading-relaxed">
              An unexpected UI state occurred. We've captured the context to preserve system stability.
            </p>
            <div className="flex items-center justify-center gap-3 pt-2">
              <button
                onClick={() => { this.setState({ hasError: false, error: null }); window.location.reload(); }}
                className="px-5 py-2.5 bg-[#8B5CF6] hover:bg-[#7C3AED] text-white font-bold text-xs rounded-xl transition-all"
              >
                Reload Page
              </button>
              <a
                href="/dashboard/hiring-agent"
                className="px-5 py-2.5 bg-[#1C162E] border border-[#2D234A] text-gray-300 font-bold text-xs rounded-xl hover:bg-[#251B38] transition-all"
              >
                Go to Hiring Dashboard
              </a>
            </div>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}

function App() {
  const [loading, setLoading] = useState(true);

  return (
    <Router>
      <AnimatePresence>
        {loading && <Preloader onComplete={() => setLoading(false)} />}
      </AnimatePresence>

      {!loading && (
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="min-h-screen bg-gray-50 dark:bg-page-gradient overflow-x-hidden relative transition-colors duration-500"
        >
          {/* Background ambient glows */}
          <div className="absolute top-[-10%] left-[-10%] w-[800px] h-[800px] bg-founder-primary/5 dark:bg-founder-primary/10 rounded-full blur-[150px] pointer-events-none"></div>
          <div className="absolute bottom-[-10%] right-[-10%] w-[800px] h-[800px] bg-founder-secondary/5 rounded-full blur-[150px] pointer-events-none"></div>
          
          <ErrorBoundary>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/contact" element={<ContactPage />} />
              <Route path="/auth" element={<AuthPage />} />
              <Route path="/dashboard" element={<DashboardPage />} />
              <Route path="/dashboard/:tabId" element={<DashboardPage />} />
              <Route path="/hiring" element={<DashboardPage />} />
              <Route path="/hiring/jobs/:jobId" element={<DashboardPage />} />
              <Route path="/hiring/candidates/:candidateId" element={<CandidateDetailPage />} />
              <Route path="/hiring/assessment/:assessmentId" element={<AssessmentPage />} />
            </Routes>
          </ErrorBoundary>
        </motion.div>
      )}
    </Router>
  );
}

export default App;
