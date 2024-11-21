import boto3
from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
  try:
    data = request.json
    text = data.get('text')
    voice = 'Mia'
    output_fromat = 'mp3'

    if not text:
      return jsonify({'error': 'No se recibio el texto'}), 400

    polly = boto3.client('polly', region_name='us-east-1')

    response = polly.synthesize_speech(
      text=text,
      output_fromat=output_fromat
      VoiceId=voice
    )

    audio_file = "output.mp3"
    with open(audio_file, 'wb') as f:
      file.write(response['AudioStream'].read())

    return send_file(audio_file, mimetype='audio/mpeg')
    
  except Exception as e:
    return jsonify({'error': str(e)}),500
    