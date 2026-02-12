import React, { ReactNode } from 'react';
import Head from 'next/head';

interface LayoutProps {
    children: ReactNode;
    title?: string;
}

const Layout: React.FC<LayoutProps> = ({ children, title = "NAVINT | Maritime Intelligence" }) => {
    return (
        <div style={{
            display: 'flex',
            height: '100vh',
            width: '100vw',
            backgroundColor: '#020617',
            color: '#f8fafc',
            fontFamily: 'Inter, system-ui, sans-serif',
            overflow: 'hidden'
        }}>
            <Head>
                <title>{title}</title>
            </Head>

            {/* Sidebar - Glassmorphism style */}
            <aside style={{
                width: '260px',
                background: 'rgba(30, 41, 59, 0.4)',
                backdropFilter: 'blur(12px)',
                borderRight: '1px solid rgba(255, 255, 255, 0.1)',
                display: 'flex',
                flexDirection: 'column',
                padding: '24px 16px'
            }}>
                <div style={{ marginBottom: '40px', display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{
                        width: '40px',
                        height: '40px',
                        background: 'linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%)',
                        borderRadius: '10px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: '0 0 20px rgba(56, 189, 248, 0.3)'
                    }}>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2"><path d="M22 3.5l-2.4 2.4-1.6-1.6L20.4 2 22 3.5zM2 21.5l2.4-2.4 1.6 1.6-2.4 2.4-1.6-1.6zM14 6l6 6M9 11l6 6M4 16l6 6M11 4l6 6M6 9l6 6M1 14l6 6" /></svg>
                    </div>
                    <span style={{ fontSize: '1.5rem', fontWeight: 800, letterSpacing: '-1px' }}>NAVINT</span>
                </div>

                <nav style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {['Monitoring', 'Analytics', 'Signals', 'Reports', 'Settings'].map((item) => (
                        <div key={item} style={{
                            padding: '12px 16px',
                            borderRadius: '8px',
                            cursor: 'pointer',
                            fontSize: '0.95rem',
                            fontWeight: 500,
                            display: 'flex',
                            alignItems: 'center',
                            gap: '12px',
                            transition: 'all 0.2s ease',
                            backgroundColor: item === 'Monitoring' ? 'rgba(56, 189, 248, 0.1)' : 'transparent',
                            color: item === 'Monitoring' ? '#38bdf8' : '#94a3b8'
                        }}
                            onMouseEnter={(e) => {
                                if (item !== 'Monitoring') e.currentTarget.style.backgroundColor = 'rgba(255, 255, 255, 0.05)';
                            }}
                            onMouseLeave={(e) => {
                                if (item !== 'Monitoring') e.currentTarget.style.backgroundColor = 'transparent';
                            }}
                        >
                            {item}
                        </div>
                    ))}
                </nav>

                <div style={{
                    marginTop: 'auto',
                    paddingTop: '20px',
                    borderTop: '1px solid rgba(255, 255, 255, 0.05)',
                    fontSize: '0.75rem',
                    color: '#475569',
                    textAlign: 'center'
                }}>
                    CONF23-STD-SDLC-NAVMIL<br />USO OFICIAL
                </div>
            </aside>

            {/* Main Content Area */}
            <main style={{ flex: 1, display: 'flex', flexDirection: 'column', position: 'relative' }}>
                {/* Top Navbar */}
                <header style={{
                    height: '64px',
                    background: 'rgba(2, 6, 23, 0.8)',
                    backdropFilter: 'blur(8px)',
                    borderBottom: '1px solid rgba(255, 255, 255, 0.05)',
                    display: 'flex',
                    alignItems: 'center',
                    padding: '0 24px',
                    justifyContent: 'space-between',
                    zIndex: 10
                }}>
                    <div style={{ display: 'flex', gap: '24px', fontSize: '0.9rem', color: '#64748b' }}>
                        <span>Active Vessels: <strong style={{ color: '#38bdf8' }}>142</strong></span>
                        <span>Alerts: <strong style={{ color: '#ef4444' }}>1 Critical</strong></span>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                        <button
                            onClick={() => window.open('http://127.0.0.1:8000/api/v1/export/vessels')}
                            style={{
                                padding: '6px 12px',
                                borderRadius: '6px',
                                background: 'rgba(56, 189, 248, 0.1)',
                                border: '1px solid rgba(56, 189, 248, 0.2)',
                                color: '#38bdf8',
                                fontSize: '0.75rem',
                                fontWeight: 600,
                                cursor: 'pointer',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '6px'
                            }}>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3" /></svg>
                            Export
                        </button>
                        <div style={{
                            backgroundColor: 'rgba(255,255,255,0.05)',
                            borderRadius: '20px',
                            padding: '6px 16px',
                            fontSize: '0.8rem',
                            color: '#94a3b8'
                        }}>
                            Local Node: 127.0.0.1
                        </div>
                        <div style={{ width: '32px', height: '32px', borderRadius: '50%', backgroundColor: '#334155' }}></div>
                    </div>

                </header>

                {/* Dynamic Content */}
                <div style={{ flex: 1, position: 'relative', overflowY: 'auto' }}>
                    {children}
                </div>
            </main>
        </div>
    );
};

export default Layout;
