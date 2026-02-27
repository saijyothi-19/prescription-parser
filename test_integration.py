from translation_voice import process_prescription

data = {
    "medicine": "Amoxicillin",
    "dosage": "250mg",
    "frequency": "Three times daily",
    "duration": "7 days"
}

result = process_prescription(data)

print("\n--- INTEGRATION TEST OUTPUT ---\n")
print(result)