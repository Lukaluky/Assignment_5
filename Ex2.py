from abc import ABC, abstractmethod

# Base class for data types
class Data:
    def __init__(self, type, content):
        self.type = type
        self.content = content

# Abstract Data Processor class using the Factory Method pattern
class DataProcessor(ABC):
    @abstractmethod
    def process_data(self, data):
        pass

# Concrete Data Processor for Text Data
class TextDataProcessor(DataProcessor):
    def process_data(self, data):
        print(f"Processing text data: {data.content}")
        # Additional text-specific processing logic can be implemented here

# Concrete Data Processor for Audio Data
class AudioDataProcessor(DataProcessor):
    def process_data(self, data):
        print(f"Processing audio data: {data.content}")
        # Additional audio-specific processing logic can be implemented here

# Concrete Data Processor for Video Data
class VideoDataProcessor(DataProcessor):
    def process_data(self, data):
        print(f"Processing video data: {data.content}")
        # Additional video-specific processing logic can be implemented here

# Creator class that manages data processing
class DataProcessorCreator:
    def __init__(self, processor=None):
        self.processor = processor

    def set_processor(self, processor):
        self.processor = processor

    def process_data(self, data):
        if self.processor:
            self.processor.process_data(data)
        else:
            print("Data processor is not set.")

# Main function to demonstrate data processing
def main():
    # Example data of different types
    text_data = Data("text", "Here is some text.")
    audio_data = Data("audio", b"Some audio bytes.")
    video_data = Data("video", b"Some video bytes.")

    # Creating the processor manager
    processor_creator = DataProcessorCreator()

    # Setting and using a text processor
    processor_creator.set_processor(TextDataProcessor())
    processor_creator.process_data(text_data)

    # Setting and using an audio processor
    processor_creator.set_processor(AudioDataProcessor())
    processor_creator.process_data(audio_data)

    # Setting and using a video processor
    processor_creator.set_processor(VideoDataProcessor())
    processor_creator.process_data(video_data)

if __name__ == "__main__":
    main()
