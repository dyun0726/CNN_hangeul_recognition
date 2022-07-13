import tensorflow as tf
import os
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"]='0'

model = tf.keras.models.load_model('./model/25_32.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_float_model = converter.convert()

# Show model size in KBs.
float_model_size = len(tflite_float_model) / 1024
print('Float model size = %dKBs.' % float_model_size)


# Lite 모델 양자화로 크기 줄이는 과정
# Re-convert the model to TF Lite using quantization.
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quantized_model = converter.convert()
# Show model size in KBs.
quantized_model_size = len(tflite_quantized_model) / 1024
print('Quantized model size = %dKBs,' % quantized_model_size)
print('which is about %d%% of the float model size.'\
      % (quantized_model_size * 100 / float_model_size))

# TFlite 모델 저장
# Save the quantized model to file to the Downloads directory
f = open('./tflite/hangeul.tflite', "wb")
f.write(tflite_float_model)
f.close()
