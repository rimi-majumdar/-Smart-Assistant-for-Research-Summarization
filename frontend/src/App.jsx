import React, { useState } from "react";
import { FaBrain, FaBolt } from "react-icons/fa";

export default function App() {
  const [mode, setMode] = useState("ask");
  const [history, setHistory] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    const newEntry = { role: mode === "ask" ? "🧠 Ask Me" : "🎯 Challenge", message: input };
    setHistory([newEntry, ...history]);
    setInput("");
  };

  return (
    <div className="flex h-screen bg-[#0d1117] text-white font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-[#161b22] p-6 flex flex-col justify-between">
        <div>
          <h1 className="text-2xl font-bold mb-8 text-purple-400">Smart Assistant</h1>
          <nav className="space-y-4">
            <button
              onClick={() => setMode("ask")}
              className={`w-full flex items-center space-x-2 px-4 py-2 rounded-lg ${
                mode === "ask" ? "bg-purple-600 text-white" : "hover:bg-[#1f2937]"
              }`}
            >
              <FaBrain /> <span>Ask Me</span>
            </button>
            <button
              onClick={() => setMode("challenge")}
              className={`w-full flex items-center space-x-2 px-4 py-2 rounded-lg ${
                mode === "challenge" ? "bg-purple-600 text-white" : "hover:bg-[#1f2937]"
              }`}
            >
              <FaBolt /> <span>Challenge Me</span>
            </button>
          </nav>
        </div>
        <div className="text-sm text-gray-400">
          <p>Pro Access</p>
          <p className="text-purple-300 font-bold">$10/month</p>
        </div>
      </aside>

      {/* Main Chat Interface */}
      <main className="flex-1 p-6 flex flex-col">
        <div className="text-xl font-bold mb-2">
          {mode === "ask" ? "💬 Ask Me Anything" : "🧠 Challenge Questions"}
        </div>
        <div className="flex-1 bg-[#161b22] rounded-xl p-6 shadow-inner overflow-y-auto">
          {history.length === 0 ? (
            <p className="text-gray-400">No messages yet. Start a conversation!</p>
          ) : (
            <ul className="space-y-3">
              {history.map((entry, idx) => (
                <li key={idx} className="bg-[#21262d] p-4 rounded-lg">
                  <div className="text-sm text-purple-300 font-semibold">{entry.role}</div>
                  <div>{entry.message}</div>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="mt-4 flex items-center bg-[#1f2937] rounded-xl px-4 py-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 bg-transparent outline-none text-white placeholder-gray-400"
          />
          <button
            onClick={handleSend}
            className="ml-4 bg-purple-600 px-4 py-2 rounded-lg hover:bg-purple-700"
          >
            Send
          </button>
        </div>
      </main>

      {/* Chat History Panel */}
      <aside className="w-80 bg-[#161b22] p-4 border-l border-gray-700">
        <h2 className="text-lg font-bold mb-4 text-purple-200">History</h2>
        <ul className="text-sm text-gray-300 space-y-2">
          {history.map((entry, i) => (
            <li key={i} className="truncate">{entry.role}: {entry.message.slice(0, 40)}...</li>
          ))}
        </ul>
      </aside>
    </div>
  );
}