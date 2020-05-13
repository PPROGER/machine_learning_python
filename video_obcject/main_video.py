from imageai.Detection import VideoObjectDetection
import os

def Detection_object_video(path_model,path_input,path_output,frames_per_seconds):
	execution_path = os.getcwd()

	detector = VideoObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath( os.path.join(execution_path , str(path_model)))
	detector.loadModel()

	video_path = detector.detectObjectsFromVideo(
		input_file_path=os.path.join(execution_path, str(path_input)),
		output_file_path=os.path.join(execution_path, str(path_output)),
		frames_per_second=int(frames_per_seconds),
		log_progress=True
	)

	print(video_path)