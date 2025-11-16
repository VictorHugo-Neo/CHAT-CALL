export function ChatWindow() {
  return (
    <div className="flex-grow p-4 overflow-y-auto bg-gray-50">
      {/* As mensagens do chat (role 'user' e 'ai') aparecerão aqui */}

      <div className="text-center text-gray-400 mt-4">
        A conversa começa aqui.
      </div>
    </div>
  );
}