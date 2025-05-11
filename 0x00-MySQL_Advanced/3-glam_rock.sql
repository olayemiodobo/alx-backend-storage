-- Script to list all Glam rock bands ranked by their longevity

-- Calculate the lifespan as the difference between 2022 and the year they were formed.
-- If the band has split, use the split year instead of 2022.

SELECT 
    band_name,
    CASE 
        WHEN split IS NOT NULL THEN split - formed
        ELSE 2022 - formed
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam%'
ORDER BY 
    lifespan DESC;
