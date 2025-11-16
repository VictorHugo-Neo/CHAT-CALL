const API_URL = "http://127.0.0.1:8000/api/v1/chat";

export type Message = {
  role: 'user' | 'ai';
  content: string;
}
type ApiResponse = {
  resposta: string;
}

export async function fetchAiResponse(pergunta: string): Promise<string> {
  const response = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ pergunta }),
  });

  if (!response.ok) {
    throw new Error("Falha na requisição da API");
  }

  const data = (await response.json()) as ApiResponse;
  return data.resposta;
}