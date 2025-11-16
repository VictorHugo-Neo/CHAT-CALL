import { ChatWindow } from './components/ChatWindow';
import { MessageInput } from './components/MessageInput';

function App() {
  return (
    // Layout principal que ocupa a tela inteira
    <div className="flex flex-col h-screen bg-gray-100">

      {/* 1. Cabeçalho */}
      <header className="bg-white shadow-md p-4">
        <h1 className="text-xl font-bold text-center text-gray-800">
          ChatCall AI
        </h1>
      </header>

      {/* 2. Janela do Chat (ocupa o espaço restante) */}
      <ChatWindow />

      {/* 3. Input da Mensagem (na parte inferior) */}
      <MessageInput />

    </div>
  );
}

export default App;