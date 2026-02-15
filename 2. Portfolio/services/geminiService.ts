
import { GoogleGenAI } from "@google/genai";
import { PROJECTS, EXPERIENCES, SKILLS, USER_INFO, EDUCATION } from '../constants';

const ai = new GoogleGenAI({ apiKey: process.env.API_KEY || '' });

const SYSTEM_INSTRUCTION = `
You are the personal AI assistant for ${USER_INFO.name}, a ${USER_INFO.title}. 
Your goal is to answer questions from visitors about Julien's portfolio, data science expertise, AI vision projects, and analytics experience.

Context about Julien:
- Professional Identity: ${USER_INFO.about}
- Key Skills: ${SKILLS.map(s => `${s.name} (${s.category})`).join(', ')}
- Work History: ${EXPERIENCES.map(e => `${e.role} at ${e.company} (${e.period}). Result: ${e.results}`).join('; ')}
- Education: ${EDUCATION.map(ed => `${ed.degree} from ${ed.institution}`).join('; ')}
- Notable Projects: ${PROJECTS.map(p => p.title + ": " + p.description).join('; ')}

Julien is an expert in Power BI, SQL, Python, and AI Vision (YOLO, PyTorch). He is currently available for opportunities.

Guidelines:
1. Be professional, analytical, and technical but accessible.
2. Emphasize his ability to bridge the gap between business needs and data solutions.
3. If asked about contact, provide his email: ${USER_INFO.email} or LinkedIn.
4. Keep answers concise. Use formatting to highlight key achievements.
`;

export async function chatWithAI(message: string, history: {role: 'user' | 'model', parts: {text: string}[]}[]) {
  try {
    const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: [
        ...history.map(h => ({ role: h.role, parts: h.parts })),
        { role: 'user', parts: [{ text: message }] }
      ],
      config: {
        systemInstruction: SYSTEM_INSTRUCTION,
        temperature: 0.7,
      },
    });

    return response.text;
  } catch (error) {
    console.error("Gemini API Error:", error);
    return "I'm having a bit of trouble processing your request. Please feel free to reach out to Julien directly via email!";
  }
}
