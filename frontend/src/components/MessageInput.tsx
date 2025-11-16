import { useState } from 'react';
import { useChat } from '../contexts/ChatContext'; 
export function MessageInput() {
  const [inputValue, setInputValue] = useState('');
  const { sendMessage, isLoading } = useChat(); 

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); 
    sendMessage(inputValue); 
    setInputValue(''); 
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-gray-100 border-t border-gray-300">
      <div className="flex rounded-lg shadow-sm">
        <input
          type="text"
          className="flex-grow p-3 border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-200"
          placeholder={isLoading ? "Pensando..." : "Digite sua mensagem..."}
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          disabled={isLoading}
        />
        <button
          type="submit"
          className="bg-blue-600 text-white p-3 rounded-r-lg font-semibold hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-blue-400"
          disabled={isLoading} 
        >
          {isLoading ? "..." : "Enviar"}
        </button>
      </div>
    </form>
  );
}