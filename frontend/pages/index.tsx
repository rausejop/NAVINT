import React from 'react';
import Head from 'next/head';

export default function Home() {
    return (
        <div style={{ fontFamily: 'sans-serif', padding: '40px', backgroundColor: '#0f172a', color: '#f8fafc', minHeight: '100vh' }}>
            <Head>
                <title>NAVINT | Maritime Intelligence</title>
            </Head>

            <header style={{ borderBottom: '1px solid #334155', paddingBottom: '20px', marginBottom: '40px' }}>
                <h1 style={{ margin: 0, fontSize: '2.5rem', color: '#38bdf8' }}>NAVINT</h1>
                <p style={{ margin: 0, opacity: 0.7 }}>Standalone Maritime Intelligence Support Tool</p>
            </header>

            <main>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px' }}>
                    <div style={{ padding: '20px', border: '1px solid #334155', borderRadius: '8px', backgroundColor: '#1e293b' }}>
                        <h2 style={{ marginTop: 0 }}>Vessel Tracking</h2>
                        <p>Real-time monitoring of AIS targets. Interface loading...</p>
                    </div>

                    <div style={{ padding: '20px', border: '1px solid #334155', borderRadius: '8px', backgroundColor: '#1e293b' }}>
                        <h2 style={{ marginTop: 0 }}>Active Alerts</h2>
                        <p>System status: Operational. No active threats detected in localhost sector.</p>
                    </div>

                    <div style={{ padding: '20px', border: '1px solid #334155', borderRadius: '8px', backgroundColor: '#1e293b' }}>
                        <h2 style={{ marginTop: 0 }}>Analytics Dashboard</h2>
                        <p>Access Streamlit analytics on port 8501 for high-level risk modeling.</p>
                    </div>
                </div>
            </main>

            <footer style={{ marginTop: '80px', paddingTop: '20px', borderTop: '1px solid #334155', fontSize: '0.8rem', opacity: 0.5 }}>
                CONF23-STD-SDLC-NAVMIL | USO OFICIAL
            </footer>
        </div>
    );
}
