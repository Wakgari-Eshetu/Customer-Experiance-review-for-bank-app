DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS banks;

CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) NOT NULL,
    app_name VARCHAR(255)
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text TEXT NOT NULL,
    rating INT CHECK (rating >= 0 AND rating <= 5),
    review_date DATE,
    sentiment_label VARCHAR(50),
    sentiment_score FLOAT,
    source VARCHAR(100)
);
ALTER TABLE banks
ADD CONSTRAINT unique_bank_name UNIQUE (bank_name);

--Count reviews per bank
SELECT b.bank_name, COUNT(r.review_id) AS total_reviews
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name   
ORDER BY total_reviews DESC;

--Average rating per bank
SELECT b.bank_name, AVG(r.rating) AS avg_rating
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
GROUP BY b.bank_name
ORDER BY avg_rating DESC;

--sentiment distribution per bank
SELECT b.bank_name, r.sentiment_label, COUNT(r.review_id) AS sentiment_count    
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id   
GROUP BY b.bank_name, r.sentiment_label    
ORDER BY b.bank_name, sentiment_count DESC;

--Top rated reviews per bank
SELECT b.bank_name, r.review_text, r.rating
FROM banks b
LEFT JOIN reviews r ON b.bank_id = r.bank_id
WHERE r.rating = 5
ORDER BY b.bank_name;
--count reviews by sentimnent
SELECT 
    b.bank_name,
    r.sentiment_label,
    COUNT(*) AS sentiment_count
FROM 
    reviews r
JOIN 
    banks b 
ON 
    r.bank_id = b.bank_id
GROUP BY 
    b.bank_name, r.sentiment_label
ORDER BY 
    b.bank_name, sentiment_count DESC;



