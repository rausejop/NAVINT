import React, { useEffect, useState } from 'react';

/**
 * VesselList Component
 * Coherence Refactor: Standardized naming 'vessel_type' to match Backend Schema.
 */
interface Vessel {
    mmsi: number;
    name: string;
    flag: string;
    vessel_type: string;
    risk: number;
}

const VesselList: React.FC = () => {
    const [vessels, setVessels] = useState<Vessel[]>([
        { mmsi: 224123456, name: "VIVA ESPANA", flag: "ES", vessel_type: "Cargo", risk: 0.15 },
        { mmsi: 351987654, name: "OCEAN MARAUDER", flag: "PA", vessel_type: "Tanker", risk: 0.85 },
        { mmsi: 667001122, name: "DARK STAR", flag: "SL", vessel_type: "Tug", risk: 0.95 }
    ]);

    useEffect(() => {
        const socket = new WebSocket('ws://127.0.0.1:8000/ws/vessels');

        socket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                if (data.type === 'vessel_update') {
                    setVessels(prev => {
                        const index = prev.findIndex(v => v.mmsi === data.data.mmsi);
                        const updatedVessel = {
                            mmsi: data.data.mmsi,
                            name: data.data.name,
                            flag: prev[index]?.flag || "UNKNOWN",
                            vessel_type: data.data.vessel_type || prev[index]?.vessel_type || "Unknown",
                            risk: data.data.risk_score
                        };

                        if (index !== -1) {
                            const next = [...prev];
                            next[index] = updatedVessel;
                            return next;
                        }
                        return [...prev, updatedVessel];
                    });
                }
            } catch (err) {
                console.error("Coherence Error: WebSocket parse failed", err);
            }
        };

        return () => socket.close();
    }, []);

    return (
        <div style={{
            padding: '24px',
            background: 'rgba(2, 6, 23, 0.4)',
            height: '100%',
            overflowY: 'auto'
        }}>
            <h3 style={{ fontSize: '1.1rem', marginBottom: '20px', color: '#94a3b8', letterSpacing: '1px' }}>MONITORED TARGETS</h3>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {vessels.map(v => (
                    <div key={v.mmsi} style={{
                        padding: '16px',
                        background: 'rgba(30, 41, 59, 0.4)',
                        border: '1px solid rgba(255, 255, 255, 0.05)',
                        borderRadius: '12px',
                        cursor: 'pointer',
                        transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
                    }}
                        onMouseEnter={e => e.currentTarget.style.transform = 'translateX(4px)'}
                        onMouseLeave={e => e.currentTarget.style.transform = 'translateX(0)'}
                    >
                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                            <span style={{ fontWeight: 700, fontSize: '0.9rem' }}>{v.name}</span>
                            <span style={{
                                fontSize: '0.7rem',
                                padding: '2px 8px',
                                borderRadius: '10px',
                                backgroundColor: v.risk > 0.8 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(56, 189, 248, 0.1)',
                                color: v.risk > 0.8 ? '#ef4444' : '#38bdf8',
                                fontWeight: 600
                            }}>
                                RISK: {v.risk.toFixed(2)}
                            </span>
                        </div>
                        <div style={{ fontSize: '0.8rem', color: '#64748b', display: 'flex', gap: '12px' }}>
                            <span>MMSI: {v.mmsi}</span>
                            <span>Flag: {v.flag}</span>
                            <span>{v.vessel_type}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default VesselList;
