use ht22_1_project_group_14;
SELECT DISTINCT HK_Prod_title
FROM HasKeywords
WHERE HK_Word in (SELECT HK_Word FROM HasKeywords Where HK_Prod_title="Car");
