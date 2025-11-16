export function MessageInput() {
  return (
    <form className="p-4 bg-gray-100 border-t border-gray-300">
      <div className="flex rounded-lg shadow-sm">
        <input
          type="text"
          className="flex-grow p-3 border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Digite sua mensagem..."
        />
        <button
          type="submit"
          className="bg-blue-600 text-white p-3 rounded-r-lg font-semibold hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Enviar
        </button>
      </div>
    </form>
  );
}