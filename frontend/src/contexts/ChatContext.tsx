import { createContext, useContext, useState, type ReactNode, useEffect} from 'react';
import { fetchAiResponse, fetchHistory, type Message } from '../services/apiService';

type ChatContextType = {
  messages: Message[];
  isLoading: boolean;
  sendMessage: (pergunta: string) => Promise<void>;
};


const ChatContext = createContext<ChatContextType | undefined>(undefined);

export function ChatProvider({ children }: { children: ReactNode }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
  
    const loadHistory = async () => {
      setIsLoading(true); 
      try {
        const historyMessages = await fetchHistory();
        setMessages(historyMessages); 
      } catch (error) {
        console.error("Erro ao carregar histórico:", error);
        
        setMessages([{ 
          role: 'ai', 
          content: 'Não foi possível carregar o histórico.' 
        }]);
      } finally {
        setIsLoading(false);
      }
    };

    loadHistory();
  }, []);
  
  const sendMessage = async (pergunta: string) => {
    if (!pergunta.trim()) return;

    const userMessage: Message = { role: 'user', content: pergunta };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    
    setIsLoading(true);

    try {
      const aiContent = await fetchAiResponse(pergunta);
      const aiMessage: Message = { role: 'ai', content: aiContent };
      
      setMessages((prevMessages) => [...prevMessages, aiMessage]);
    } catch (error) {
      console.error(error);
      const errorMessage: Message = { 
        role: 'ai', 
        content: 'Desculpe, ocorreu um erro. Tente novamente.' 
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const value = {
    messages,
    isLoading,
    sendMessage,
  };

  return <ChatContext.Provider value={value}>{children}</ChatContext.Provider>;
}
// eslint-disable-next-line react-refresh/only-export-components
export function useChat() {
  const context = useContext(ChatContext);
  if (context === undefined) {
    throw new Error('useChat deve ser usado dentro de um ChatProvider');
  }
  return context;
}