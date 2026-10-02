"""
Servicio de IA para Hi Learning (Capa Adaptativa de Rol y Feedback).
Maneja la interacción con Google Gemini API o provee simulación inteligente local si no hay API key configurada.
"""

import os
from typing import Tuple, List, Dict
from core.types import Turno


# Prompts de sistema para cada escenario de rol
SCENARIOS = {
    "☕ Coffee Shop": {
        "title": "Barista at Central Perk",
        "description": "Order coffee and pastries in a busy cafe setting.",
        "system_prompt": (
            "You are a friendly, conversational barista at a cozy coffee shop. "
            "Your goal is to have a natural 5-minute English practice dialogue with a customer. "
            "Ask short, conversational questions (1-2 sentences maximum). "
            "Never lecture or correct the student's grammar during the dialogue; simply maintain the immersive role."
        ),
        "initial_message": "Hi there! Welcome to Central Coffee. What can I get started for you today?"
    },
    "💼 Job Interview": {
        "title": "Hiring Manager at TechCorp",
        "description": "Practice answering common professional interview questions.",
        "system_prompt": (
            "You are an encouraging hiring manager conducting an initial screening interview in English. "
            "Keep your questions concise (1-2 sentences). "
            "Ask about background, strengths, and interest in the role."
        ),
        "initial_message": "Hello! Thank you for joining today's interview. Could you briefly tell me about yourself?"
    },
    "✈️ Airport Check-in": {
        "title": "Airline Gate Agent",
        "description": "Check in for an international flight and navigate travel questions.",
        "system_prompt": (
            "You are an airline customer service agent at the check-in desk. "
            "Help the passenger with their luggage, seat selection, and passport verification in English. "
            "Keep replies brief and clear."
        ),
        "initial_message": "Good morning! Welcome to SkyAir. Where are you flying to today?"
    }
}


def responder_rol_conversacional(
    scenario_key: str,
    historial: Tuple[Turno, ...],
    api_key: str = ""
) -> str:
    """
    Genera la respuesta del personaje de IA.
    Si se dispone de api_key (o en variable de entorno GEMINI_API_KEY), llama a Gemini.
    De lo contrario, usa respuestas simuladas contextuales para pruebas inmediatas.
    """
    key = api_key or os.environ.get("GEMINI_API_KEY", "")
    scenario = SCENARIOS.get(scenario_key, SCENARIOS["☕ Coffee Shop"])

    if key:
        try:
            from google import genai
            client = genai.Client(api_key=key)
            
            # Formatear el historial para el contexto
            prompt_context = f"Role: {scenario['system_prompt']}\n\nConversation so far:\n"
            for t in historial:
                rol = "Student" if t.emisor == "user" else "Assistant"
                prompt_context += f"{rol}: {t.texto}\n"
            prompt_context += "\nAssistant (keep response under 35 words):"

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_context
            )
            if response.text:
                return response.text.strip()
        except Exception as e:
            # Fallback en caso de error de red o cuota
            pass

    # Respuestas de contingencia / fallback simulado (para probar sin configurar API key)
    turnos_usuario = [t for t in historial if t.emisor == "user"]
    num_turnos = len(turnos_usuario)
    
    simulated_dialogues = {
        "☕ Coffee Shop": [
            "Great choice! Would you like that iced or hot, and what size?",
            "Got it! Do you prefer regular milk, oat milk, or almond milk?",
            "Perfect. Would you like any pastries or snacks to go with that today?",
            "Awesome. That will be $4.50. Will you be paying with cash or card?",
            "Here is your receipt and order! Enjoy your drink and have a fantastic day!"
        ],
        "💼 Job Interview": [
            "That sounds like great experience! What would you say is one of your key strengths?",
            "Interesting! How do you typically handle working under tight deadlines?",
            "Thanks for sharing that. Why are you specifically interested in this position?",
            "Great answer! Do you have any questions for me about our team culture?",
            "Thank you so much for your time today. We will follow up with next steps soon!"
        ],
        "✈️ Airport Check-in": [
            "May I please see your passport and booking confirmation number?",
            "Thank you! Do you have any checked bags or just carry-on luggage?",
            "Would you prefer a window seat or an aisle seat for your flight?",
            "All set! Your gate is B14 and boarding begins at 3:30 PM. Any questions?",
            "Have a safe and pleasant flight! Thank you for flying with us."
        ]
    }
    
    opciones = simulated_dialogues.get(scenario_key, simulated_dialogues["☕ Coffee Shop"])
    indice = min(num_turnos - 1, len(opciones) - 1)
    if indice >= 0:
        return opciones[indice]
    return "Could you please tell me more about that?"
