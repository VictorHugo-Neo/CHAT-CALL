import { ChatWindow } from './components/ChatWindow';
import { MessageInput } from './components/MessageInput';

function App() {
  return (
    <div className="flex flex-col h-screen bg-gray-100">
      
      <header className="bg-white shadow-md p-4">
        <h1 className="text-xl font-bold text-center text-gray-800">
          ChatCall AI
        </h1>
      </header>
      <ChatWindow />
      <MessageInput />

    </div>
  );
}

export default App;