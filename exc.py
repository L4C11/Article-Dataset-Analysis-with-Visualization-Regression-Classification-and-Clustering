import pandas as pd

data = {
    'Oszlop neve': ['timedelta', 'n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'n_non_stop_words', 'n_non_stop_unique_tokens', 'num_hrefs', 'num_self_hrefs', 'num_imgs', 'num_videos', 'average_token_length', 'num_keywords', 'data_channel_is_lifestyle', 'data_channel_is_entertainment', 'data_channel_is_bus', 'data_channel_is_socmed', 'data_channel_is_tech', 'data_channel_is_world', 'kw_min_min', 'kw_max_min', 'kw_avg_min', 'kw_min_max', 'kw_max_max', 'kw_avg_max', 'kw_min_avg', 'kw_max_avg', 'kw_avg_avg', 'self_reference_min_shares', 'self_reference_max_shares', 'self_reference_avg_sharess', 'weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday', 'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday', 'weekday_is_sunday', 'is_weekend', 'LDA_00', 'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04', 'global_subjectivity', 'global_sentiment_polarity', 'global_rate_positive_words', 'global_rate_negative_words', 'rate_positive_words', 'rate_negative_words', 'avg_positive_polarity', 'min_positive_polarity', 'max_positive_polarity', 'avg_negative_polarity', 'min_negative_polarity', 'max_negative_polarity', 'title_subjectivity', 'title_sentiment_polarity', 'abs_title_subjectivity', 'abs_title_sentiment_polarity', 'shares'],
    'Minimum': [122.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, -1.0, 0.0, 67500.0, 18020.0, 0.0, 3478.6, 889.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, -1.0, 0.0, -1.0, -1.0, 0.0, -1.0, 0.0, 35],
    'Maximum': [202.0, 20.0, 7764.0, 701.0, 1042.0, 650.0, 145.0, 31.0, 100.0, 58.0, 6.8, 10.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 77600.0, 13078.5, 843300.0, 843300.0, 843300.0, 843300.0, 3562.1, 135124.6, 20377.6, 690400.0, 690400.0, 690400.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9, 0.9, 0.9, 0.9, 0.9, 1.0, 0.6, 0.1, 0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 109800],
    'Terjedelem': [80.0, 16.0, 7764.0, 701.0, 1042.0, 650.0, 145.0, 31.0, 100.0, 58.0, 6.8, 9.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 77600.0, 13079.5, 843300.0, 843300.0, 825280.0, 3562.1, 131646.0, 19488.4, 690400.0, 690400.0, 690400.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9, 0.9, 0.9, 0.9, 0.9, 1.0, 0.8, 0.1, 0.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 0.5, 1.0, 109765]
}

# DataFrame létrehozása
df = pd.DataFrame(data)

# Excel fájl létrehozása
df.to_excel('adatok.xlsx', index=False)

