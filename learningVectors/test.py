from car_data_etl import prepare_car_reviews_data
DATA_PATH = "data/archive/*"

chroma_car_reviews_dict = prepare_car_reviews_data(DATA_PATH)
chroma_car_reviews_dict.keys()
# dict_keys(['ids', 'documents', 'metadatas'])

chroma_car_reviews_dict["ids"][-10]
# 'review5860'

print(chroma_car_reviews_dict["documents"][-10])
# I've never had a perfect car for me but this is quite close. My husband
# refused to ever drive an SUV but he loves this car. He's always looking
# for an excuse to drive. It has power! There are lots of extras in the
# inscription that are worth the extra money. I like the larger tires and
# leather quality especially. My kids love the car too and prefer to ride
# in the "way back". Some of the technology is tricky but you do get the
# hang of it and there are so many features that it's worth the effort to
# learn it.

print(chroma_car_reviews_dict["metadatas"][-10])
# {'Review_Title': 'Very happy!', 'Rating': 5.0, 'Vehicle_Year': 2017, 'Vehicle_Model': 'Volvo'}