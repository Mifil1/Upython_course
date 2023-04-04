--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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

--
-- Name: gender; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.gender AS ENUM (
    'm',
    'f'
);


ALTER TYPE public.gender OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: gender_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gender_info (
    "Gender information:" character varying(100)
);


ALTER TABLE public.gender_info OWNER TO postgres;

--
-- Name: task1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task1 (
    info character varying(255)
);


ALTER TABLE public.task1 OWNER TO postgres;

--
-- Name: task2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task2 (
    answer character varying(255)
);


ALTER TABLE public.task2 OWNER TO postgres;

--
-- Name: task3; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task3 (
    name character varying(50),
    words integer
);


ALTER TABLE public.task3 OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(60) NOT NULL,
    pwd character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    gender public.gender NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: vocabulary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vocabulary (
    id integer NOT NULL,
    name character varying(255),
    info text
);


ALTER TABLE public.vocabulary OWNER TO postgres;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vocabulary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vocabulary_id_seq OWNER TO postgres;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vocabulary_id_seq OWNED BY public.vocabulary.id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.word (
    id integer NOT NULL,
    word character varying(255),
    vocabulary_id integer
);


ALTER TABLE public.word OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_id_seq OWNER TO postgres;

--
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: vocabulary id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vocabulary ALTER COLUMN id SET DEFAULT nextval('public.vocabulary_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: gender_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gender_info ("Gender information:") FROM stdin;
| We have 5 boys!  |
| We have 5 girls! |
\.


--
-- Data for Name: task1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task1 (info) FROM stdin;
| This is Vasya, he has email mmm@mmail.com |
| This is Alex, he has email mmm@gmail.com |
| This is Alexey, he has email alexey@gmail.com |
| This is Helen, she has email hell@gmail.com |
| This is Jenny, she has email eachup@gmail.com |
| This is Lora, she has email tpicks@gmail.com |
| This is Zhenia, he has email dwdw@mmail.com |
| This is Christina, she has email ddwgrtgs@l.com |
| This is Liza, she has email s@l.com |
| This is Pablo, he has email swda@l.com |
\.


--
-- Data for Name: task2; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task2 (answer) FROM stdin;
\.


--
-- Data for Name: task3; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task3 (name, words) FROM stdin;
animals	10
school	10
SF	10
human	10
nature	10
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, pwd, email, gender) FROM stdin;
1	Vasya	21341234qwfsdf	mmm@mmail.com	m
2	Alex	21341234	mmm@gmail.com	m
3	Alexey	qq21341234Q	alexey@gmail.com	m
4	Helen	MarryMeeee	hell@gmail.com	f
5	Jenny	SmakeMyb	eachup@gmail.com	f
6	Lora	burn23	tpicks@gmail.com	f
7	Zhenia	awdaw89789ad	dwdw@mmail.com	m
8	Christina	jhifgrahasfh8	ddwgrtgs@l.com	f
9	Liza	iawdpjk	s@l.com	f
10	Pablo	plkawdo	swda@l.com	m
\.


--
-- Data for Name: vocabulary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vocabulary (id, name, info) FROM stdin;
1	animals	\N
2	school	\N
3	nature	\N
4	human	\N
5	SF	\N
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.word (id, word, vocabulary_id) FROM stdin;
1	turtle	1
2	pig	1
3	dog	1
4	cat	1
5	lizard	1
6	cow	1
7	rabbit	1
8	frog	1
9	headgehog	1
10	goat	1
11	desk	2
12	book	2
13	chalk	2
14	pen	2
15	pencil	2
16	copybook	2
17	lesson	2
18	teacher	2
19	pupils	2
20	school	2
21	ray	3
22	thunder	3
23	sun	3
24	field	3
25	hill	3
26	mountain	3
27	river	3
28	forest	3
29	grass	3
30	rain	3
31	hair	4
32	nail	4
33	finger	4
34	eye	4
35	tooth	4
36	knee	4
37	elbow	4
38	leg	4
39	arm	4
40	head	4
41	engine	5
42	steel	5
43	power	5
44	nuclear	5
45	shotgun	5
46	laser	5
47	flight	5
48	energy	5
49	Moon	5
50	splace	5
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 10, true);


--
-- Name: vocabulary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vocabulary_id_seq', 5, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.word_id_seq', 50, true);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

