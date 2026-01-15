import React from 'react';
import { Activity, Cpu } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const TelemetryChart = ({ data }) => {
    if (!data) {
        return (
            <div className="glass-panel p-6 lg:col-span-2 min-h-[500px] flex flex-col">
                <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
                    <Activity className="text-cyan-400" /> Real-time Telemetry
                </h2>
                <div className="flex-1 flex flex-col items-center justify-center text-gray-500">
                    <Cpu size={64} className="mb-4 opacity-20" />
                    <p>System Ready. Awaiting quantum tasks.</p>
                </div>
            </div>
        );
    }

    return (
        <div className="glass-panel p-6 lg:col-span-2 min-h-[500px] flex flex-col">
            <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
                <Activity className="text-cyan-400" /> Real-time Telemetry
            </h2>

            <div className="flex-1">
                <div className="grid grid-cols-2 gap-4 mb-6">
                    <div className="bg-white/5 p-4 rounded-lg">
                        <p className="text-gray-400 text-xs uppercase">Final Energy</p>
                        <p className="text-2xl font-mono text-cyan-400">{data.final_energy.toFixed(6)}</p>
                    </div>
                    <div className="bg-white/5 p-4 rounded-lg">
                        <p className="text-gray-400 text-xs uppercase">Best Solution Found</p>
                        <p className="text-sm font-mono text-purple-300 break-all">
                            [{data.final_solution.map(x => x.toFixed(3)).join(', ')}]
                        </p>
                    </div>
                </div>

                <div className="h-[300px] w-full">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={data.history}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#333" />
                            <XAxis dataKey="step" stroke="#666" />
                            <YAxis stroke="#666" />
                            <Tooltip
                                contentStyle={{ backgroundColor: '#050510', border: '1px solid #333' }}
                                itemStyle={{ color: '#fff' }}
                            />
                            <Line
                                type="monotone"
                                dataKey="energy"
                                stroke="#00f2ff"
                                strokeWidth={2}
                                dot={false}
                            />
                            <Line
                                type="monotone"
                                dataKey="best_energy"
                                stroke="#7000ff"
                                strokeWidth={2}
                                dot={false}
                                strokeDasharray="5 5"
                            />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            </div>
        </div>
    );
};

export default TelemetryChart;
