import React from 'react';
import Layout from '../components/Layout';
import MapView from '../components/MapView';
import VesselList from '../components/VesselList';

/**
 * NAVINT - Unified Operational Dashboard
 * Consolidated Next.js interface for monitoring and analytics.
 */
export default function Home() {
    return (
        <Layout title="NAVINT | Unified Operational Dashboard">
            <div style={{
                display: 'flex',
                height: '100%',
                width: '100%'
            }}>
                {/* Main Map View (Flex 1) */}
                <div style={{ flex: 1, position: 'relative' }}>
                    <MapView />
                </div>

                {/* Right Sidebar - Integrated Analytics & Vessel Intelligence */}
                <div style={{
                    width: '400px',
                    borderLeft: '1px solid rgba(255, 255, 255, 0.05)',
                    display: 'flex',
                    flexDirection: 'column',
                    backgroundColor: 'rgba(2, 6, 23, 0.6)',
                    backdropFilter: 'blur(30px)'
                }}>
                    <VesselList />

                    {/* Critical Alert Panel (Footer) */}
                    <div style={{
                        padding: '20px 24px',
                        borderTop: '1px solid rgba(255, 255, 255, 0.1)',
                        background: 'linear-gradient(to bottom, rgba(239, 68, 68, 0.1), transparent)',
                        marginTop: 'auto'
                    }}>
                        <div style={{
                            display: 'flex',
                            alignItems: 'center',
                            gap: '8px',
                            fontWeight: 700,
                            fontSize: '0.8rem',
                            color: '#ef4444',
                            marginBottom: '8px'
                        }}>
                            <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#ef4444', animation: 'pulse 2s infinite' }}></span>
                            CRITICAL ALERT DETECTED
                        </div>
                        <div style={{ fontSize: '0.8rem', color: '#94a3b8', lineHeight: '1.4' }}>
                            Vessel <strong>DARK STAR (MMSI: 667001122)</strong> identified within 2NM of <strong>Strategic Asset Alpha</strong>. Initiating anomaly verification.
                        </div>
                        <button style={{
                            marginTop: '12px',
                            width: '100%',
                            padding: '8px',
                            backgroundColor: 'rgba(239, 68, 68, 0.2)',
                            border: '1px solid rgba(239, 68, 68, 0.3)',
                            borderRadius: '6px',
                            color: '#ef4444',
                            fontSize: '0.75rem',
                            fontWeight: 600,
                            cursor: 'pointer'
                        }}>
                            ACKNOWLEDGE & TRIAGE
                        </button>
                    </div>
                </div>
            </div>

            <style jsx global>{`
        @keyframes pulse {
          0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
          70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
          100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }
      `}</style>
        </Layout>
    );
}
