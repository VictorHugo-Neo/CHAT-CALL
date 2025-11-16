import { useChat } from '../contexts/ChatContext'; 
import { useEffect, useRef } from 'react';

export function ChatWindow() {
  const { messages } = useChat(); 
  const endOfMessagesRef = useRef<HTMLDivElement>(null); 

  useEffect(() => {
    endOfMessagesRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex-grow p-4 overflow-y-auto bg-gray-50 space-y-4">
      
      {messages.map((msg, index) => (
        <div
          key={index}
          className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
        >
          <div
            className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg shadow ${
              msg.role === 'user'
                ? 'bg-blue-600 text-white'
                : 'bg-white text-gray-800'
            }`}
          >
            
            <pre className="whitespace-pre-wrap font-sans">{msg.content}</pre>
          </div>
        </div>
      ))}
      <div ref={endOfMessagesRef} />
    </div>
  );
}