--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: film_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film_info (
    id_film integer NOT NULL,
    name_film character varying(100) NOT NULL,
    name_producer character varying(100) NOT NULL,
    release_film integer NOT NULL
);


ALTER TABLE public.film_info OWNER TO postgres;

--
-- Name: film_info_id_film_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_info_id_film_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.film_info_id_film_seq OWNER TO postgres;

--
-- Name: film_info_id_film_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_info_id_film_seq OWNED BY public.film_info.id_film;


--
-- Name: film_info id_film; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film_info ALTER COLUMN id_film SET DEFAULT nextval('public.film_info_id_film_seq'::regclass);


--
-- Data for Name: film_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film_info (id_film, name_film, name_producer, release_film) FROM stdin;
1	Test	Test	2001
2	Test	Тест	2001
3	Темний лицар	Крістофер Нолан	2008
4	Форрест Гамп	Роберт Земекіс	1994
5	Форрест Гамп	Роберт Земекіс	1994
6	Матриця	Лана та Лілі Вачовські	1999
7	Втеча з Шоушенка	Френк Дарабонт	1994
8	Втеча з Шоушенка	Френк Дарабонт	1994
9	Гладіатор	Рідлі Скотт	2000
10	Інтерстеллар	Крістофер Нолан	2014
11	Запах жінки	Мартін Брест	1992
12	Джокер	Тодд Філліпс	2019
13	Джокер	Тодд Філліпс	2019
\.


--
-- Name: film_info_id_film_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_info_id_film_seq', 13, true);


--
-- PostgreSQL database dump complete
--

