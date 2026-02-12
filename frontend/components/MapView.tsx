import React from 'react';

const MapView: React.FC = () => {
    return (
        <div style={{
            width: '100%',
            height: '100%',
            background: '#020617',
            position: 'relative',
            backgroundImage: 'radial-gradient(rgba(56, 189, 248, 0.1) 1px, transparent 0)',
            backgroundSize: '40px 40px'
        }}>
            {/* Map Content Placeholder */}
            <div style={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                textAlign: 'center',
                color: '#334155'
            }}>
                <div style={{ fontSize: '4rem', marginBottom: '16px' }}>📡</div>
                <div style={{ fontSize: '1.2rem', fontWeight: 600 }}>Initializing Real-Time Map</div>
                <div style={{ fontSize: '0.9rem', opacity: 0.6 }}>Waiting for AIS local stream linkage...</div>
            </div>

            {/* Overlay controls */}
            <div style={{
                position: 'absolute',
                bottom: '24px',
                right: '24px',
                display: 'flex',
                flexDirection: 'column',
                gap: '8px'
            }}>
                {['+', '-', 'TARGET'].map(btn => (
                    <button key={btn} style={{
                        width: '44px',
                        height: '44px',
                        backgroundColor: 'rgba(30, 41, 59, 0.8)',
                        border: '1px solid rgba(255, 255, 255, 0.1)',
                        borderRadius: '8px',
                        color: 'white',
                        cursor: 'pointer',
                        fontWeight: 700,
                        backdropFilter: 'blur(4px)'
                    }}>{btn}</button>
                ))}
            </div>

            {/* Vessel Legend */}
            <div style={{
                position: 'absolute',
                top: '24px',
                left: '24px',
                padding: '16px',
                background: 'rgba(2, 6, 23, 0.7)',
                backdropFilter: 'blur(10px)',
                border: '1px solid rgba(255, 255, 255, 0.05)',
                borderRadius: '12px',
                width: '200px'
            }}>
                <div style={{ fontSize: '0.8rem', fontWeight: 700, marginBottom: '12px', color: '#94a3b8' }}>LAYER CONTROL</div>
                {[
                    { color: '#10b981', label: 'Cargo Vessels' },
                    { color: '#3b82f6', label: 'Tankers' },
                    { color: '#f59e0b', label: 'Pleasure Craft' },
                    { color: '#ef4444', label: 'High Risk Targets' }
                ].map(item => (
                    <div key={item.label} style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px', fontSize: '0.8rem' }}>
                        <div style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: item.color }}></div>
                        {item.label}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MapView;
