import tensorflow as tf

saved_model_dir = tf.keras.models.load_model('traincnn.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_types = [tf.float16]
tflite_quant_model = converter.convert()

# 변환된 모델 저장
with open('test_fivecnn.tflite', 'wb') as f:
    f.write(tflite_quant_model)