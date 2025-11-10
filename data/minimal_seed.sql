--
-- PostgreSQL database dump
--

\restrict JOOOFm2RnEaf1F019WJSYViwYkK9lweUobCrE1EzrtWGvRVgh3LMzrLSdCrG7xn

-- Dumped from database version 14.19 (Debian 14.19-1.pgdg13+1)
-- Dumped by pg_dump version 14.19 (Debian 14.19-1.pgdg13+1)

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
-- Data for Name: auth_app_user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.auth_app_user (id, password, last_login, is_superuser, email, is_active, is_staff, created_at, updated_at) VALUES (4, 'pbkdf2_sha256$720000$9KqbO4oH6iQbH8ID5316EG$8Wkx38jPrMb3SdUta4gJ6ulf+RhKCfXkJ2Ch0CpdURE=', NULL, false, 'debug@example.com', true, false, '2025-09-27 18:29:39.370805+00', '2025-09-27 18:29:39.370829+00');
INSERT INTO public.auth_app_user (id, password, last_login, is_superuser, email, is_active, is_staff, created_at, updated_at) VALUES (5, 'testpass123', NULL, false, 'querytest@example.com', true, false, '2025-10-04 10:04:30.617549+00', '2025-10-04 10:04:30.61757+00');
INSERT INTO public.auth_app_user (id, password, last_login, is_superuser, email, is_active, is_staff, created_at, updated_at) VALUES (1, 'pbkdf2_sha256$1000000$CMg9DwhasRy8yxIMmUFCUR$66hi2OBeJbaOsPLcRP4qL5FtJ/4sSJ6RtQ4/C1vxFiQ=', NULL, false, 'uakinderua@gmail.com', true, false, '2025-09-14 10:44:12.176349+00', '2025-09-14 10:44:12.176361+00');


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: auth_app_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sites', 'site');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'authtoken', 'token');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'authtoken', 'tokenproxy');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'movie', 'movie');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'movie', 'likemovie');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'movie', 'watchlatermovie');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'movie', 'actor');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'movie', 'director');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'movie', 'genre');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'movie', 'country');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (16, 'movie', 'language');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (17, 'movie', 'writer');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (18, 'movie', 'rating');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (19, 'auth_app', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (20, 'account', 'emailaddress');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (21, 'account', 'emailconfirmation');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (22, 'socialaccount', 'socialaccount');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (23, 'socialaccount', 'socialapp');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (24, 'socialaccount', 'socialtoken');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (25, 'movie', 'recommendedmovie');


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add site', 6, 'add_site');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change site', 6, 'change_site');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete site', 6, 'delete_site');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view site', 6, 'view_site');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add Token', 7, 'add_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change Token', 7, 'change_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete Token', 7, 'delete_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view Token', 7, 'view_token');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add Token', 8, 'add_tokenproxy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change Token', 8, 'change_tokenproxy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete Token', 8, 'delete_tokenproxy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view Token', 8, 'view_tokenproxy');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add movie', 9, 'add_movie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change movie', 9, 'change_movie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete movie', 9, 'delete_movie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view movie', 9, 'view_movie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add like movie', 10, 'add_likemovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change like movie', 10, 'change_likemovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete like movie', 10, 'delete_likemovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view like movie', 10, 'view_likemovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add watch later movie', 11, 'add_watchlatermovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change watch later movie', 11, 'change_watchlatermovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete watch later movie', 11, 'delete_watchlatermovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view watch later movie', 11, 'view_watchlatermovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add actor', 12, 'add_actor');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change actor', 12, 'change_actor');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete actor', 12, 'delete_actor');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view actor', 12, 'view_actor');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add director', 13, 'add_director');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change director', 13, 'change_director');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete director', 13, 'delete_director');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view director', 13, 'view_director');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add genre', 14, 'add_genre');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change genre', 14, 'change_genre');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete genre', 14, 'delete_genre');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view genre', 14, 'view_genre');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can add country', 15, 'add_country');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can change country', 15, 'change_country');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can delete country', 15, 'delete_country');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can view country', 15, 'view_country');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (61, 'Can add language', 16, 'add_language');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (62, 'Can change language', 16, 'change_language');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (63, 'Can delete language', 16, 'delete_language');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (64, 'Can view language', 16, 'view_language');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (65, 'Can add writer', 17, 'add_writer');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (66, 'Can change writer', 17, 'change_writer');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (67, 'Can delete writer', 17, 'delete_writer');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (68, 'Can view writer', 17, 'view_writer');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (69, 'Can add rating', 18, 'add_rating');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (70, 'Can change rating', 18, 'change_rating');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (71, 'Can delete rating', 18, 'delete_rating');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (72, 'Can view rating', 18, 'view_rating');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (73, 'Can add user', 19, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (74, 'Can change user', 19, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (75, 'Can delete user', 19, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (76, 'Can view user', 19, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (77, 'Can add email address', 20, 'add_emailaddress');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (78, 'Can change email address', 20, 'change_emailaddress');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (79, 'Can delete email address', 20, 'delete_emailaddress');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (80, 'Can view email address', 20, 'view_emailaddress');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (81, 'Can add email confirmation', 21, 'add_emailconfirmation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (82, 'Can change email confirmation', 21, 'change_emailconfirmation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (83, 'Can delete email confirmation', 21, 'delete_emailconfirmation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (84, 'Can view email confirmation', 21, 'view_emailconfirmation');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (85, 'Can add social account', 22, 'add_socialaccount');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (86, 'Can change social account', 22, 'change_socialaccount');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (87, 'Can delete social account', 22, 'delete_socialaccount');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (88, 'Can view social account', 22, 'view_socialaccount');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (89, 'Can add social application', 23, 'add_socialapp');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (90, 'Can change social application', 23, 'change_socialapp');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (91, 'Can delete social application', 23, 'delete_socialapp');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (92, 'Can view social application', 23, 'view_socialapp');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (93, 'Can add social application token', 24, 'add_socialtoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (94, 'Can change social application token', 24, 'change_socialtoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (95, 'Can delete social application token', 24, 'delete_socialtoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (96, 'Can view social application token', 24, 'view_socialtoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (97, 'Can add recommended movie', 25, 'add_recommendedmovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (98, 'Can change recommended movie', 25, 'change_recommendedmovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (99, 'Can delete recommended movie', 25, 'delete_recommendedmovie');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (100, 'Can view recommended movie', 25, 'view_recommendedmovie');


--
-- Data for Name: auth_app_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2025-09-14 10:43:39.476037+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2025-09-14 10:43:39.482954+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'auth', '0001_initial', '2025-09-14 10:43:39.521084+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2025-09-14 10:43:39.526705+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'auth', '0003_alter_user_email_max_length', '2025-09-14 10:43:39.532686+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'auth', '0004_alter_user_username_opts', '2025-09-14 10:43:39.540063+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'auth', '0005_alter_user_last_login_null', '2025-09-14 10:43:39.546222+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'auth', '0006_require_contenttypes_0002', '2025-09-14 10:43:39.548121+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2025-09-14 10:43:39.554791+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0008_alter_user_username_max_length', '2025-09-14 10:43:39.560628+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2025-09-14 10:43:39.566811+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0010_alter_group_name_max_length', '2025-09-14 10:43:39.573733+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0011_update_proxy_permissions', '2025-09-14 10:43:39.579794+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2025-09-14 10:43:39.586157+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth_app', '0001_initial', '2025-09-14 10:43:39.617563+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'account', '0001_initial', '2025-09-14 10:43:39.65296+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'account', '0002_email_max_length', '2025-09-14 10:43:39.667736+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2025-09-14 10:43:39.698469+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'account', '0004_alter_emailaddress_drop_unique_email', '2025-09-14 10:43:39.717605+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'account', '0005_emailaddress_idx_upper_email', '2025-09-14 10:43:39.730862+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'account', '0006_emailaddress_lower', '2025-09-14 10:43:39.745214+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'account', '0007_emailaddress_idx_email', '2025-09-14 10:43:39.768251+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'account', '0008_emailaddress_unique_primary_email_fixup', '2025-09-14 10:43:39.782394+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'account', '0009_emailaddress_unique_primary_email', '2025-09-14 10:43:39.792812+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (25, 'admin', '0001_initial', '2025-09-14 10:43:39.813158+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (26, 'admin', '0002_logentry_remove_auto_add', '2025-09-14 10:43:39.823912+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (27, 'admin', '0003_logentry_add_action_flag_choices', '2025-09-14 10:43:39.833077+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (28, 'authtoken', '0001_initial', '2025-09-14 10:43:39.850822+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (29, 'authtoken', '0002_auto_20160226_1747', '2025-09-14 10:43:39.936023+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (30, 'authtoken', '0003_tokenproxy', '2025-09-14 10:43:39.939264+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (31, 'authtoken', '0004_alter_tokenproxy_options', '2025-09-14 10:43:39.944366+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (32, 'movie', '0001_initial', '2025-09-14 10:43:40.02219+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (33, 'movie', '0002_alter_movie_title', '2025-09-14 10:43:40.030734+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (34, 'movie', '0003_movie_genre_movie_plot', '2025-09-14 10:43:40.040149+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (35, 'movie', '0004_actor_director_genre_remove_movie_genre_movie_actors_and_more', '2025-09-14 10:43:40.129107+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (36, 'movie', '0005_country_language_writer_remove_movie_director_and_more', '2025-09-14 10:43:40.421421+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (37, 'sessions', '0001_initial', '2025-09-14 10:43:40.427372+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (38, 'sites', '0001_initial', '2025-09-14 10:43:40.429649+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (39, 'sites', '0002_alter_domain_unique', '2025-09-14 10:43:40.43298+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (40, 'socialaccount', '0001_initial', '2025-09-14 10:43:40.487058+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (41, 'socialaccount', '0002_token_max_lengths', '2025-09-14 10:43:40.500587+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (42, 'socialaccount', '0003_extra_data_default_dict', '2025-09-14 10:43:40.505869+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (43, 'socialaccount', '0004_app_provider_id_settings', '2025-09-14 10:43:40.516291+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (44, 'socialaccount', '0005_socialtoken_nullable_app', '2025-09-14 10:43:40.529737+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (45, 'socialaccount', '0006_alter_socialaccount_extra_data', '2025-09-14 10:43:40.54049+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (46, 'movie', '0006_alter_rating_movie', '2025-09-14 10:54:22.209977+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (47, 'movie', '0007_rename_released_movie_released_date', '2025-09-14 12:57:48.664582+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (48, 'movie', '0008_alter_movie_awards_alter_movie_imdb_rating_and_more', '2025-09-18 14:38:06.11008+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (49, 'movie', '0009_recommendedmovie', '2025-09-27 20:44:02.738311+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (50, 'movie', '0010_recommendedmovie_deactivated_at_and_more', '2025-09-28 10:27:22.315171+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (51, 'movie', '0011_alter_recommendedmovie_options_and_more', '2025-09-28 10:27:22.364303+00');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.django_site (id, domain, name) VALUES (1, 'example.com', 'example.com');


--
-- Data for Name: movie_actor; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (1, 'Owen Wilson', '2025-09-14 10:49:55.482921+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (2, 'Bonnie Hunt', '2025-09-14 10:49:55.492616+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (3, 'Paul Newman', '2025-09-14 10:49:55.501517+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (4, 'Larry the Cable Guy', '2025-09-14 10:49:56.055754+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (5, 'Michael Caine', '2025-09-14 10:49:56.062841+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (6, 'Cristela Alonzo', '2025-09-14 10:49:56.694423+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (7, 'Chris Cooper', '2025-09-14 10:49:56.701478+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (8, 'Carlos Alazraqui', '2025-09-14 10:49:57.624826+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (9, 'Dane Cook', '2025-09-14 10:49:57.630572+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (10, 'Stacy Keach', '2025-09-14 10:49:57.635861+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (11, 'Ed Harris', '2025-09-14 10:49:58.138052+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (12, 'Julie Bowen', '2025-09-14 10:49:58.144761+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (13, 'Jeffrey Wright', '2025-09-14 10:55:48.65222+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (14, 'Frances McDormand', '2025-09-14 10:55:48.658909+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (15, 'Maleah Nipay-Padilla', '2025-09-14 10:55:48.667471+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (16, 'Kelly Macdonald', '2025-09-14 10:55:49.234844+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (17, 'Billy Connolly', '2025-09-14 10:55:49.258272+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (18, 'Emma Thompson', '2025-09-14 10:55:49.266843+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (19, 'Anthony Gonzalez', '2025-09-14 10:55:49.66128+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (20, 'Gael García Bernal', '2025-09-14 10:55:49.668139+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (21, 'Benjamin Bratt', '2025-09-14 10:55:49.674842+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (22, 'Auli''i Cravalho', '2025-09-14 10:55:50.150627+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (23, 'Dwayne Johnson', '2025-09-14 10:55:50.15779+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (24, 'Rachel House', '2025-09-14 10:55:50.164843+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (25, 'Kristen Bell', '2025-09-14 10:55:50.688576+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (26, 'Idina Menzel', '2025-09-14 10:55:50.694892+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (27, 'Jonathan Groff', '2025-09-14 10:55:50.701908+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (28, 'Rolf Saxon', '2025-09-14 11:02:37.692197+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (29, 'Jessica Smith', '2025-09-14 11:02:37.697634+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (30, 'John Simmit', '2025-09-14 11:02:37.703563+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (31, 'Benedict Lim', '2025-09-14 12:52:28.503389+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (32, 'Clinton Loomis', '2025-09-14 12:52:28.514868+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (33, 'Danil Ishutin', '2025-09-14 12:52:28.527633+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (34, 'Clive Owen', '2025-09-14 12:52:29.010729+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (35, 'Naomi Watts', '2025-09-14 12:52:29.017568+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (36, 'Armin Mueller-Stahl', '2025-09-14 12:52:29.024689+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (37, 'Yuri Lowenthal', '2025-09-14 12:52:29.559094+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (38, 'Lara Pulver', '2025-09-14 12:52:29.564943+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (39, 'Troy Baker', '2025-09-14 12:52:29.570609+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (40, 'Sharlto Copley', '2025-09-14 12:55:37.387526+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (41, 'Brie Larson', '2025-09-14 12:55:37.395244+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (42, 'Armie Hammer', '2025-09-14 12:55:37.403224+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (43, 'Denzel Washington', '2025-09-14 12:55:44.043283+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (44, 'Bruce Willis', '2025-09-14 12:55:44.050208+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (45, 'Annette Bening', '2025-09-14 12:55:44.056186+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (46, 'Robin Williams', '2025-09-14 13:01:00.215059+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (47, 'Robert Sean Leonard', '2025-09-14 13:01:00.222311+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (48, 'Ethan Hawke', '2025-09-14 13:01:00.229671+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (49, 'Emilio Estevez', '2025-09-14 13:01:00.579788+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (50, 'Judd Nelson', '2025-09-14 13:01:00.586882+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (51, 'Molly Ringwald', '2025-09-14 13:01:00.593507+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (52, 'Matthew Broderick', '2025-09-14 13:01:00.9862+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (53, 'Alan Ruck', '2025-09-14 13:01:00.993561+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (54, 'Mia Sara', '2025-09-14 13:01:01.000386+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (55, 'Michael Cera', '2025-09-14 13:01:01.323415+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (56, 'Jonah Hill', '2025-09-14 13:01:01.331527+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (57, 'Christopher Mintz-Plasse', '2025-09-14 13:01:01.339123+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (58, 'Jason Biggs', '2025-09-14 13:01:01.704435+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (59, 'Chris Klein', '2025-09-14 13:01:01.713131+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (60, 'Thomas Ian Nicholas', '2025-09-14 13:01:01.72024+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (61, 'Sean Penn', '2025-09-14 13:01:02.073519+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (62, 'Jennifer Jason Leigh', '2025-09-14 13:01:02.082087+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (63, 'Judge Reinhold', '2025-09-14 13:01:02.088979+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (64, 'Anthony Michael Hall', '2025-09-14 13:01:02.424566+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (65, 'Justin Henry', '2025-09-14 13:01:02.431613+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (66, 'Alicia Silverstone', '2025-09-14 13:01:02.739424+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (67, 'Stacey Dash', '2025-09-14 13:01:02.744998+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (68, 'Brittany Murphy', '2025-09-14 13:01:02.750983+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (69, 'Heath Ledger', '2025-09-14 13:01:03.097232+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (70, 'Julia Stiles', '2025-09-14 13:01:03.104226+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (71, 'Joseph Gordon-Levitt', '2025-09-14 13:01:03.111465+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (72, 'Freddie Prinze Jr.', '2025-09-14 13:01:03.667792+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (73, 'Rachael Leigh Cook', '2025-09-14 13:01:03.676705+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (74, 'Matthew Lillard', '2025-09-14 13:01:03.684711+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (75, 'Daniel Brühl', '2025-09-14 13:17:46.373233+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (76, 'Chris Hemsworth', '2025-09-14 13:17:46.381457+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (77, 'Olivia Wilde', '2025-09-14 13:17:46.389078+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (78, 'Matt Damon', '2025-09-14 13:17:46.786901+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (79, 'Christian Bale', '2025-09-14 13:17:46.800375+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (80, 'Jon Bernthal', '2025-09-14 13:17:46.811413+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (81, 'Ayrton Senna', '2025-09-14 13:17:47.511141+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (82, 'Reginaldo Leme', '2025-09-14 13:17:47.516403+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (83, 'John Bisignano', '2025-09-14 13:17:47.522186+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (84, 'James Garner', '2025-09-14 13:17:48.017676+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (85, 'Eva Marie Saint', '2025-09-14 13:17:48.022997+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (86, 'Yves Montand', '2025-09-14 13:17:48.029279+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (87, 'Tom Cruise', '2025-09-14 13:17:48.524418+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (88, 'Nicole Kidman', '2025-09-14 13:17:48.532851+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (89, 'Robert Duvall', '2025-09-14 13:17:48.540636+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (90, 'Steve McQueen', '2025-09-14 13:17:48.875351+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (91, 'Siegfried Rauch', '2025-09-14 13:17:48.882427+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (92, 'Elga Andersen', '2025-09-14 13:17:48.88967+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (93, 'Emile Hirsch', '2025-09-14 13:17:49.380505+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (94, 'Matthew Fox', '2025-09-14 13:17:49.385779+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (95, 'Christina Ricci', '2025-09-14 13:17:49.392074+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (96, 'Sylvester Stallone', '2025-09-14 13:17:49.704302+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (97, 'Kip Pardue', '2025-09-14 13:17:49.71104+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (98, 'Til Schweiger', '2025-09-14 13:17:49.718961+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (99, 'Kevin Costner', '2025-09-14 13:17:50.258217+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (100, 'Milo Ventimiglia', '2025-09-14 13:17:50.264897+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (101, 'Jackie Minns', '2025-09-14 13:17:50.272612+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (102, 'Mike Myers', '2025-09-14 13:18:51.560424+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (103, 'Eddie Murphy', '2025-09-14 13:18:51.568008+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (104, 'Cameron Diaz', '2025-09-14 13:18:51.57499+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (105, 'John Lithgow', '2025-09-14 13:18:53.940034+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (106, 'Brian d''Arcy James', '2025-09-14 13:18:54.312005+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (107, 'Sutton Foster', '2025-09-14 13:18:54.322776+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (108, 'Christopher Sieber', '2025-09-14 13:18:54.334275+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (109, 'Christopher Knights', '2025-09-14 13:18:54.635101+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (110, 'Guillaume Aretos', '2025-09-14 13:18:54.638575+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (111, 'Grant Duffrin', '2025-09-14 13:18:55.064583+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (112, 'Eric Nitshcke', '2025-09-14 13:18:55.071502+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (113, 'Harry Antonucci', '2025-09-14 13:18:55.077174+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (114, 'Michael Gough', '2025-09-14 13:18:55.512217+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (115, 'Dean Edwards', '2025-09-14 13:18:55.520999+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (116, 'Holly Fields', '2025-09-14 13:18:55.529958+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (117, 'Actor One', '2025-10-04 10:04:30.642788+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (118, 'Amy Adams', '2025-10-04 10:15:04.4646+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (119, 'Susan Sarandon', '2025-10-04 10:15:04.476975+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (120, 'James Marsden', '2025-10-04 10:15:04.485429+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (121, 'Hugh Jackman', '2025-10-04 10:15:04.959813+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (122, 'Michelle Williams', '2025-10-04 10:15:04.970174+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (123, 'Zac Efron', '2025-10-04 10:15:04.982918+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (124, 'Jim Henson', '2025-10-04 10:15:05.350622+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (125, 'Frank Oz', '2025-10-04 10:15:05.357294+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (126, 'Jerry Nelson', '2025-10-04 10:15:05.362917+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (127, 'Julie Andrews', '2025-10-04 10:15:05.776497+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (128, 'Dick Van Dyke', '2025-10-04 10:15:05.785882+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (129, 'David Tomlinson', '2025-10-04 10:15:05.793056+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (130, 'Jeremy Irons', '2025-10-04 10:15:06.307198+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (131, 'James Earl Jones', '2025-10-04 10:15:06.315496+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (132, 'Cary Elwes', '2025-10-04 10:15:06.805979+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (133, 'Mandy Patinkin', '2025-10-04 10:15:06.816024+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (134, 'Robin Wright', '2025-10-04 10:15:06.824989+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (135, 'Danny DeVito', '2025-10-04 10:53:20.685079+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (136, 'Rhea Perlman', '2025-10-04 10:53:20.692061+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (137, 'Mara Wilson', '2025-10-04 10:53:20.698537+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (138, 'Noah Hathaway', '2025-10-04 10:53:20.805008+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (139, 'Barret Oliver', '2025-10-04 10:53:20.811785+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (140, 'Tami Stronach', '2025-10-04 10:53:20.818612+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (141, 'Judy Garland', '2025-10-04 10:55:11.777436+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (142, 'Frank Morgan', '2025-10-04 10:55:11.784366+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (143, 'Ray Bolger', '2025-10-04 10:55:11.791007+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (144, 'Matthew McConaughey', '2025-10-04 10:55:12.215749+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (145, 'Reese Witherspoon', '2025-10-04 10:55:12.221125+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (146, 'Seth MacFarlane', '2025-10-04 10:55:12.229296+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (147, 'Christopher Plummer', '2025-10-04 10:55:12.639995+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (148, 'Eleanor Parker', '2025-10-04 10:55:12.651897+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (149, 'Billy Crystal', '2025-10-19 09:11:03.643826+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (150, 'John Goodman', '2025-10-19 09:11:03.657932+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (151, 'Mary Gibbs', '2025-10-19 09:11:03.668532+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (152, 'Craig T. Nelson', '2025-10-19 09:11:04.121243+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (153, 'Samuel L. Jackson', '2025-10-19 09:11:04.129805+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (154, 'Holly Hunter', '2025-10-19 09:11:04.139376+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (155, 'Tom Hanks', '2025-10-19 09:11:04.53772+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (156, 'Tim Allen', '2025-10-19 09:11:04.560855+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (157, 'Don Rickles', '2025-10-19 09:11:04.571824+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (158, 'Albert Brooks', '2025-10-19 09:11:05.018283+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (159, 'Ellen DeGeneres', '2025-10-19 09:11:05.020987+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (160, 'Alexander Gould', '2025-10-19 09:11:05.027189+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (161, 'Chris Rock', '2025-10-19 09:11:05.441967+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (162, 'Ben Stiller', '2025-10-19 09:11:05.450708+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (163, 'David Schwimmer', '2025-10-19 09:11:05.459283+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (164, 'Denis Leary', '2025-10-19 09:11:05.96335+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (165, 'John Leguizamo', '2025-10-19 09:11:05.969477+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (166, 'Ray Romano', '2025-10-19 09:11:05.975069+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (167, 'Jay Baruchel', '2025-10-19 09:11:06.371768+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (168, 'Gerard Butler', '2025-10-19 09:11:06.380643+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (169, 'Steve Carell', '2025-10-19 09:11:06.783205+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (170, 'Jason Segel', '2025-10-19 09:11:06.790862+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (171, 'Russell Brand', '2025-10-19 09:11:06.801231+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (172, 'Anika Noni Rose', '2025-10-19 09:11:07.281835+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (173, 'Keith David', '2025-10-19 09:11:07.294175+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (174, 'Oprah Winfrey', '2025-10-19 09:11:07.303307+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (175, 'Scott Weinger', '2025-10-19 11:04:48.345917+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (176, 'Linda Larkin', '2025-10-19 11:04:48.349473+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (177, 'Jodi Benson', '2025-10-19 11:04:48.649089+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (178, 'Samuel E. Wright', '2025-10-19 11:04:48.658685+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (179, 'Rene Auberjonois', '2025-10-19 11:04:48.667282+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (180, 'Stephanie Beatriz', '2025-10-19 11:04:49.080594+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (181, 'María Cecilia Botero', '2025-10-19 11:04:49.088373+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (182, 'Mandy Moore', '2025-10-19 11:04:49.477848+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (183, 'Zachary Levi', '2025-10-19 11:04:49.486231+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (184, 'Donna Murphy', '2025-10-19 11:04:49.494333+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (185, 'Paige O''Hara', '2025-10-19 11:04:49.891145+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (186, 'Robby Benson', '2025-10-19 11:04:49.898125+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (187, 'Jesse Corti', '2025-10-19 11:04:49.904581+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (188, 'Michael Herbig', '2025-10-19 11:05:31.877215+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (189, 'Christoph Maria Herbst', '2025-10-19 11:05:31.884095+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (190, 'Heike Makatsch', '2025-10-19 11:05:31.890311+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (191, 'Rick Kavanian', '2025-10-19 11:05:32.298002+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (192, 'Daichi Harashima', '2025-10-19 11:16:13.815536+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (193, 'Li Feng', '2025-10-19 11:16:13.818864+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (194, 'Zhong Yu', '2025-10-19 11:16:13.822298+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (195, 'Liqing Zu', '2025-10-19 11:16:14.143032+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (196, 'Lin Zhang', '2025-10-19 11:16:14.150083+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (197, 'Quansheng Gao', '2025-10-19 11:16:14.156118+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (198, 'Bichang Zhou', '2025-10-19 11:16:14.439209+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (199, 'Ah-Niu', '2025-10-19 11:16:14.445418+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (200, 'Eddy Ou', '2025-10-19 11:16:14.454569+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (201, 'Ding Li', '2025-10-19 11:16:14.795647+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (202, 'Xiong Xiao', '2025-10-19 11:16:14.80509+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (203, 'Man-Yee Ching', '2025-10-19 11:16:15.139719+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (204, 'Yuting Deng', '2025-10-19 11:16:15.143043+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (205, 'Ying Liang', '2025-10-19 11:16:15.148291+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (206, 'Kuan-Chun Chi', '2025-10-19 11:16:15.444939+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (207, 'Tao-Liang Tan', '2025-10-19 11:16:15.447963+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (208, 'Hsiao Wen Tang', '2025-10-19 11:16:15.450976+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (209, 'Steven Zhang', '2025-10-19 11:16:15.769931+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (210, 'Zihan Chen', '2025-10-19 11:16:15.776778+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (211, 'Jiajia Deng', '2025-10-19 11:16:15.783078+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (212, 'Szu Shih', '2025-10-19 11:16:16.062855+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (213, 'Lieh Lo', '2025-10-19 11:16:16.069846+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (214, 'Pei-Shan Chang', '2025-10-19 11:16:16.077011+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (215, 'Shuzhen Zhao', '2025-10-19 11:16:38.610581+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (216, 'Awkwafina', '2025-10-19 11:16:38.618011+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (217, 'X Mayo', '2025-10-19 11:16:38.624634+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (218, 'Constance Wu', '2025-10-19 11:16:39.020875+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (219, 'Henry Golding', '2025-10-19 11:16:39.027216+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (220, 'Michelle Yeoh', '2025-10-19 11:16:39.033734+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (221, 'Stephanie Hsu', '2025-10-19 11:16:39.3905+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (222, 'Jamie Lee Curtis', '2025-10-19 11:16:39.398181+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (223, 'Steven Yeun', '2025-10-19 11:16:39.739269+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (224, 'Han Ye-ri', '2025-10-19 11:16:39.745892+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (225, 'Alan Kim', '2025-10-19 11:16:39.752967+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (226, 'Song Kang-ho', '2025-10-19 11:16:40.145808+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (227, 'Lee Sun-kyun', '2025-10-19 11:16:40.152094+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (228, 'Cho Yeo-jeong', '2025-10-19 11:16:40.158757+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (229, 'Simu Liu', '2025-10-19 11:16:40.556558+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (230, 'Tony Leung Chiu-wai', '2025-10-19 11:16:40.565544+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (231, 'Tamlyn Tomita', '2025-10-19 11:16:40.906201+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (232, 'Rosalind Chao', '2025-10-19 11:16:40.913381+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (233, 'Kieu Chinh', '2025-10-19 11:16:40.919232+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (234, 'Maggie Cheung', '2025-10-19 11:16:41.304613+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (235, 'Ping-Lam Siu', '2025-10-19 11:16:41.31268+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (236, 'Jet Li', '2025-10-19 11:16:41.680485+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (237, 'Chow Yun-Fat', '2025-10-19 11:16:42.091897+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (238, 'Ziyi Zhang', '2025-10-19 11:16:42.100922+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (239, 'Bill Murray', '2025-10-19 11:19:33.443876+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (240, 'Scarlett Johansson', '2025-10-19 11:19:33.450133+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (241, 'Giovanni Ribisi', '2025-10-19 11:19:33.456301+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (242, 'Tim Robbins', '2025-10-19 11:20:04.941913+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (243, 'Kelly McGillis', '2025-10-19 11:20:04.948398+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (244, 'Jennifer Connelly', '2025-10-19 11:20:05.338183+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (245, 'Miles Teller', '2025-10-19 11:20:05.345042+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (246, 'Robert Downey Jr.', '2025-10-19 11:20:05.671323+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (247, 'Gwyneth Paltrow', '2025-10-19 11:20:05.677954+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (248, 'Terrence Howard', '2025-10-19 11:20:05.684772+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (249, 'Chris Evans', '2025-10-19 11:20:06.176989+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (250, 'Idris Elba', '2025-10-19 11:20:06.590983+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (251, 'Charlie Hunnam', '2025-10-19 11:20:06.597896+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (252, 'Rinko Kikuchi', '2025-10-19 11:20:06.60507+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (253, 'Will Smith', '2025-10-19 11:20:06.950034+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (254, 'Bill Pullman', '2025-10-19 11:20:06.956562+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (255, 'Jeff Goldblum', '2025-10-19 11:20:06.963105+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (256, 'Ralph D. Apel', '2025-10-19 11:20:07.296692+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (257, 'Stevi Apel', '2025-10-19 11:20:07.304164+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (258, 'Cal Bonavita', '2025-10-19 11:20:07.310945+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (259, 'Sam Worthington', '2025-10-19 11:20:07.710107+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (260, 'Zoe Saldaña', '2025-10-19 11:20:07.716807+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (261, 'Sigourney Weaver', '2025-10-19 11:20:07.723606+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (262, 'Tom Hardy', '2025-10-19 11:20:08.106866+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (263, 'Charlize Theron', '2025-10-19 11:20:08.113546+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (264, 'Nicholas Hoult', '2025-10-19 11:20:08.120724+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (265, 'Keanu Reeves', '2025-10-19 11:23:58.72532+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (266, 'Laurence Fishburne', '2025-10-19 11:23:58.732773+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (267, 'Carrie-Anne Moss', '2025-10-19 11:23:58.739848+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (268, 'Leonardo DiCaprio', '2025-10-19 11:23:59.087918+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (269, 'Elliot Page', '2025-10-19 11:23:59.095144+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (270, 'Anne Hathaway', '2025-10-19 11:23:59.404686+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (271, 'Jessica Chastain', '2025-10-19 11:23:59.411425+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (272, 'Harrison Ford', '2025-10-19 11:23:59.760482+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (273, 'Ryan Gosling', '2025-10-19 11:23:59.767112+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (274, 'Ana de Armas', '2025-10-19 11:23:59.773662+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (275, 'Aaron Eckhart', '2025-10-19 11:24:00.148831+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (276, 'Antonio Banderas', '2025-10-19 12:03:19.171831+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (277, 'Salma Hayek', '2025-10-19 12:03:19.177986+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (278, 'Zach Galifianakis', '2025-10-19 12:03:19.184121+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (279, 'Harvey Guillén', '2025-10-19 12:03:19.563468+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (280, 'Ralph Fiennes', '2025-10-19 12:03:32.173638+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (281, 'F. Murray Abraham', '2025-10-19 12:03:32.181084+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (282, 'Mathieu Amalric', '2025-10-19 12:03:32.187032+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (283, 'Will Ferrell', '2025-10-19 12:03:32.566766+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (284, 'Christina Applegate', '2025-10-19 12:03:32.57349+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (285, 'Sacha Baron Cohen', '2025-10-19 12:03:32.985036+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (286, 'Ken Davitian', '2025-10-19 12:03:32.992048+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (287, 'Luenell', '2025-10-19 12:03:32.998134+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (288, 'Jack Black', '2025-10-19 12:03:33.401645+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (289, 'Christine Taylor', '2025-10-19 12:03:33.754301+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (290, 'Bradley Cooper', '2025-10-19 12:03:34.116128+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (291, 'Justin Bartha', '2025-10-19 12:03:34.124138+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (292, 'Kristen Wiig', '2025-10-19 12:03:34.520421+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (293, 'Maya Rudolph', '2025-10-19 12:03:34.527177+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (294, 'Rose Byrne', '2025-10-19 12:03:34.534027+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (295, 'John C. Reilly', '2025-10-19 12:03:34.941636+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (296, 'Mary Steenburgen', '2025-10-19 12:03:34.950131+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (297, 'Seth Rogen', '2025-10-19 12:03:35.344217+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (298, 'James Franco', '2025-10-19 12:03:35.35063+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (299, 'Gary Cole', '2025-10-19 12:03:35.356031+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (300, 'Katherine Heigl', '2025-10-19 12:03:36.082858+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (301, 'Paul Rudd', '2025-10-19 12:03:36.08947+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (302, 'Vince Vaughn', '2025-10-19 12:03:36.475609+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (303, 'Rachel McAdams', '2025-10-19 12:03:36.483582+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (304, 'Jon Heder', '2025-10-19 12:03:37.234412+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (305, 'Efren Ramirez', '2025-10-19 12:03:37.241064+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (306, 'Jon Gries', '2025-10-19 12:03:37.247565+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (307, 'Mark Wahlberg', '2025-10-19 12:03:37.596694+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (308, 'Derek Jeter', '2025-10-19 12:03:37.603407+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (309, 'Elizabeth Hurley', '2025-10-19 12:03:38.326836+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (310, 'Michael York', '2025-10-19 12:03:38.338031+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (311, 'Jim Carrey', '2025-10-19 12:03:38.713798+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (312, 'Jeff Daniels', '2025-10-19 12:03:38.71998+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (313, 'Lauren Holly', '2025-10-19 12:03:38.726417+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (314, 'Robert De Niro', '2025-10-19 12:03:39.132229+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (315, 'Teri Polo', '2025-10-19 12:03:39.138826+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (316, 'Edward Asner', '2025-10-24 18:54:19.749918+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (317, 'Jordan Nagai', '2025-10-24 18:54:19.756338+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (318, 'John Ratzenberger', '2025-10-24 18:54:19.765556+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (319, 'Pepijn Hikspoors', '2025-10-24 18:54:20.191905+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (320, 'Joe Porter', '2025-10-24 18:54:20.199095+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (321, 'John Travolta', '2025-10-24 19:36:41.704446+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (322, 'Uma Thurman', '2025-10-24 19:36:41.729467+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (323, 'Morgan Freeman', '2025-10-24 19:36:55.390386+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (324, 'Bob Gunton', '2025-10-24 19:36:55.396918+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (325, 'Gary Sinise', '2025-10-24 19:36:55.803362+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (326, 'Ray Liotta', '2025-10-24 19:36:56.320601+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (327, 'Joe Pesci', '2025-10-24 19:36:56.330106+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (328, 'Marlon Brando', '2025-10-24 19:36:56.721037+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (329, 'Al Pacino', '2025-10-24 19:36:56.727111+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (330, 'James Caan', '2025-10-24 19:36:56.73455+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (331, 'Humphrey Bogart', '2025-10-24 19:36:57.113605+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (332, 'Ingrid Bergman', '2025-10-24 19:36:57.123462+00');
INSERT INTO public.movie_actor (id, full_name, created_at) VALUES (333, 'Paul Henreid', '2025-10-24 19:36:57.13062+00');


--
-- Data for Name: movie_country; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_country (id, name) VALUES (1, 'United States');
INSERT INTO public.movie_country (id, name) VALUES (2, 'Japan');
INSERT INTO public.movie_country (id, name) VALUES (3, 'India');
INSERT INTO public.movie_country (id, name) VALUES (4, 'United Kingdom');
INSERT INTO public.movie_country (id, name) VALUES (5, 'Australia');
INSERT INTO public.movie_country (id, name) VALUES (6, 'Mexico');
INSERT INTO public.movie_country (id, name) VALUES (7, 'Germany');
INSERT INTO public.movie_country (id, name) VALUES (8, 'France');
INSERT INTO public.movie_country (id, name) VALUES (9, 'Turkey');
INSERT INTO public.movie_country (id, name) VALUES (10, 'Canada');
INSERT INTO public.movie_country (id, name) VALUES (11, 'USA');
INSERT INTO public.movie_country (id, name) VALUES (12, 'Algeria');
INSERT INTO public.movie_country (id, name) VALUES (13, 'New Zealand');
INSERT INTO public.movie_country (id, name) VALUES (14, 'China');
INSERT INTO public.movie_country (id, name) VALUES (15, 'West Germany');
INSERT INTO public.movie_country (id, name) VALUES (16, 'Brazil');
INSERT INTO public.movie_country (id, name) VALUES (17, 'Taiwan');
INSERT INTO public.movie_country (id, name) VALUES (18, 'Hong Kong');
INSERT INTO public.movie_country (id, name) VALUES (19, 'South Korea');
INSERT INTO public.movie_country (id, name) VALUES (20, 'Spain');
INSERT INTO public.movie_country (id, name) VALUES (21, 'Netherlands');


--
-- Data for Name: movie_director; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_director (id, full_name, created_at) VALUES (1, 'John Lasseter', '2025-09-14 10:49:55.520869+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (2, 'Joe Ranft', '2025-09-14 10:49:55.528255+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (3, 'Bradford Lewis', '2025-09-14 10:49:56.080055+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (4, 'Brian Fee', '2025-09-14 10:49:56.718213+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (5, 'Klay Hall', '2025-09-14 10:49:57.65036+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (6, 'Bobs Gannaway', '2025-09-14 10:49:58.161634+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (7, 'Peter Sohn', '2025-09-14 10:55:48.689541+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (8, 'Mark Andrews', '2025-09-14 10:55:49.289662+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (9, 'Brenda Chapman', '2025-09-14 10:55:49.296918+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (10, 'Steve Purcell', '2025-09-14 10:55:49.30423+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (11, 'Lee Unkrich', '2025-09-14 10:55:49.692638+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (12, 'Adrian Molina', '2025-09-14 10:55:49.698902+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (13, 'Ron Clements', '2025-09-14 10:55:50.182308+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (14, 'John Musker', '2025-09-14 10:55:50.189171+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (15, 'Don Hall', '2025-09-14 10:55:50.19566+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (16, 'Chris Buck', '2025-09-14 10:55:50.716892+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (17, 'Jennifer Lee', '2025-09-14 10:55:50.723136+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (18, 'N/A', '2025-09-14 11:02:37.722619+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (19, 'Valve', '2025-09-14 12:52:28.570156+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (20, 'Tom Tykwer', '2025-09-14 12:52:29.039853+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (21, 'Ben Wheatley', '2025-09-14 12:55:37.424935+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (22, 'Edward Zwick', '2025-09-14 12:55:44.071463+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (23, 'Peter Weir', '2025-09-14 13:01:00.24708+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (24, 'John Hughes', '2025-09-14 13:01:00.608196+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (25, 'Greg Mottola', '2025-09-14 13:01:01.360925+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (26, 'Paul Weitz', '2025-09-14 13:01:01.739312+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (27, 'Amy Heckerling', '2025-09-14 13:01:02.105423+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (28, 'Gil Junger', '2025-09-14 13:01:03.128141+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (29, 'Robert Iscove', '2025-09-14 13:01:03.702325+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (30, 'Ron Howard', '2025-09-14 13:17:46.409463+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (31, 'James Mangold', '2025-09-14 13:17:46.833225+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (32, 'Asif Kapadia', '2025-09-14 13:17:47.536597+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (33, 'John Frankenheimer', '2025-09-14 13:17:48.04868+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (34, 'Tony Scott', '2025-09-14 13:17:48.55802+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (35, 'Lee H. Katzin', '2025-09-14 13:17:48.90806+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (36, 'John Sturges', '2025-09-14 13:17:48.917033+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (37, 'Lana Wachowski', '2025-09-14 13:17:49.401022+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (38, 'Lilly Wachowski', '2025-09-14 13:17:49.403744+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (39, 'Renny Harlin', '2025-09-14 13:17:49.736968+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (40, 'Simon Curtis', '2025-09-14 13:17:50.290825+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (41, 'Andrew Adamson', '2025-09-14 13:18:51.593105+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (42, 'Vicky Jenson', '2025-09-14 13:18:51.600592+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (43, 'Kelly Asbury', '2025-09-14 13:18:52.078819+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (44, 'Conrad Vernon', '2025-09-14 13:18:52.093374+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (45, 'Chris Miller', '2025-09-14 13:18:52.484869+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (46, 'Raman Hui', '2025-09-14 13:18:52.491522+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (47, 'Mike Mitchell', '2025-09-14 13:18:53.065824+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (48, 'Gary Trousdale', '2025-09-14 13:18:53.460339+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (49, 'Simon J. Smith', '2025-09-14 13:18:53.957087+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (50, 'Michael John Warren', '2025-09-14 13:18:54.353217+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (51, 'Grant Duffrin', '2025-09-14 13:18:55.091765+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (52, 'Sean Bishop', '2025-09-14 13:18:55.551628+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (53, 'Director One', '2025-10-04 10:04:30.647458+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (54, 'Kevin Lima', '2025-10-04 10:15:04.504376+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (55, 'Michael Gracey', '2025-10-04 10:15:05.007903+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (56, 'James Frawley', '2025-10-04 10:15:05.37659+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (57, 'Robert Stevenson', '2025-10-04 10:15:05.808443+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (58, 'Roger Allers', '2025-10-04 10:15:06.331817+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (59, 'Rob Minkoff', '2025-10-04 10:15:06.338566+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (60, 'Rob Reiner', '2025-10-04 10:15:06.847817+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (61, 'Danny DeVito', '2025-10-04 10:53:20.713853+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (62, 'Wolfgang Petersen', '2025-10-04 10:53:20.833585+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (63, 'Victor Fleming', '2025-10-04 10:55:11.807536+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (64, 'George Cukor', '2025-10-04 10:55:11.813376+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (65, 'Norman Taurog', '2025-10-04 10:55:11.820881+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (66, 'Garth Jennings', '2025-10-04 10:55:12.247705+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (67, 'Christophe Lourdelet', '2025-10-04 10:55:12.254394+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (68, 'Robert Wise', '2025-10-04 10:55:12.676387+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (69, 'Pete Docter', '2025-10-19 09:11:03.702702+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (70, 'David Silverman', '2025-10-19 09:11:03.711209+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (71, 'Brad Bird', '2025-10-19 09:11:04.155733+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (72, 'Andrew Stanton', '2025-10-19 09:11:05.049285+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (73, 'Eric Darnell', '2025-10-19 09:11:05.478055+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (74, 'Tom McGrath', '2025-10-19 09:11:05.490129+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (75, 'Chris Wedge', '2025-10-19 09:11:05.997048+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (76, 'Carlos Saldanha', '2025-10-19 09:11:06.004998+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (77, 'Dean DeBlois', '2025-10-19 09:11:06.403555+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (78, 'Chris Sanders', '2025-10-19 09:11:06.412443+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (79, 'Pierre Coffin', '2025-10-19 09:11:06.820901+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (80, 'Chris Renaud', '2025-10-19 09:11:06.83081+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (81, 'Jared Bush', '2025-10-19 11:04:49.108906+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (82, 'Byron Howard', '2025-10-19 11:04:49.1161+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (83, 'Charise Castro Smith', '2025-10-19 11:04:49.122438+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (84, 'Nathan Greno', '2025-10-19 11:04:49.513443+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (85, 'Kirk Wise', '2025-10-19 11:04:49.921052+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (86, 'Sebastian Niemann', '2025-10-19 11:05:31.905657+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (87, 'Zhong Yu', '2025-10-19 11:16:13.829173+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (88, 'William Kan', '2025-10-19 11:16:14.473043+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (89, 'Junzheng Wang', '2025-10-19 11:16:14.825614+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (90, 'Wu Ma', '2025-10-19 11:16:15.456745+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (91, 'Chiang Shen', '2025-10-19 11:16:16.092114+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (92, 'Lulu Wang', '2025-10-19 11:16:38.64014+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (93, 'Jon M. Chu', '2025-10-19 11:16:39.048128+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (94, 'Daniel Kwan', '2025-10-19 11:16:39.416904+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (95, 'Daniel Scheinert', '2025-10-19 11:16:39.42701+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (96, 'Lee Isaac Chung', '2025-10-19 11:16:39.767864+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (97, 'Bong Joon Ho', '2025-10-19 11:16:40.17245+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (98, 'Destin Daniel Cretton', '2025-10-19 11:16:40.582996+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (99, 'Wayne Wang', '2025-10-19 11:16:40.933208+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (100, 'Wong Kar-Wai', '2025-10-19 11:16:41.32817+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (101, 'Yimou Zhang', '2025-10-19 11:16:41.708672+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (102, 'Ang Lee', '2025-10-19 11:16:42.115681+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (103, 'Sofia Coppola', '2025-10-19 11:19:33.471116+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (104, 'Joseph Kosinski', '2025-10-19 11:20:05.359944+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (105, 'Jon Favreau', '2025-10-19 11:20:05.699552+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (106, 'Joss Whedon', '2025-10-19 11:20:06.193948+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (107, 'Guillermo del Toro', '2025-10-19 11:20:06.620964+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (108, 'Roland Emmerich', '2025-10-19 11:20:06.97864+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (109, 'Patrick Cotnoir', '2025-10-19 11:20:07.326197+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (110, 'James Cameron', '2025-10-19 11:20:07.73746+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (111, 'George Miller', '2025-10-19 11:20:08.135184+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (112, 'Christopher Nolan', '2025-10-19 11:23:59.109026+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (113, 'Denis Villeneuve', '2025-10-19 11:23:59.793074+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (114, 'Joel Crawford', '2025-10-19 12:03:19.596176+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (115, 'Januel Mercado', '2025-10-19 12:03:19.608783+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (116, 'Wes Anderson', '2025-10-19 12:03:32.201763+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (117, 'Adam McKay', '2025-10-19 12:03:32.590763+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (118, 'Larry Charles', '2025-10-19 12:03:33.013627+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (119, 'Ben Stiller', '2025-10-19 12:03:33.417852+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (120, 'Todd Phillips', '2025-10-19 12:03:34.14002+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (121, 'Paul Feig', '2025-10-19 12:03:34.549157+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (122, 'David Gordon Green', '2025-10-19 12:03:35.369652+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (123, 'Evan Goldberg', '2025-10-19 12:03:35.766895+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (124, 'Seth Rogen', '2025-10-19 12:03:35.775116+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (125, 'Judd Apatow', '2025-10-19 12:03:36.107627+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (126, 'David Dobkin', '2025-10-19 12:03:36.500262+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (127, 'Rawson Marshall Thurber', '2025-10-19 12:03:36.89239+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (128, 'Jared Hess', '2025-10-19 12:03:37.261379+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (129, 'Jay Roach', '2025-10-19 12:03:38.356502+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (130, 'Peter Farrelly', '2025-10-19 12:03:38.742135+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (131, 'Bobby Farrelly', '2025-10-19 12:03:38.748357+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (132, 'Bob Peterson', '2025-10-24 18:54:19.783709+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (133, 'Brian Bear', '2025-10-24 18:54:20.214128+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (134, 'Cas van de Pol', '2025-10-24 18:54:20.220861+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (135, 'Quentin Tarantino', '2025-10-24 19:36:41.780385+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (136, 'Frank Darabont', '2025-10-24 19:36:55.412911+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (137, 'Robert Zemeckis', '2025-10-24 19:36:55.818698+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (138, 'Martin Scorsese', '2025-10-24 19:36:56.346126+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (139, 'Francis Ford Coppola', '2025-10-24 19:36:56.752799+00');
INSERT INTO public.movie_director (id, full_name, created_at) VALUES (140, 'Michael Curtiz', '2025-10-24 19:36:57.147437+00');


--
-- Data for Name: movie_genre; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_genre (id, name, created_at) VALUES (1, 'Animation', '2025-09-14 10:49:55.430999+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (2, 'Adventure', '2025-09-14 10:49:55.446739+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (3, 'Comedy', '2025-09-14 10:49:55.460882+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (4, 'Action', '2025-09-14 10:55:48.633213+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (5, 'Drama', '2025-09-14 10:55:49.643514+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (6, 'Family', '2025-09-14 11:02:37.659724+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (7, 'Fantasy', '2025-09-14 11:02:37.666987+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (8, 'Musical', '2025-09-14 11:02:37.674216+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (9, 'Documentary', '2025-09-14 12:52:28.477606+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (10, 'Crime', '2025-09-14 12:52:28.992638+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (11, 'Thriller', '2025-09-14 12:55:44.028112+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (12, 'Romance', '2025-09-14 13:01:02.407146+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (13, 'Biography', '2025-09-14 13:17:46.337694+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (14, 'Sport', '2025-09-14 13:17:46.349335+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (15, 'Short', '2025-09-14 13:18:53.4256+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (16, 'Music', '2025-09-14 13:18:54.625013+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (17, 'Sci-Fi', '2025-10-19 11:20:05.654648+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (18, 'Mystery', '2025-10-19 11:23:59.745601+00');
INSERT INTO public.movie_genre (id, name, created_at) VALUES (19, 'War', '2025-10-19 12:03:33.385365+00');


--
-- Data for Name: movie_language; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_language (id, name) VALUES (1, 'English');
INSERT INTO public.movie_language (id, name) VALUES (2, 'Italian');
INSERT INTO public.movie_language (id, name) VALUES (3, 'Japanese');
INSERT INTO public.movie_language (id, name) VALUES (4, 'Yiddish');
INSERT INTO public.movie_language (id, name) VALUES (5, 'French');
INSERT INTO public.movie_language (id, name) VALUES (6, 'Russian');
INSERT INTO public.movie_language (id, name) VALUES (7, 'Spanish');
INSERT INTO public.movie_language (id, name) VALUES (8, 'German');
INSERT INTO public.movie_language (id, name) VALUES (9, 'Mandarin');
INSERT INTO public.movie_language (id, name) VALUES (10, 'Icelandic');
INSERT INTO public.movie_language (id, name) VALUES (11, 'North American Indian');
INSERT INTO public.movie_language (id, name) VALUES (12, 'Polish');
INSERT INTO public.movie_language (id, name) VALUES (13, 'Chinese');
INSERT INTO public.movie_language (id, name) VALUES (14, 'Czech');
INSERT INTO public.movie_language (id, name) VALUES (15, 'Bulgarian');
INSERT INTO public.movie_language (id, name) VALUES (16, 'Danish');
INSERT INTO public.movie_language (id, name) VALUES (17, 'Arabic');
INSERT INTO public.movie_language (id, name) VALUES (18, 'Latin');
INSERT INTO public.movie_language (id, name) VALUES (19, 'Portuguese');
INSERT INTO public.movie_language (id, name) VALUES (20, 'Swahili');
INSERT INTO public.movie_language (id, name) VALUES (21, 'Xhosa');
INSERT INTO public.movie_language (id, name) VALUES (22, 'Zulu');
INSERT INTO public.movie_language (id, name) VALUES (23, 'American Sign');
INSERT INTO public.movie_language (id, name) VALUES (24, 'Cantonese');
INSERT INTO public.movie_language (id, name) VALUES (25, 'Hokkien');
INSERT INTO public.movie_language (id, name) VALUES (26, 'Malay');
INSERT INTO public.movie_language (id, name) VALUES (27, 'Korean');
INSERT INTO public.movie_language (id, name) VALUES (28, 'Shanghainese');
INSERT INTO public.movie_language (id, name) VALUES (29, 'Persian');
INSERT INTO public.movie_language (id, name) VALUES (30, 'Urdu');
INSERT INTO public.movie_language (id, name) VALUES (31, 'Kurdish');
INSERT INTO public.movie_language (id, name) VALUES (32, 'Hindi');
INSERT INTO public.movie_language (id, name) VALUES (33, 'Hungarian');
INSERT INTO public.movie_language (id, name) VALUES (34, 'Romanian');
INSERT INTO public.movie_language (id, name) VALUES (35, 'Hebrew');
INSERT INTO public.movie_language (id, name) VALUES (36, 'Armenian');
INSERT INTO public.movie_language (id, name) VALUES (37, 'Thai');
INSERT INTO public.movie_language (id, name) VALUES (38, 'Ukrainian');
INSERT INTO public.movie_language (id, name) VALUES (39, 'Swedish');


--
-- Data for Name: movie_movie; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (11, 'Teletubbies', 'tt0142055', '1997–2001', 'series', 'https://m.media-amazon.com/images/M/MV5BZWM5ZjNkOWItNmU0Zi00YzdiLTg0MTAtMzkxMTZmZGI4NmQ2XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 11:02:37.65078+00', '2025-09-14 11:02:37.650819+00', 'Four creatures with televisions in their stomachs have fun in their magical world.', 'Won 2 BAFTA 2 wins & 7 nominations total', '3.9', '9,337', 'N/A', '1998-04-06', 'N/A', '2');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (14, 'Dota: Dragon''s Blood', 'tt14069590', '2021–2022', 'series', 'https://m.media-amazon.com/images/M/MV5BMGQ2YjcwZDUtNDQ4YS00MThjLWJlMjYtZjkxMTYxNmU4MGY0XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 12:52:29.538456+00', '2025-09-14 12:52:29.538473+00', 'After encounters with a dragon and a princess on her own mission, a Dragon Knight becomes embroiled in events larger than he could have ever imagined.', '1 win total', '7.7', '23,222', 'N/A', '2021-03-25', '1 min', '3');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (13, 'The International', 'tt0963178', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjE3Njg5NzY2OV5BMl5BanBnXkFtZTcwMDMxNjEwMg@@._V1_SX300.jpg', '2025-09-14 12:52:28.982641+00', '2025-09-14 12:52:28.982659+00', 'An Interpol agent attempts to expose a high-profile financial institution''s role in an international arms dealing ring.', '1 win & 1 nomination total', '6.5', '103,019', '52', '2009-02-13', '118 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (1, 'Cars', 'tt0317219', '2006', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTg5NzY0MzA2MV5BMl5BanBnXkFtZTYwNDc3NTc2._V1_SX300.jpg', '2025-09-14 10:49:55.418962+00', '2025-09-14 10:49:55.418969+00', 'On the way to the biggest race of his life, a hotshot rookie race car gets stranded in a rundown town and learns that winning isn''t everything in life.', 'Nominated for 2 Oscars. 28 wins & 34 nominations total', '7.3', '513,360', '73', '2006-06-09', '116 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (2, 'Cars 2', 'tt1216475', '2011', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTUzNTc3MTU3M15BMl5BanBnXkFtZTcwMzIxNTc3NA@@._V1_SX300.jpg', '2025-09-14 10:49:56.028355+00', '2025-09-14 10:49:56.028374+00', 'Star race car Lightning McQueen and his pal Mater head overseas to compete in the World Grand Prix race. But the road to the championship becomes rocky as Mater gets caught up in an intriguing adventure of his own: international e...', '1 win & 19 nominations total', '6.2', '240,276', '57', '2011-06-24', '106 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (3, 'Cars 3', 'tt3606752', '2017', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTc0NzU2OTYyN15BMl5BanBnXkFtZTgwMTkwOTg2MTI@._V1_SX300.jpg', '2025-09-14 10:49:56.669847+00', '2025-09-14 10:49:56.669865+00', 'Lightning McQueen sets out to prove to a new generation of racers that he''s still the best race car in the world.', '3 wins & 24 nominations total', '6.7', '141,123', '59', '2017-06-16', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (4, 'Planes', 'tt1691917', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjAwODc5NzYzOF5BMl5BanBnXkFtZTcwNTk4MjEzOQ@@._V1_SX300.jpg', '2025-09-14 10:49:57.604287+00', '2025-09-14 10:49:57.604311+00', 'A cropdusting plane with a fear of heights lives his dream of competing in a famous around-the-world aerial race.', '5 nominations total', '5.7', '50,739', '39', '2013-08-09', '91 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (5, 'Planes: Fire & Rescue', 'tt2980706', '2014', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTcwMjY4NDM4OF5BMl5BanBnXkFtZTgwMDIxNDU2MTE@._V1_SX300.jpg', '2025-09-14 10:49:58.113324+00', '2025-09-14 10:49:58.113346+00', 'When Dusty learns that his engine is damaged and he may never race again, he joins a forest fire and rescue unit to be trained as a firefighter, or else his air strip will be shut down.', 'Nominated for 1 BAFTA Award6 nominations total', '5.9', '21,135', '48', '2014-07-18', '83 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (6, 'The Good Dinosaur', 'tt1979388', '2015', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTc5MTg2NjQ4MV5BMl5BanBnXkFtZTgwNzcxOTY5NjE@._V1_SX300.jpg', '2025-09-14 10:55:48.622983+00', '2025-09-14 10:55:48.623021+00', 'In a world where dinosaurs and humans live side-by-side, an Apatosaurus named Arlo makes an unlikely human friend.', '9 wins & 41 nominations total', '6.7', '135,719', '66', '2015-11-25', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (7, 'Brave', 'tt1217209', '2012', 'movie', 'https://m.media-amazon.com/images/M/MV5BMzgwODk3ODA1NF5BMl5BanBnXkFtZTcwNjU3NjQ0Nw@@._V1_SX300.jpg', '2025-09-14 10:55:49.200818+00', '2025-09-14 10:55:49.200836+00', 'Determined to make her own path in life, Princess Merida defies a custom that brings chaos to her kingdom. Granted one wish, Merida must rely on her bravery and her archery skills to undo a beastly curse.', 'Won 1 Oscar. 20 wins & 48 nominations total', '7.1', '467,171', '69', '2012-06-22', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (8, 'Coco', 'tt2380307', '2017', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDIyM2E2NTAtMzlhNy00ZGUxLWI1NjgtZDY5MzhiMDc5NGU3XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 10:55:49.631781+00', '2025-09-14 10:55:49.631801+00', 'Aspiring musician Miguel, confronted with his family''s ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.', 'Won 2 Oscars. 112 wins & 42 nominations total', '8.4', '664,277', '81', '2017-11-22', '105 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (9, 'Moana', 'tt3521164', '2016', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_SX300.jpg', '2025-09-14 10:55:50.127911+00', '2025-09-14 10:55:50.127928+00', 'In ancient Polynesia, when a terrible curse incurred by the demigod Maui reaches Moana''s island, she answers the Ocean''s call to seek out Maui to set things right.', 'Nominated for 2 Oscars. 22 wins & 90 nominations total', '7.6', '423,719', '81', '2016-11-23', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (10, 'Frozen', 'tt2294629', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SX300.jpg', '2025-09-14 10:55:50.667569+00', '2025-09-14 10:55:50.667586+00', 'Fearless optimist Anna teams up with rugged mountain man Kristoff and his loyal reindeer Sven in an epic journey to find Anna''s sister Elsa, whose icy powers have trapped the kingdom of Arendelle in eternal winter.', 'Won 2 Oscars. 83 wins & 60 nominations total', '7.4', '695,677', '75', '2013-11-27', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (12, 'Free to Play', 'tt3203290', '2014', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTYxMjk0OTUwMF5BMl5BanBnXkFtZTgwNTY0ODIzMDE@._V1_SX300.jpg', '2025-09-14 12:52:28.466204+00', '2025-09-14 12:52:28.466226+00', 'Follow three professional video game players as they overcome personal adversity, family pressures, and the realities of life to compete in a $1,000,000 tournament that could change their lives forever.', 'N/A', '7.6', '13,627', 'N/A', '2021-04-14', '75 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (15, 'Free Fire', 'tt4158096', '2016', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTk5MzJhNjItZTRlOC00YWRlLTgyYmUtZmZhZjA0NmFmNjE2XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 12:55:37.352486+00', '2025-09-14 12:55:37.352531+00', 'Set in Boston in 1978, a meeting in a deserted warehouse between two gangs turns into a shoot-out and a game of survival.', '3 wins & 9 nominations total', '6.3', '52,597', '63', '2017-04-21', '91 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (16, 'The Siege', 'tt0133952', '1998', 'movie', 'https://m.media-amazon.com/images/M/MV5BNjY4YmMyMzYtM2M4YS00YzQ2LTg5OWUtZjc4YmQ4NGE0ZGViXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 12:55:44.019208+00', '2025-09-14 12:55:44.019226+00', 'The secret U.S. abduction of a suspected terrorist leads to a wave of terrorist attacks in New York City, which leads to the declaration of martial-law.', '2 wins & 4 nominations total', '6.4', '80,779', '53', '1998-11-06', '116 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (17, 'Dead Poets Society', 'tt0097165', '1989', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDYwNGVlY2ItMWYxMS00YjZiLWE5MTAtYWM5NWQ2ZWJjY2Q3XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:00.189254+00', '2025-09-14 13:01:00.189294+00', 'Maverick teacher John Keating returns in 1959 to the prestigious New England boys'' boarding school where he was once a star student, using poetry to embolden his pupils to new heights of self-expression.', 'Won 1 Oscar. 20 wins & 19 nominations total', '8.1', '603,509', '79', '1989-06-09', '128 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (18, 'The Breakfast Club', 'tt0088847', '1985', 'movie', 'https://m.media-amazon.com/images/M/MV5BZTZiMGU1MWMtNjk0Yi00ZjNjLTljMDEtMDhkNGE2OWY3YzZiXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:00.556623+00', '2025-09-14 13:01:00.556641+00', 'Five high school students meet in Saturday detention and discover how they have a great deal more in common than they thought.', '4 wins total', '7.8', '462,255', '66', '1985-02-15', '97 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (19, 'Ferris Bueller''s Day Off', 'tt0091042', '1986', 'movie', 'https://m.media-amazon.com/images/M/MV5BZWYwMjUxNjMtMzE0MC00NDM3LWIxMmQtYmEyNWVjNjdlZGZjXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:00.9689+00', '2025-09-14 13:01:00.96892+00', 'A brash, cocky high school senior, tired of skipping school to spend a boring day at home, is determined to enjoy an epic day roaring around his favorite Chicago sites, enlisting his best friend and girlfriend to join him on the a...', '3 wins & 1 nomination total', '7.8', '405,647', '61', '1986-06-11', '103 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (20, 'Superbad', 'tt0829482', '2007', 'movie', 'https://m.media-amazon.com/images/M/MV5BNjk0MzdlZGEtNTRkOC00ZDRiLWJkYjAtMzUzYTRiNzk1YTViXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:01.301031+00', '2025-09-14 13:01:01.301051+00', 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.', '11 wins & 24 nominations total', '7.6', '672,775', '76', '2007-08-17', '113 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (21, 'American Pie', 'tt0163651', '1999', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTg3ODY5ODI1NF5BMl5BanBnXkFtZTgwMTkxNTYxMTE@._V1_SX300.jpg', '2025-09-14 13:01:01.686189+00', '2025-09-14 13:01:01.68621+00', 'Four teenage boys enter a pact to lose their virginity by prom night.', '9 wins & 14 nominations total', '7.0', '457,741', '58', '1999-07-09', '95 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (22, 'Fast Times at Ridgemont High', 'tt0083929', '1982', 'movie', 'https://m.media-amazon.com/images/M/MV5BMWM4NTc3N2YtMjk2Ny00MTRmLWE4YzItNTVhMTRlODVkNmE5XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:02.052656+00', '2025-09-14 13:01:02.052674+00', 'A group of SoCal high school students would rather ignore their studies and instead indulge in their teenage distractions.', '1 win & 1 nomination total', '7.1', '121,961', '61', '1982-08-13', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (23, 'Sixteen Candles', 'tt0088128', '1984', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTgzNTkxMTkxMl5BMl5BanBnXkFtZTgwMjE3NjkzMTE@._V1_SX300.jpg', '2025-09-14 13:01:02.397099+00', '2025-09-14 13:01:02.397117+00', 'A girl''s "sweet" sixteenth birthday is anything but special: her family forgets about it, and she suffers from every embarrassment possible.', '2 wins & 1 nomination total', '7.0', '130,929', '61', '1984-05-04', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (24, 'Clueless', 'tt0112697', '1995', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTgwYjQ1NDktOTcwNi00MWZhLTliYWQtZDg5NjZhY2U5ZTNlXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:02.719884+00', '2025-09-14 13:01:02.719899+00', 'Shallow, rich and socially successful Cher is at the top of her Beverly Hills high school''s pecking scale. Seeing herself as a matchmaker, Cher first coaxes two teachers into dating each other.', '6 wins & 12 nominations total', '6.9', '268,796', '73', '1995-07-19', '97 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (25, '10 Things I Hate About You', 'tt0147800', '1999', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTQwYmRhNGQtODI2Mi00ZTRlLTk0Y2QtY2NkNjE1MGNhNTgwXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:03.073863+00', '2025-09-14 13:01:03.073882+00', 'A high-school boy, Cameron, cannot date Bianca until her anti-social older sister, Kat, has a boyfriend. So, Cameron pays a mysterious boy, Patrick, to charm Kat.', '2 wins & 13 nominations total', '7.4', '425,583', '70', '1999-03-31', '97 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (26, 'She''s All That', 'tt0160862', '1999', 'movie', 'https://m.media-amazon.com/images/M/MV5BOGUyZTFiOTEtN2Y1Ny00NDFhLWEyMTMtZmE0MzNjODE3MzAzXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:01:03.644613+00', '2025-09-14 13:01:03.644634+00', 'When Zack''s famous girlfriend, Taylor, cheats on him with another boy and parts ways with him, he makes a bet with his friends to turn a socially inept Laney into their high school''s next prom queen.', '8 wins & 6 nominations total', '5.9', '106,106', '51', '1999-01-29', '95 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (27, 'Rush', 'tt1979320', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTZhOGQxM2ItNGQyYy00YzE5LWI5MjMtNmMzNGQzNDE1OTUzXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:46.326098+00', '2025-09-14 13:17:46.326155+00', 'James Hunt and Niki Lauda, two extremely skilled Formula One racers, have an intense rivalry with each other. However, it is their enmity that pushes them to their limits.', 'Won 1 BAFTA Award6 wins & 66 nominations total', '8.1', '544,257', '74', '2013-09-27', '123 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (28, 'Ford v Ferrari', 'tt1950186', '2019', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTBjNTEyNjYtYjdkNi00YzE5LTljYzUtZjVlYmYwZmJmZWYxXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:46.751072+00', '2025-09-14 13:17:46.751093+00', 'American car designer Carroll Shelby and driver Ken Miles battle corporate interference and the laws of physics to build a revolutionary race car for Ford in order to defeat Ferrari at the 24 Hours of Le Mans in 1966.', 'Won 2 Oscars. 26 wins & 86 nominations total', '8.1', '539,559', '81', '2019-11-15', '152 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (29, 'Senna', 'tt1424432', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTc5MTUzOTAxMl5BMl5BanBnXkFtZTcwODQzMjg3NA@@._V1_SX300.jpg', '2025-09-14 13:17:47.490982+00', '2025-09-14 13:17:47.491003+00', 'A documentary on Brazilian Formula One racing driver Ayrton Senna, who won the F1 world championship three times before his death at age 34.', 'Won 2 BAFTA 20 wins & 19 nominations total', '8.5', '80,387', '79', '2011-05-25', '106 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (30, 'Grand Prix', 'tt0060472', '1966', 'movie', 'https://m.media-amazon.com/images/M/MV5BNTA2NzQzYWQtY2FlZi00ODFiLTgyOTctY2RmNjE4YTcwMjg5XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:47.998945+00', '2025-09-14 13:17:47.998964+00', 'American Grand Prix driver Pete Aron is fired by his Jordan-BRM racing team after a crash at Monaco that injures his British teammate, Scott Stoddard.', 'Won 3 Oscars. 3 wins & 4 nominations total', '7.2', '11,191', '72', '1966-12-21', '176 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (31, 'Days of Thunder', 'tt0099371', '1990', 'movie', 'https://m.media-amazon.com/images/M/MV5BNjM0NjgwYjAtMjQ3Mi00NDY1LTgwMDktZGJkOGRkMTBkMDA2XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:48.500499+00', '2025-09-14 13:17:48.500519+00', 'A young hot-shot stock car driver gets his chance to compete at the top level.', 'Nominated for 1 Oscar. 1 win & 2 nominations total', '6.1', '101,796', '60', '1990-06-27', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (32, 'Le Mans', 'tt0067334', '1971', 'movie', 'https://m.media-amazon.com/images/M/MV5BYmNmNjViZDYtZDhmOC00M2E5LWI2NmYtNDg2YWFhNzMxOWFiXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:48.853217+00', '2025-09-14 13:17:48.853235+00', 'Two car racing champions, an American and a German, face off on the world''s hardest endurance course: Le Mans in France.', '1 nomination total', '6.7', '12,811', '52', '1971-06-23', '106 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (33, 'Speed Racer', 'tt0811080', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BNzE3MWIxNzktYzQyMy00NGQ5LThmZTktM2ZkZjc0NWEzZTg5XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:49.365085+00', '2025-09-14 13:17:49.365102+00', 'Young driver, Speed Racer, aspires to be champion of the racing world with the help of his family and his high-tech Mach 5 automobile.', '1 win & 12 nominations total', '6.1', '81,122', '37', '2008-05-09', '135 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (34, 'Driven', 'tt0132245', '2001', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjA5MDk4NzI0NF5BMl5BanBnXkFtZTYwNjU0Nzc5._V1_SX300.jpg', '2025-09-14 13:17:49.680141+00', '2025-09-14 13:17:49.680208+00', 'A young hot shot driver is in the middle of a championship season and is coming apart at the seams. A former CART champion is called in to give him guidance.', '1 win & 10 nominations total', '4.6', '44,565', '29', '2001-04-27', '116 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (35, 'The Art of Racing in the Rain', 'tt1478839', '2019', 'movie', 'https://m.media-amazon.com/images/M/MV5BNzUyMTJlMzMtYjJkYy00MDA4LTlhMDAtNjM1OGVhYmFjZmJiXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:17:50.23384+00', '2025-09-14 13:17:50.233859+00', 'Through his bond with his owner, aspiring Formula One race car driver Denny, golden retriever Enzo learns that the techniques needed on the racetrack can also be used to successfully navigate the journey of life.', 'N/A', '7.6', '42,068', '43', '2019-08-09', '109 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (36, 'Shrek', 'tt0126029', '2001', 'movie', 'https://m.media-amazon.com/images/M/MV5BN2FkMTRkNTUtYTI0NC00ZjI4LWI5MzUtMDFmOGY0NmU2OGY1XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:18:51.526511+00', '2025-09-14 13:18:51.526588+00', 'A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.', 'Won 1 Oscar. 40 wins & 60 nominations total', '7.9', '779,468', '84', '2001-05-18', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (37, 'Shrek 2', 'tt0298148', '2004', 'movie', 'https://m.media-amazon.com/images/M/MV5BMzNmNjQ1NmUtNzhiZS00YWE2LTg4N2ItZTA2ODdmOTMwOTQ1XkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:18:52.047366+00', '2025-09-14 13:18:52.047375+00', 'Shrek and Fiona travel to the Kingdom of Far Far Away, where Fiona''s parents are King and Queen, to celebrate their marriage. When they arrive, they find they are not as welcome as they thought they would be.', 'Nominated for 2 Oscars. 18 wins & 52 nominations total', '7.4', '538,651', '75', '2004-05-19', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (38, 'Shrek the Third', 'tt0413267', '2007', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTgyMjc3ODk2MV5BMl5BanBnXkFtZTcwMjY0MjEzMw@@._V1_SX300.jpg', '2025-09-14 13:18:52.446095+00', '2025-09-14 13:18:52.446268+00', 'Reluctantly designated as the heir to the land of Far, Far Away, Shrek hatches a plan to install the rebellious Artie as the new king while Princess Fiona tries to fend off a coup d''état by the jilted Prince Charming.', 'Nominated for 1 BAFTA Award5 wins & 17 nominations total', '6.1', '351,701', '58', '2007-05-18', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (39, 'Shrek Forever After', 'tt0892791', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY0OTU1NzkxMl5BMl5BanBnXkFtZTcwMzI2NDUzMw@@._V1_SX300.jpg', '2025-09-14 13:18:53.025992+00', '2025-09-14 13:18:53.02601+00', 'Rumpelstiltskin tricks a mid-life crisis burdened Shrek into allowing himself to be erased from existence and cast in a dark alternate timeline where Rumpelstiltskin rules supreme.', '1 win & 13 nominations total', '6.3', '237,152', '58', '2010-05-21', '93 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (40, 'Shrek the Halls', 'tt0897387', '2007', 'movie', 'https://m.media-amazon.com/images/M/MV5BYzM4NzA2YzctNzBiNi00YjU0LWJkNjAtMzNjOWZkOGVmMDJiXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:18:53.409975+00', '2025-09-14 13:18:53.409994+00', 'This half-hour animated TV special features the Shrek characters putting their own spin on holiday traditions.', '4 nominations total', '6.4', '16,781', 'N/A', '2007-11-28', '21 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (41, 'Shrek 4-D', 'tt0360985', '2003', 'movie', 'https://m.media-amazon.com/images/M/MV5BNDVlOWZkNTEtNTcxZS00NDVhLWFlZWItYWFhNmZmZWNhYzU1XkEyXkFqcGdeQXVyNzMwOTY2NTI@._V1_SX300.jpg', '2025-09-14 13:18:53.903126+00', '2025-09-14 13:18:53.903156+00', 'Join Donkey and Shrek as they rescue Fiona from the evil ghost of Lord Farquaad and embark on a bone-chilling adventure.', 'N/A', '6.3', '4,711', 'N/A', '2009-09-18', '13 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (42, 'Shrek the Musical', 'tt3070936', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BY2Y5YTllMWMtMDc5MC00ZDQ4LTllY2UtNWY4ZThmNTVlOTAyXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:18:54.281638+00', '2025-09-14 13:18:54.281662+00', 'Make room for ogre-sized family fun as the greatest fairy tale never told comes to life in a whole new way in this breathtaking Broadway musical adaptation of the hit movie Shrek!', 'N/A', '6.9', '4,623', 'N/A', '2013-09-17', '130 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (43, 'Shrek in the Swamp Karaoke Dance Party', 'tt0307461', '2001', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTlmZjQzNmYtMjA1Ny00N2JkLWJhM2ItYTU3ODQ4Zjc2MWE1XkEyXkFqcGdeQXVyNzg5OTk2OA@@._V1_SX300.jpg', '2025-09-14 13:18:54.619139+00', '2025-09-14 13:18:54.619147+00', 'Shrek and his friends enjoy themselves with some Karaoke partying.', 'N/A', '7.0', '2,047', 'N/A', '2001-11-02', '3 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (44, 'Shrek Retold', 'tt9334162', '2018', 'movie', 'https://m.media-amazon.com/images/M/MV5BZDY3ZDFjZWYtNDhmNC00OGVjLWIxZDYtNzlmYTAyYjMwNTcyXkEyXkFqcGdeQXVyNTk5NzczMDE@._V1_SX300.jpg', '2025-09-14 13:18:55.04301+00', '2025-09-14 13:18:55.043029+00', 'After his swamp is filled with magical creatures, Shrek agrees to rescue Princess Fiona for a villainous lord in order to get his land back.', 'N/A', '7.4', '1,448', 'N/A', '2018-11-29', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (45, 'Shrek: Thriller Night', 'tt2051999', '2011', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjljZTQ0YWYtNGEwNC00ODJmLTgyOTQtZmIyNjI0YzFmNDgzXkEyXkFqcGc@._V1_SX300.jpg', '2025-09-14 13:18:55.490435+00', '2025-09-14 13:18:55.490452+00', 'Shrek is bored on Halloween, and wants to have something scary. The power of Thriller gives him more than he bargained for.', 'N/A', '6.2', '1,156', 'N/A', '2011-09-13', '6 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (46, 'Query Movie', 'tt-query-1', '', '', '', '2025-10-04 10:04:30.631765+00', '2025-10-04 10:04:30.631783+00', '', '', '', '', '', NULL, '', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (47, 'Query Movie 2', 'tt-query-2', '', '', '', '2025-10-04 10:04:30.636132+00', '2025-10-04 10:04:30.636146+00', '', '', '', '', '', NULL, '', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (49, 'Enchanted', 'tt0461770', '2007', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjE4NDQ2Mjc0OF5BMl5BanBnXkFtZTcwNzQ2NDE1MQ@@._V1_SX300.jpg', '2025-10-04 10:15:04.429854+00', '2025-10-04 10:15:04.429891+00', 'A young maiden in a land called Andalasia, who is prepared to be wed, is sent away to New York City by an evil Queen, where she falls in love with a lawyer.', 'Nominated for 3 Oscars. 12 wins & 51 nominations total', '7.1', '225,315', '75', '2007-11-21', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (50, 'The Greatest Showman', 'tt1485796', '2017', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjI1NDYzNzY2Ml5BMl5BanBnXkFtZTgwODQwODczNTM@._V1_SX300.jpg', '2025-10-04 10:15:04.928024+00', '2025-10-04 10:15:04.928038+00', 'Celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.', 'Nominated for 1 Oscar. 17 wins & 32 nominations total', '7.5', '333,888', '48', '2017-12-20', '105 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (51, 'The Muppet Movie', 'tt0079588', '1979', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTE0ODE3N2ItYjRiOS00ZGU4LThjZTgtOGY5ZTFhMTNlZTNlXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:15:05.328647+00', '2025-10-04 10:15:05.328663+00', 'Kermit and his newfound friends trek across America to find success in Hollywood, but a frog legs merchant is after Kermit.', 'Nominated for 2 Oscars. 4 wins & 11 nominations total', '7.6', '41,401', '74', '1979-06-22', '95 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (52, 'Mary Poppins', 'tt0058331', '1964', 'movie', 'https://m.media-amazon.com/images/M/MV5BNThiNjgzMTYtZjUzMC00YTVlLTg4MDItMmFjMDIwYjg4ZDAwXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:15:05.752787+00', '2025-10-04 10:15:05.752812+00', 'In turn of the century London, a magical nanny employs music and adventure to help two neglected children become closer to their father.', 'Won 5 Oscars. 23 wins & 17 nominations total', '7.8', '194,527', '88', '1965-06-18', '139 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (53, 'The Lion King', 'tt0110357', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BZGRiZDZhZjItM2M3ZC00Y2IyLTk3Y2MtMWY5YjliNDFkZTJlXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:15:06.270819+00', '2025-10-04 10:15:06.270836+00', 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.', 'Won 2 Oscars. 43 wins & 35 nominations total', '8.5', '1,223,797', '88', '1994-06-24', '88 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (54, 'The Princess Bride', 'tt0093779', '1987', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjFiOTEyNGMtN2E4MC00ZjZlLTk3ZDQtNTU1ZGNiZTA1MzJlXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:15:06.771763+00', '2025-10-04 10:15:06.771779+00', 'A bedridden boy''s grandfather reads him the story of a farmboy-turned-pirate who encounters numerous obstacles, enemies and allies in his quest to be reunited with his true love.', 'Nominated for 1 Oscar. 7 wins & 11 nominations total', '8.0', '473,749', '78', '1987-10-09', '98 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (55, 'Matilda', 'tt0117008', '1996', 'movie', 'https://m.media-amazon.com/images/M/MV5BYWE3ZDMzMmEtODgwNi00NzMxLThkYWItMTAzMWUyMzI1NDQ1XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:53:20.659945+00', '2025-10-04 10:53:20.659982+00', 'A girl gifted with a keen intellect and psychic powers uses both to get even with her callous family and free her kindly schoolteacher from the tyrannical grip of a sadistic headmistress.', '3 wins & 7 nominations total', '7.0', '188,260', '72', '1996-08-02', '98 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (56, 'The NeverEnding Story', 'tt0088323', '1984', 'movie', 'https://m.media-amazon.com/images/M/MV5BYzE0Y2E0NGYtYzRmMy00ZDRjLTk1NDItNjZjYTMyMmJjMGYxXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:53:20.783637+00', '2025-10-04 10:53:20.783651+00', 'A troubled boy dives into a wondrous fantasy world through the pages of a mysterious book.', '6 wins & 9 nominations total', '7.3', '166,145', '49', '1984-07-20', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (57, 'The Wizard of Oz', 'tt0032138', '1939', 'movie', 'https://m.media-amazon.com/images/M/MV5BYWRmY2I0MGItYTQ0OC00NWZmLWIwMDktYjJlNDc0MzVhMmViXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:55:11.754728+00', '2025-10-04 10:55:11.754767+00', 'Young Dorothy Gale and her dog Toto are swept away by a tornado from their Kansas farm to the magical Land of Oz and embark on a quest with three new friends to see the Wizard, who can return her to her home and fulfill the others...', 'Won 2 Oscars. 16 wins & 14 nominations total', '8.1', '453,906', '92', '1939-08-25', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (58, 'Sing', 'tt3470600', '2016', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTYzODYzODU2Ml5BMl5BanBnXkFtZTgwNTc1MTA2NzE@._V1_SX300.jpg', '2025-10-04 10:55:12.190757+00', '2025-10-04 10:55:12.190778+00', 'In a city of humanoid animals, a hustling theater impresario''s attempt to save his theater with a singing competition becomes grander than he anticipates even as its finalists find that their lives will never be the same.', '3 wins & 25 nominations total', '7.1', '206,430', '59', '2016-12-21', '108 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (59, 'The Sound of Music', 'tt0059742', '1965', 'movie', 'https://m.media-amazon.com/images/M/MV5BYWJhYmU4MjQtZDJhYi00ZGVjLTlkNTEtNzkzNGVjOWQ3MjcwXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-04 10:55:12.612305+00', '2025-10-04 10:55:12.612321+00', 'A young novice is sent by her convent in 1930s Austria to become a governess to the seven children of a widowed naval officer.', 'Won 5 Oscars. 19 wins & 13 nominations total', '8.1', '281,671', '63', '1965-04-01', '174 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (60, 'Monsters, Inc.', 'tt0198781', '2001', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY1NTI0ODUyOF5BMl5BanBnXkFtZTgwNTEyNjQ0MDE@._V1_SX300.jpg', '2025-10-19 09:11:03.598822+00', '2025-10-19 09:11:03.598876+00', 'In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.', 'Won 1 Oscar. 15 wins & 38 nominations total', '8.1', '1,045,975', '79', '2001-11-02', '92 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (61, 'The Incredibles', 'tt0317705', '2004', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_SX300.jpg', '2025-10-19 09:11:04.095206+00', '2025-10-19 09:11:04.095234+00', 'While trying to lead a quiet suburban life, a family of undercover superheroes are forced into action to save the world.', 'Won 2 Oscars. 69 wins & 56 nominations total', '8.0', '875,373', '90', '2004-11-05', '115 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (62, 'Toy Story', 'tt0114709', '1995', 'movie', 'https://m.media-amazon.com/images/M/MV5BZTA3OWVjOWItNjE1NS00NzZiLWE1MjgtZDZhMWI1ZTlkNzYwXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 09:11:04.50971+00', '2025-10-19 09:11:04.509733+00', 'A cowboy doll is profoundly jealous when a new spaceman action figure supplants him as the top toy in a boy''s bedroom. When circumstances separate them from their owner, the duo have to put aside their differences to return to him.', 'Nominated for 3 Oscars. 29 wins & 24 nominations total', '8.3', '1,141,954', '96', '1995-11-22', '81 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (63, 'Finding Nemo', 'tt0266543', '2003', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTc5NjExNTA5OV5BMl5BanBnXkFtZTYwMTQ0ODY2._V1_SX300.jpg', '2025-10-19 09:11:05.008214+00', '2025-10-19 09:11:05.008222+00', 'After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.', 'Won 1 Oscar. 49 wins & 63 nominations total', '8.2', '1,178,332', '90', '2003-05-30', '100 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (64, 'Madagascar', 'tt0351283', '2005', 'movie', 'https://m.media-amazon.com/images/M/MV5BYjk4OGFmZmYtYWE4NC00MzM4LTkwZTItODdhMjk3NTZjMmI5XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 09:11:05.407351+00', '2025-10-19 09:11:05.407381+00', 'A group of animals who have spent all their life in a New York zoo end up in the jungles of Madagascar, and must adjust to living in the wild.', '4 wins & 32 nominations total', '6.9', '466,710', '57', '2005-05-27', '86 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (65, 'Ice Age', 'tt0268380', '2002', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDBlYzU2OGMtOGJjNi00ZGZjLWIwNjMtYzdiZjkwYWNjZDljXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 09:11:05.935917+00', '2025-10-19 09:11:05.93594+00', 'Manny the mammoth, Sid the loquacious sloth, and Diego the sabre-toothed tiger go on a comical quest to return a human baby back to his father, across a world on the brink of an ice age.', 'Nominated for 1 Oscar. 5 wins & 30 nominations total', '7.5', '550,167', '61', '2002-03-15', '81 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (66, 'How to Train Your Dragon', 'tt0892769', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjA5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1_SX300.jpg', '2025-10-19 09:11:06.348338+00', '2025-10-19 09:11:06.348357+00', 'A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.', 'Nominated for 2 Oscars. 25 wins & 63 nominations total', '8.1', '868,640', '75', '2010-03-26', '98 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (67, 'Despicable Me', 'tt1323594', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY3NjY0MTQ0Nl5BMl5BanBnXkFtZTcwMzQ2MTc0Mw@@._V1_SX300.jpg', '2025-10-19 09:11:06.75857+00', '2025-10-19 09:11:06.758586+00', 'Gru, a criminal mastermind, adopts three orphans as pawns to carry out the biggest heist in history. His life takes an unexpected turn when the little girls see the evildoer as their potential father.', 'Nominated for 1 BAFTA Award3 wins & 41 nominations total', '7.6', '618,896', '72', '2010-07-09', '95 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (68, 'The Princess and the Frog', 'tt0780521', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTE3YTExYTEtOTUxZC00OTM0LWJmYmItMDk5YjczNmIwNzA2XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 09:11:07.244434+00', '2025-10-19 09:11:07.244463+00', 'A waitress desperate to fulfill her dreams as a restaurant owner is set on a journey to turn a frog prince back into a human, but she has to face the same problem after she kisses him.', 'Nominated for 3 Oscars. 10 wins & 42 nominations total', '7.2', '180,621', '73', '2009-12-11', '97 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (69, 'Aladdin', 'tt0103639', '1992', 'movie', 'https://m.media-amazon.com/images/M/MV5BMmQwYWZjZGItYzc0OC00ZDllLTg3NjItOWIyOWYwMDljMjAyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:04:48.335912+00', '2025-10-19 11:04:48.335928+00', 'A kind-hearted street urchin and a power-hungry Grand Vizier vie for a magic lamp that has the power to make their deepest wishes come true.', 'Won 2 Oscars. 35 wins & 22 nominations total', '8.0', '490,592', '86', '1992-11-25', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (70, 'The Little Mermaid', 'tt0097757', '1989', 'movie', 'https://m.media-amazon.com/images/M/MV5BNmQ3ODcyZGMtMjNlOS00YzhlLTg0YzAtZGVjNmQ0OTYyNDg0XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:04:48.638614+00', '2025-10-19 11:04:48.638621+00', 'A mermaid princess makes a Faustian bargain in an attempt to become human and win a prince''s love.', 'Won 2 Oscars. 16 wins & 9 nominations total', '7.6', '303,917', '88', '1989-11-17', '83 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (71, 'Encanto', 'tt2953050', '2021', 'movie', 'https://m.media-amazon.com/images/M/MV5BNGEyNzk2M2MtNjBhZS00MzYwLWI0Y2YtYjc5ZWE2MjM0YWE5XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:04:49.051682+00', '2025-10-19 11:04:49.051702+00', 'An extraordinary family, the Madrigals, live hidden in the mountains of Colombia, in a magical house called an Encanto. The magic of the Encanto has blessed every child in the family with a unique gift - every child except one, Mi...', 'Won 1 Oscar. 58 wins & 86 nominations total', '7.2', '286,569', '75', '2021-11-24', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (72, 'Tangled', 'tt0398286', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTAxNDYxMjg0MjNeQTJeQWpwZ15BbWU3MDcyNTk2OTM@._V1_SX300.jpg', '2025-10-19 11:04:49.452446+00', '2025-10-19 11:04:49.452462+00', 'The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief has stumbled upon her, she is about to discover the world for the first time, and who she really is.', 'Nominated for 1 Oscar. 10 wins & 42 nominations total', '7.7', '530,733', '71', '2010-11-24', '100 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (73, 'Beauty and the Beast', 'tt0101414', '1991', 'movie', 'https://m.media-amazon.com/images/M/MV5BYTY3NDg2YzktYWFjZC00MTExLTlmZDctMGY3MWYzZTlkYTNiXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:04:49.871008+00', '2025-10-19 11:04:49.871026+00', 'A prince cursed to spend his days as a hideous monster sets out to regain his humanity by earning a young woman''s love.', 'Won 2 Oscars. 33 wins & 32 nominations total', '8.0', '498,015', '95', '1991-11-22', '84 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (74, 'Hui Buh: Das Schlossgespenst', 'tt0428646', '2006', 'movie', 'https://m.media-amazon.com/images/M/MV5BOWI3NmQ4YjQtNWMzMS00MTY0LTgyYTAtYjYwNzgxNGIxZmRkXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:05:31.855771+00', '2025-10-19 11:05:31.855788+00', 'Five hundred years ago, Hui Buh cheated in a card game, thus was turned into a ghost by thunder lighting. For all this time, he has lived in the castle alone without anyone to scare. Until when King Julius moves in for his wedding...', 'N/A', '4.8', '3,304', 'N/A', '2006-07-20', '103 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (75, 'Hui Buh und das Hexenschloss', 'tt14176696', '2022', 'movie', 'https://m.media-amazon.com/images/M/MV5BZDU2N2NiMTItMzAzNy00MDdhLWI3MzAtYjdlZjc5Y2IxOWE0XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:05:32.268112+00', '2025-10-19 11:05:32.268134+00', 'The evil witch Erla makes life difficult for Hui Buh and his niece, the little witch Ophelia. After her mother is captured, she seeks Hui Buh''s help with a valuable book of spells.', 'N/A', '5.2', '376', 'N/A', '2022-11-03', '88 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (76, 'Xiong mao hui jia lu', 'tt1247700', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BODE0ODQxM2QtZTI2Yy00NTdjLTljNmItOGFlYmU4NjE2NGExXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:13.799669+00', '2025-10-19 11:16:13.799691+00', 'High in the mountains of the China, a ten-year-old mute orphan boy, Lu, rescues a lost panda cub separated from its mother. As Lu struggles to return the cub to its mother-and protect it from trappers-the two form a unique connect...', '', '6.2', '268', '', NULL, '87 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (77, 'Xi Yang Yang yu Hui Tai Lang', 'tt8677202', '2005–2008', 'series', 'https://m.media-amazon.com/images/M/MV5BYzA4YzdlOTEtNDliOC00NzBhLWFiOTgtZjc2ODdhYTZkYzU5XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:14.121951+00', '2025-10-19 11:16:14.121968+00', 'In the year of 3131 Goat calendar, the goats are living happily and peacefully on Green-Green Grassland until the wolf couple moves to the forest on the opposite side of the shore.', '', '5.9', '123', '', '2005-06-01', '', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (78, 'Xi Yang Yang Yu Hui Tai Lang Zhi Kaixin Chuang Long Nian', 'tt2193271', '2012', 'movie', 'https://m.media-amazon.com/images/M/MV5BM2E1YWFlNzAtZTEzNy00MjJkLWJmZGYtM2M5OGRjN2Q1ZGI1XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:14.418316+00', '2025-10-19 11:16:14.418332+00', 'In the film, Weslie and his crew discover an evil mechanical dragon who defeats Wolffy as he was attempting to capture the goats, but a series of good dragons rescue Weslie and the goats. The good dragons say that evil dragons hav...', '', '5.1', '99', '', '2012-01-12', '85 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (79, 'Tian tang hui xin', 'tt0334505', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTJjYWM2OTktYWIyMi00ZWNmLThiZTYtZjMyMzFhZWY5ODM2XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:14.776443+00', '2025-10-19 11:16:14.77646+00', '', '1 win & 5 nominations', '7.5', '94', '', '1996-04-24', '', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (80, 'Xi Yang Yang Yu Hui Tai Lang Zhi Xi Qi Yang Yang Guo She Nian', 'tt2772570', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BZjVjMWU2MWYtMzliYi00OWRmLWI3YzAtYjIwOGVhMGNjODRiXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:15.128942+00', '2025-10-19 11:16:15.12895+00', '', '', '5.5', '66', '', '2013-01-24', '86 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (81, 'Hu Hui Gan xue zhan xi dan si', 'tt0078260', '1978', 'movie', 'https://m.media-amazon.com/images/M/MV5BZTc3YTEzOTYtNWFiZi00NDg0LTljOGUtMzUwNWZiMmMxNDc4XkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_SX300.jpg', '2025-10-19 11:16:15.435908+00', '2025-10-19 11:16:15.435917+00', 'Shaolin hero Hu Hui-Chien has become the people''s champion and the sworn enemy of the Ching government. So enraged are they that they employ the best fighters from the Wu Tang. A master leg fighter named Kao Chin Chung, whose "Fla...', '', '6.4', '61', '', NULL, '84 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (82, 'Hui Lang Ting', 'tt12483716', '2022–', 'series', 'https://m.media-amazon.com/images/M/MV5BN2JjNTY1MjItNjA2Ny00MGY3LWE1MjctYzA1ZmUwY2I0YmE3XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:15.750016+00', '2025-10-19 11:16:15.750032+00', 'Kairoutei suddenly caught fire in the middle of the night, a man died in the fire, Jiang Yuanxing was severely burned and disfigured; Handsome man Cheng Cheng appeared in Jiang Yuanxing''s life, and the fate of the two seemed to be...', '', '', '58', '', '2022-06-15', '', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (83, 'Long hu hui feng yun', 'tt0445534', '1973', 'movie', 'https://m.media-amazon.com/images/M/MV5BZjQzYzY3NzktMjA2Yi00MWU3LThkMGItY2RlNzNmNzI0N2ZmXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:16.040041+00', '2025-10-19 11:16:16.040058+00', 'Swordswoman Meng Hung must work with Fan Tien-fu, to find then protect the royal seals of the Sung Dynasty. If they should fail, the dynasty will fall.', '', '6.5', '56', '', '1973-12-01', '81 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (84, 'The Farewell', 'tt8637428', '2019', 'movie', 'https://m.media-amazon.com/images/M/MV5BYjdlZDI1OWYtZWU4MC00NDhkLThmOWEtMTZiODFhZThkMjA4XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:38.59002+00', '2025-10-19 11:16:38.590037+00', 'A Chinese family discovers their grandmother has only a short while left to live and decide to keep her in the dark, scheduling a wedding to gather before she dies.', 'Nominated for 1 BAFTA Award37 wins & 194 nominations total', '7.5', '72,726', '89', '2019-08-09', '100 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (85, 'Crazy Rich Asians', 'tt3104988', '2018', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTYxNDMyOTAxN15BMl5BanBnXkFtZTgwMDg1ODYzNTM@._V1_SX300.jpg', '2025-10-19 11:16:38.998437+00', '2025-10-19 11:16:38.998452+00', 'This contemporary romantic comedy based on a global bestseller follows native New Yorker Rachel Chu to Singapore to meet her boyfriend''s family.', '14 wins & 70 nominations total', '6.9', '203,321', '74', '2018-08-15', '120 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (86, 'Everything Everywhere All at Once', 'tt6710474', '2022', 'movie', 'https://m.media-amazon.com/images/M/MV5BOWNmMzAzZmQtNDQ1NC00Nzk5LTkyMmUtNGI2N2NkOWM4MzEyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:39.365969+00', '2025-10-19 11:16:39.365986+00', 'A middle-aged Chinese immigrant is swept up into an insane adventure in which she alone can save existence by exploring other universes and connecting with the lives she could have led.', 'Won 7 Oscars. 397 wins & 379 nominations total', '7.8', '593,726', '81', '2022-04-08', '139 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (87, 'Minari', 'tt10633456', '2020', 'movie', 'https://m.media-amazon.com/images/M/MV5BNWVmNDE3YzMtZWQ3Ny00YjhkLWEzN2QtZjNhYWNlMGI2N2NkXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:39.72374+00', '2025-10-19 11:16:39.723756+00', 'A Korean American family moves to an Arkansas farm in search of its own American dream. Amidst the challenges of new life in the strange and rugged Ozarks, they discover the undeniable resilience of family and what really makes a ...', 'Won 1 Oscar. 120 wins & 241 nominations total', '7.4', '105,340', '89', '2021-02-12', '115 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (88, 'Parasite', 'tt6751668', '2019', 'movie', 'https://m.media-amazon.com/images/M/MV5BYjk1Y2U4MjQtY2ZiNS00OWQyLWI3MmYtZWUwNmRjYWRiNWNhXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:40.126774+00', '2025-10-19 11:16:40.126792+00', 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.', 'Won 4 Oscars. 309 wins & 260 nominations total', '8.5', '1,100,523', '97', '2019-11-08', '132 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (89, 'Shang-Chi and the Legend of the Ten Rings', 'tt9376612', '2021', 'movie', 'https://m.media-amazon.com/images/M/MV5BZmY5MDcyNzAtYzg3MC00MGNlLTg3OGItNmRjYThkZGVlNzAyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:40.534546+00', '2025-10-19 11:16:40.534563+00', 'Shang-Chi, the master of weaponry-based Kung Fu, is forced to confront his past after being drawn into the Ten Rings organization.', 'Nominated for 1 Oscar. 19 wins & 67 nominations total', '7.3', '475,117', '71', '2021-09-03', '132 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (90, 'The Joy Luck Club', 'tt0107282', '1993', 'movie', 'https://m.media-amazon.com/images/M/MV5BNGE2YWVjZDYtOGI2Ni00NjUwLWI5ZjgtODA3ZTI5M2NlMmZmXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:40.888986+00', '2025-10-19 11:16:40.889003+00', 'Four Chinese women along with their mothers delve into their past and try to find answers. Slowly, this search helps them to understand the complex relationship they share with each other.', 'Nominated for 1 BAFTA Award4 wins & 5 nominations total', '7.7', '19,256', '84', '1993-10-29', '139 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (91, 'In the Mood for Love', 'tt0118694', '2000', 'movie', 'https://m.media-amazon.com/images/M/MV5BN2Q4NjllMDgtOTk2Zi00YzM1LWJmOTMtNmRiZDgyZGJmMjQzXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:41.286075+00', '2025-10-19 11:16:41.286091+00', 'Two neighbors form a strong bond after both suspect extramarital activities of their spouses. However, they agree to keep their bond platonic so as not to commit similar wrongs.', 'Nominated for 1 BAFTA Award45 wins & 50 nominations total', '8.1', '181,324', '87', '2001-03-09', '98 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (92, 'Hero', 'tt0299977', '2002', 'movie', 'https://m.media-amazon.com/images/M/MV5BYTlkZWVjYzQtZmI1My00MGM2LTlmZjEtNjU1M2Y1MTRkNmZjXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:41.657118+00', '2025-10-19 11:16:41.657134+00', 'A defense officer, Nameless, was summoned by the King of Qin regarding his success of terminating three warriors.', 'Nominated for 1 Oscar. 46 wins & 48 nominations total', '7.9', '192,049', '85', '2004-08-27', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (93, 'Crouching Tiger, Hidden Dragon', 'tt0190332', '2000', 'movie', 'https://m.media-amazon.com/images/M/MV5BMzRmMTU2OWEtZjI0Ni00MGRhLThjOTItZTJiNmM4MDk0ZWU2XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:16:42.070237+00', '2025-10-19 11:16:42.070262+00', 'A young Chinese warrior steals a sword from a famed swordsman and then escapes into a world of romantic adventure with a mysterious man in the frontier of the nation.', 'Won 4 Oscars. 101 wins & 132 nominations total', '7.9', '290,075', '94', '2001-01-12', '120 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (94, 'Lost in Translation', 'tt0335266', '2003', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTUxMzk0NDg1MV5BMl5BanBnXkFtZTgwNDg0NjkxMDI@._V1_SX300.jpg', '2025-10-19 11:19:33.4246+00', '2025-10-19 11:19:33.424616+00', 'A fading movie star falls for a lonely young woman in Tokyo.', 'Won 1 Oscar. 97 wins & 133 nominations total', '7.7', '517,809', '91', '2003-10-03', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (95, 'Top Gun', 'tt0092099', '1986', 'movie', 'https://m.media-amazon.com/images/M/MV5BZmVjNzQ3MjYtYTZiNC00Y2YzLWExZTEtMTM2ZDllNDI0MzgyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:04.921933+00', '2025-10-19 11:20:04.92195+00', 'The Top Gun Naval Fighter Weapons School is where the best of the best train to refine their elite flying skills. When hotshot fighter pilot Maverick is sent to the school, his reckless attitude and cocky demeanor put him at odds ...', 'Won 1 Oscar. 11 wins & 9 nominations total', '7.0', '538,178', '50', '1986-05-16', '110 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (96, 'Top Gun: Maverick', 'tt1745960', '2022', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDBkZDNjMWEtOTdmMi00NmExLTg5MmMtNTFlYTJlNWY5YTdmXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:05.317803+00', '2025-10-19 11:20:05.31782+00', 'The story involves Maverick confronting his past while training a group of younger Top Gun graduates, including the son of his deceased best friend, for a dangerous mission.', 'Won 1 Oscar. 111 wins & 235 nominations total', '8.2', '807,023', '78', '2022-05-27', '130 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (97, 'Iron Man', 'tt0371746', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg', '2025-10-19 11:20:05.643299+00', '2025-10-19 11:20:05.643315+00', 'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.', 'Nominated for 2 Oscars. 24 wins & 73 nominations total', '7.9', '1,194,561', '79', '2008-05-02', '126 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (98, 'The Avengers', 'tt0848228', '2012', 'movie', 'https://m.media-amazon.com/images/M/MV5BNGE0YTVjNzUtNzJjOS00NGNlLTgxMzctZTY4YTE1Y2Y1ZTU4XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:06.154992+00', '2025-10-19 11:20:06.15501+00', 'Earth''s mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.', 'Nominated for 1 Oscar. 39 wins & 81 nominations total', '8.0', '1,528,141', '69', '2012-05-04', '143 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (99, 'Pacific Rim', 'tt1663662', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZTcwOTU1OTU0OQ@@._V1_SX300.jpg', '2025-10-19 11:20:06.565198+00', '2025-10-19 11:20:06.565219+00', 'As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from the apocalypse.', 'Nominated for 1 BAFTA Award7 wins & 48 nominations total', '6.9', '549,323', '65', '2013-07-12', '131 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (100, 'Independence Day', 'tt0116629', '1996', 'movie', 'https://m.media-amazon.com/images/M/MV5BOGMwN2UwZjEtYjFjMi00ZDA1LWJlYTQtMjA1MTYxMzIyNTdiXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:06.928687+00', '2025-10-19 11:20:06.928703+00', 'The aliens are coming and their goal is to invade and destroy Earth. Fighting superior technology, mankind''s best weapon is the will to survive.', 'Won 1 Oscar. 35 wins & 35 nominations total', '7.0', '635,621', '59', '1996-07-03', '145 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (101, 'Maclunkey Treasure Island: A Live Staged Reading of Star Wars - A New Hope', 'tt36328088', '2025', 'movie', 'https://m.media-amazon.com/images/M/MV5BY2YwYmUwNjQtMzRmYy00OTJhLTkyYTgtYzg0MzQ1Yjk3NTNiXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:07.278962+00', '2025-10-19 11:20:07.278978+00', 'A live staged reading of the original screenplay to 1977''s Star Wars, with a radical cast including some of the galaxy''s hottest stars.', '', '', '24', '', '2025-03-15', '123 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (102, 'Avatar', 'tt0499549', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDEzMmQwZjctZWU2My00MWNlLWE0NjItMDJlYTRlNGJiZjcyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:07.6903+00', '2025-10-19 11:20:07.690317+00', 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', 'Won 3 Oscars. 91 wins & 131 nominations total', '7.9', '1,448,400', '83', '2009-12-18', '162 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (103, 'Mad Max: Fury Road', 'tt1392190', '2015', 'movie', 'https://m.media-amazon.com/images/M/MV5BZDRkODJhOTgtOTc1OC00NTgzLTk4NjItNDgxZDY4YjlmNDY2XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:20:08.08323+00', '2025-10-19 11:20:08.083247+00', 'In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshipper and a drifter named Max.', 'Won 6 Oscars. 245 wins & 234 nominations total', '8.1', '1,183,848', '90', '2015-05-15', '120 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (104, 'The Matrix', 'tt0133093', '1999', 'movie', 'https://m.media-amazon.com/images/M/MV5BN2NmN2VhMTQtMDNiOS00NDlhLTliMjgtODE2ZTY0ODQyNDRhXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:23:58.703287+00', '2025-10-19 11:23:58.703305+00', 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.', 'Won 4 Oscars. 42 wins & 52 nominations total', '8.7', '2,187,692', '73', '1999-03-31', '136 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (105, 'Inception', 'tt1375666', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg', '2025-10-19 11:23:59.065873+00', '2025-10-19 11:23:59.065894+00', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.', 'Won 4 Oscars. 159 wins & 220 nominations total', '8.8', '2,731,250', '74', '2010-07-16', '148 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (106, 'Interstellar', 'tt0816692', '2014', 'movie', 'https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 11:23:59.381488+00', '2025-10-19 11:23:59.381504+00', 'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 'Won 1 Oscar. 44 wins & 148 nominations total', '8.7', '2,409,911', '74', '2014-11-07', '169 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (107, 'Blade Runner 2049', 'tt1856101', '2017', 'movie', 'https://m.media-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_SX300.jpg', '2025-10-19 11:23:59.734312+00', '2025-10-19 11:23:59.734329+00', 'Young Blade Runner K''s discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who''s been missing for thirty years.', 'Won 2 Oscars. 100 wins & 164 nominations total', '8.0', '729,843', '81', '2017-10-06', '164 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (108, 'The Dark Knight', 'tt0468569', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg', '2025-10-19 11:24:00.124459+00', '2025-10-19 11:24:00.124476+00', 'When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.', 'Won 2 Oscars. 163 wins & 165 nominations total', '9.1', '3,074,817', '85', '2008-07-18', '152 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (109, 'Puss in Boots', 'tt0448694', '2011', 'movie', 'https://m.media-amazon.com/images/M/MV5BOTQwMGU5YTEtYmQzMy00MTM0LWFhNzAtOGY2Yzc1MzBkYTYyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:19.150481+00', '2025-10-19 12:03:19.150518+00', 'An outlaw cat, his childhood egg-friend, and a seductive thief kitty set out in search for the eggs of the fabled Golden Goose to clear his name, restore his lost honor, and regain the trust of his mother and town.', 'Nominated for 1 Oscar. 9 wins & 43 nominations total', '6.6', '204,347', '65', '2011-11-15', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (110, 'Puss in Boots: The Last Wish', 'tt3915174', '2022', 'movie', 'https://m.media-amazon.com/images/M/MV5BMzg0MWUzMjctYjVlOS00NzVjLWIwZDMtNzg1YzNkYzdjNTMwXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:19.511202+00', '2025-10-19 12:03:19.511229+00', 'When Puss in Boots discovers that his passion for adventure has taken its toll and he has burned through eight of his nine lives, he launches an epic journey to restore them by finding the mythical Last Wish.', 'Nominated for 1 Oscar. 8 wins & 57 nominations total', '7.8', '212,498', '73', '2022-12-21', '102 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (111, 'The Grand Budapest Hotel', 'tt2278388', '2014', 'movie', 'https://m.media-amazon.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_SX300.jpg', '2025-10-19 12:03:32.152553+00', '2025-10-19 12:03:32.152569+00', 'A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel''s glorious years under an exceptional concierge.', 'Won 4 Oscars. 135 wins & 227 nominations total', '8.1', '938,889', '88', '2014-03-28', '99 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (112, 'Anchorman: The Legend of Ron Burgundy', 'tt0357413', '2004', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_SX300.jpg', '2025-10-19 12:03:32.549408+00', '2025-10-19 12:03:32.549424+00', 'In the 1970s, an anchorman''s stint as San Diego''s top-rated newsreader is challenged when an ambitious newswoman becomes his co-anchor.', '1 win & 13 nominations total', '7.1', '394,337', '63', '2004-07-09', '94 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (113, 'Borat', 'tt0443453', '2006', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTk0MTQ3NDQ4Ml5BMl5BanBnXkFtZTcwOTQ3OTQzMw@@._V1_SX300.jpg', '2025-10-19 12:03:32.967174+00', '2025-10-19 12:03:32.967191+00', 'Kazakh TV talking head Borat is dispatched to the United States to report on the greatest country in the world.', 'Nominated for 1 Oscar. 20 wins & 34 nominations total', '7.4', '466,232', '89', '2006-11-03', '84 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (114, 'Tropic Thunder', 'tt0942385', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_SX300.jpg', '2025-10-19 12:03:33.373974+00', '2025-10-19 12:03:33.37399+00', 'Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying.', 'Nominated for 1 Oscar. 10 wins & 47 nominations total', '7.1', '476,779', '71', '2008-08-13', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (115, 'Zoolander', 'tt0196229', '2001', 'movie', 'https://m.media-amazon.com/images/M/MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEwOTMxMDE@._V1_SX300.jpg', '2025-10-19 12:03:33.728666+00', '2025-10-19 12:03:33.728683+00', 'At the end of his career, a clueless fashion model is brainwashed to kill the Prime Minister of Malaysia.', '1 win & 11 nominations total', '6.5', '308,631', '61', '2001-09-28', '90 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (116, 'The Hangover', 'tt1119646', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BNDI2MzBhNzgtOWYyOS00NDM2LWE0OGYtOGQ0M2FjMTI2NTllXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:34.094849+00', '2025-10-19 12:03:34.094866+00', 'Three buddies wake up from a bachelor party in Las Vegas with no memory of the previous night and the bachelor missing. They must make their way around the city in order to find their friend in time for his wedding.', 'Nominated for 1 BAFTA Award13 wins & 25 nominations total', '7.7', '903,625', '73', '2009-06-05', '100 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (117, 'Bridesmaids', 'tt1478338', '2011', 'movie', 'https://m.media-amazon.com/images/M/MV5BMjAyOTMyMzUxNl5BMl5BanBnXkFtZTcwODI4MzE0NA@@._V1_SX300.jpg', '2025-10-19 12:03:34.503157+00', '2025-10-19 12:03:34.503173+00', 'Competition between the maid of honor and a bridesmaid, over who is the bride''s best friend, threatens to upend the life of an out-of-work pastry chef.', 'Nominated for 2 Oscars. 25 wins & 72 nominations total', '6.8', '320,223', '75', '2011-05-13', '125 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (118, 'Step Brothers', 'tt0838283', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BYWNiOGZkOTgtNGMzMC00MDg5LTliM2UtN2VjMDI3N2ViOWE5XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:34.91932+00', '2025-10-19 12:03:34.919337+00', 'Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry.', '3 wins & 2 nominations total', '6.9', '333,253', '51', '2008-07-25', '98 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (119, 'Pineapple Express', 'tt0910936', '2008', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_SX300.jpg', '2025-10-19 12:03:35.323051+00', '2025-10-19 12:03:35.323067+00', 'A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witnesses his dealer''s boss murder a competitor while trying to serve papers on him.', '2 wins & 15 nominations total', '6.9', '367,336', '64', '2008-08-06', '111 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (120, 'This Is the End', 'tt1245492', '2013', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTQxODE3NjM1Ml5BMl5BanBnXkFtZTcwMzkzNjc4OA@@._V1_SX300.jpg', '2025-10-19 12:03:35.730145+00', '2025-10-19 12:03:35.730162+00', 'Six Los Angeles celebrities are stuck in James Franco''s house after a series of devastating events just destroyed the city. Inside, the group not only have to face the apocalypse, but themselves.', '10 wins & 23 nominations total', '6.6', '448,256', '67', '2013-06-12', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (121, 'Knocked Up', 'tt0478311', '2007', 'movie', 'https://m.media-amazon.com/images/M/MV5BYmIyMDA5YzgtZmNhMC00YWNlLTgwYjItOTc0ZGNjNTcwNzAxXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:36.059537+00', '2025-10-19 12:03:36.059552+00', 'For fun-loving party animal Ben Stone, the last thing he ever expected was for his one-night stand to show up on his doorstep eight weeks later to tell him she''s pregnant with his child.', '8 wins & 26 nominations total', '6.9', '393,663', '85', '2007-06-01', '129 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (122, 'Wedding Crashers', 'tt0396269', '2005', 'movie', 'https://m.media-amazon.com/images/M/MV5BYzQwNmU0NGEtZjlmYy00ZjQ5LTlmMWYtODY3YzI4NTdiYzA4XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:36.449411+00', '2025-10-19 12:03:36.449427+00', 'John Beckwith and Jeremy Grey, a pair of committed womanizers who sneak into weddings to take advantage of the romantic tinge in the air, find themselves at odds with one another when John meets and falls for Claire Cleary.', '11 wins & 11 nominations total', '7.0', '389,845', '64', '2005-07-15', '119 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (123, 'Dodgeball: A True Underdog Story', 'tt0364725', '2004', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTIwMzE2MjM4MV5BMl5BanBnXkFtZTYwNjA1OTY3._V1_SX300.jpg', '2025-10-19 12:03:36.856793+00', '2025-10-19 12:03:36.856809+00', 'A group of misfits enter a Las Vegas dodgeball tournament in order to save their cherished local gym from the onslaught of a corporate health fitness chain.', '2 wins & 9 nominations total', '6.7', '278,904', '55', '2004-06-18', '92 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (124, 'Napoleon Dynamite', 'tt0374900', '2004', 'movie', 'https://m.media-amazon.com/images/M/MV5BNjYwNTA3MDIyMl5BMl5BanBnXkFtZTYwMjIxNjA3._V1_SX300.jpg', '2025-10-19 12:03:37.217101+00', '2025-10-19 12:03:37.217117+00', 'A listless and alienated teenager helps his new friend win the class presidency in their small western high school, while dealing with his bizarre family life back home.', '10 wins & 23 nominations total', '7.0', '251,071', '64', '2004-08-27', '96 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (125, 'The Other Guys', 'tt1386588', '2010', 'movie', 'https://m.media-amazon.com/images/M/MV5BODU1OTY5ZTYtNWQ0MC00ZWE1LTkyYjEtZTI2ODM1ZGE2MjBkXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:37.572613+00', '2025-10-19 12:03:37.572628+00', 'Two mismatched New York City detectives seize an opportunity to step up like the city''s top cops, whom they idolize, only things don''t quite go as planned.', '3 wins & 15 nominations total', '6.7', '303,001', '64', '2010-08-06', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (126, 'Talladega Nights: The Ballad of Ricky Bobby', 'tt0415306', '2006', 'movie', 'https://m.media-amazon.com/images/M/MV5BNzAzOTk1OTIyM15BMl5BanBnXkFtZTcwNDIzNTQzMQ@@._V1_SX300.jpg', '2025-10-19 12:03:37.98217+00', '2025-10-19 12:03:37.982187+00', 'Number one NASCAR driver Ricky Bobby stays atop the heap thanks to a pact with his best friend and teammate, Cal Naughton, Jr. But when a French Formula One driver, makes his way up the ladder, Ricky Bobby''s talent and devotion ar...', '8 wins & 9 nominations total', '6.6', '209,231', '66', '2006-08-04', '108 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (127, 'Austin Powers: International Man of Mystery', 'tt0118655', '1997', 'movie', 'https://m.media-amazon.com/images/M/MV5BODQzM2UwODQtMzg1ZC00MTk4LTlkOTEtYzU4NDFhYmM1MWJkXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:38.293602+00', '2025-10-19 12:03:38.293618+00', 'A world-class playboy and part-time secret agent from the 1960s emerges after thirty years in a cryogenic state to battle with his nemesis Dr. Evil.', '3 wins & 8 nominations total', '7.0', '268,496', '51', '1997-05-02', '89 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (128, 'Dumb and Dumber', 'tt0109686', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BNGQxZDA1MmMtYWQ1Ni00NTJmLTljMjgtZWVmODllODVhMzgyXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:38.697357+00', '2025-10-19 12:03:38.697374+00', 'After a woman leaves a briefcase at the airport terminal, a dumb limo driver and his dumber friend set out on a hilarious cross-country road trip to Aspen to return it.', '5 wins & 3 nominations total', '7.3', '432,617', '41', '1994-12-16', '107 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (129, 'Meet the Parents', 'tt0212338', '2000', 'movie', 'https://m.media-amazon.com/images/M/MV5BZmE0MGI0OTctOGRlMy00MDdjLTg4M2EtNzFmZWNiNDhjYTgzXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-19 12:03:39.109744+00', '2025-10-19 12:03:39.109765+00', 'Chicago male nurse and chronic under-achiever Greg Focker meets his charming teacher girlfriend Pam Byrnes'' parents Jack and Dina before proposing, but suspicious Jack is an overprotective former CIA agent - every date''s worst nig...', 'Nominated for 1 Oscar. 7 wins & 15 nominations total', '7.0', '372,039', '73', '2000-10-06', '108 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (130, 'Up', 'tt1049413', '2009', 'movie', 'https://m.media-amazon.com/images/M/MV5BNmI1ZTc5MWMtMDYyOS00ZDc2LTkzOTAtNjQ4NWIxNjYyNDgzXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 18:54:19.726014+00', '2025-10-24 18:54:19.726065+00', '78-year-old Carl Fredricksen travels to South America in his house equipped with balloons, inadvertently taking a young stowaway.', 'Won 2 Oscars. 81 wins & 88 nominations total', '8.3', '1,204,006', '88', '2009-05-29', '96 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (131, 'The Ultimate ''WALL-E'' Recap Cartoon', 'tt20453422', '2022', 'movie', 'https://m.media-amazon.com/images/M/MV5BMTY5Yjc1YzUtMjkxMS00YTY3LThkOTAtZGI0ODFlN2Y3OGJjXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 18:54:20.172764+00', '2025-10-24 18:54:20.17278+00', '', '', '', '', '', '2022-02-18', '5 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (132, 'Pulp Fiction', 'tt0110912', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BYTViYTE3ZGQtNDBlMC00ZTAyLTkyODMtZGRiZDg0MjA2YThkXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:41.66211+00', '2025-10-24 19:36:41.66217+00', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'Won 1 Oscar. 69 wins & 72 nominations total', '8.8', '2,371,438', '95', '1994-10-14', '154 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (133, 'The Shawshank Redemption', 'tt0111161', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVkNGY2ZjljXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:55.371314+00', '2025-10-24 19:36:55.371331+00', 'A banker convicted of uxoricide forms a friendship over a quarter century with a hardened convict, while maintaining his innocence and trying to remain hopeful through simple compassion.', 'Nominated for 7 Oscars. 21 wins & 42 nominations total', '9.3', '3,104,274', '82', '1994-10-14', '142 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (134, 'Forrest Gump', 'tt0109830', '1994', 'movie', 'https://m.media-amazon.com/images/M/MV5BNDYwNzVjMTItZmU5YS00YjQ5LTljYjgtMjY2NDVmYWMyNWFmXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:55.780067+00', '2025-10-24 19:36:55.780083+00', 'The history of the United States from the 1950s to the ''70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.', 'Won 6 Oscars. 51 wins & 74 nominations total', '8.8', '2,422,593', '82', '1994-07-06', '142 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (135, 'Goodfellas', 'tt0099685', '1990', 'movie', 'https://m.media-amazon.com/images/M/MV5BN2E5NzI2ZGMtY2VjNi00YTRjLWI1MDUtZGY5OWU1MWJjZjRjXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:56.28832+00', '2025-10-24 19:36:56.288343+00', 'The story of Henry Hill and his life in the mafia, covering his relationship with his wife Karen and his mob partners Jimmy Conway and Tommy DeVito.', 'Won 1 Oscar. 44 wins & 38 nominations total', '8.7', '1,350,647', '92', '1990-09-21', '145 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (136, 'The Godfather', 'tt0068646', '1972', 'movie', 'https://m.media-amazon.com/images/M/MV5BNGEwYjgwOGQtYjg5ZS00Njc1LTk2ZGEtM2QwZWQ2NjdhZTE5XkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:56.701351+00', '2025-10-24 19:36:56.701373+00', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 'Won 3 Oscars. 31 wins & 31 nominations total', '9.2', '2,169,748', '100', '1972-03-24', '175 min', '');
INSERT INTO public.movie_movie (id, title, imdb_id, year, type, poster, created_at, updated_at, plot, awards, imdb_rating, imdb_votes, metascore, released_date, runtime, total_seasons) VALUES (137, 'Casablanca', 'tt0034583', '1942', 'movie', 'https://m.media-amazon.com/images/M/MV5BNWEzN2U1YTYtYTQyMS00NTVkLWE2NGQtZWFlMmM0MDNjMmRiXkEyXkFqcGc@._V1_SX300.jpg', '2025-10-24 19:36:57.079826+00', '2025-10-24 19:36:57.079849+00', 'A cynical expatriate American cafe owner struggles to decide whether or not to help his former lover and her fugitive husband escape the Nazis in French Morocco.', 'Won 3 Oscars. 18 wins & 12 nominations total', '8.5', '640,770', '100', '1943-01-23', '102 min', '');


--
-- Data for Name: movie_likemovie; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_likemovie (id, created_at, updated_at, user_id, movie_id) VALUES (2, '2025-09-14 12:51:32.960865+00', '2025-09-14 12:51:32.960886+00', 1, 11);
INSERT INTO public.movie_likemovie (id, created_at, updated_at, user_id, movie_id) VALUES (6, '2025-10-04 10:07:43.189888+00', '2025-10-04 10:07:43.189901+00', 5, 46);


--
-- Data for Name: movie_movie_actors; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (2, 1, 2);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (3, 1, 3);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (4, 2, 1);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (5, 2, 4);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (6, 2, 5);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (7, 3, 1);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (8, 3, 6);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (9, 3, 7);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (10, 4, 8);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (11, 4, 9);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (12, 4, 10);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (13, 5, 9);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (14, 5, 11);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (15, 5, 12);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (16, 6, 13);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (17, 6, 14);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (18, 6, 15);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (19, 7, 16);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (20, 7, 17);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (21, 7, 18);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (22, 8, 19);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (23, 8, 20);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (24, 8, 21);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (25, 9, 24);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (26, 9, 22);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (27, 9, 23);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (28, 10, 25);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (29, 10, 26);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (30, 10, 27);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (31, 11, 28);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (32, 11, 29);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (33, 11, 30);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (34, 12, 32);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (35, 12, 33);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (36, 12, 31);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (37, 13, 34);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (38, 13, 35);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (39, 13, 36);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (40, 14, 37);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (41, 14, 38);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (42, 14, 39);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (43, 15, 40);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (44, 15, 41);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (45, 15, 42);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (46, 16, 43);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (47, 16, 44);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (48, 16, 45);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (49, 17, 48);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (50, 17, 46);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (51, 17, 47);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (52, 18, 49);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (53, 18, 50);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (54, 18, 51);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (55, 19, 52);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (56, 19, 53);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (57, 19, 54);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (58, 20, 56);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (59, 20, 57);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (60, 20, 55);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (61, 21, 58);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (62, 21, 59);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (63, 21, 60);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (64, 22, 61);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (65, 22, 62);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (66, 22, 63);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (67, 23, 64);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (68, 23, 65);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (69, 23, 51);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (70, 24, 66);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (71, 24, 67);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (72, 24, 68);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (73, 25, 69);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (74, 25, 70);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (75, 25, 71);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (76, 26, 72);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (77, 26, 73);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (78, 26, 74);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (79, 27, 75);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (80, 27, 76);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (81, 27, 77);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (82, 28, 80);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (83, 28, 78);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (84, 28, 79);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (85, 29, 81);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (86, 29, 82);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (87, 29, 83);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (88, 30, 84);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (89, 30, 85);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (90, 30, 86);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (91, 31, 88);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (92, 31, 89);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (93, 31, 87);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (94, 32, 90);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (95, 32, 91);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (96, 32, 92);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (97, 33, 93);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (98, 33, 94);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (99, 33, 95);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (100, 34, 96);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (101, 34, 97);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (102, 34, 98);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (103, 35, 99);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (104, 35, 100);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (105, 35, 101);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (106, 36, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (107, 36, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (108, 36, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (109, 37, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (110, 37, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (111, 37, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (112, 38, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (113, 38, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (114, 38, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (115, 39, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (116, 39, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (117, 39, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (118, 40, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (119, 40, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (120, 40, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (121, 41, 104);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (122, 41, 105);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (123, 41, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (124, 41, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (125, 42, 106);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (126, 42, 107);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (127, 42, 108);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (128, 43, 110);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (129, 43, 109);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (130, 43, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (131, 43, 103);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (132, 44, 112);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (133, 44, 113);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (134, 44, 111);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (135, 45, 114);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (136, 45, 115);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (137, 45, 116);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (138, 46, 117);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (139, 47, 117);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (140, 49, 120);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (141, 49, 118);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (142, 49, 119);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (143, 50, 121);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (144, 50, 122);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (145, 50, 123);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (146, 51, 124);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (147, 51, 125);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (148, 51, 126);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (149, 52, 128);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (150, 52, 129);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (151, 52, 127);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (152, 53, 130);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (153, 53, 131);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (154, 53, 52);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (155, 54, 132);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (156, 54, 133);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (157, 54, 134);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (158, 55, 136);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (159, 55, 137);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (160, 55, 135);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (161, 56, 138);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (162, 56, 139);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (163, 56, 140);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (164, 57, 141);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (165, 57, 142);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (166, 57, 143);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (167, 58, 144);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (168, 58, 145);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (169, 58, 146);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (170, 59, 147);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (171, 59, 148);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (172, 59, 127);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (173, 60, 149);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (174, 60, 150);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (175, 60, 151);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (176, 61, 152);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (177, 61, 153);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (178, 61, 154);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (179, 62, 155);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (180, 62, 156);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (181, 62, 157);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (182, 63, 160);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (183, 63, 158);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (184, 63, 159);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (185, 64, 161);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (186, 64, 162);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (187, 64, 163);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (188, 65, 164);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (189, 65, 165);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (190, 65, 166);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (191, 66, 168);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (192, 66, 57);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (193, 66, 167);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (194, 67, 169);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (195, 67, 170);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (196, 67, 171);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (197, 68, 172);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (198, 68, 173);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (199, 68, 174);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (200, 69, 176);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (201, 69, 46);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (202, 69, 175);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (203, 70, 177);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (204, 70, 178);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (205, 70, 179);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (206, 71, 180);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (207, 71, 181);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (208, 71, 165);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (209, 72, 184);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (210, 72, 182);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (211, 72, 183);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (212, 73, 185);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (213, 73, 186);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (214, 73, 187);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (215, 74, 188);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (216, 74, 189);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (217, 74, 190);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (218, 75, 188);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (219, 75, 189);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (220, 75, 191);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (221, 76, 192);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (222, 76, 193);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (223, 76, 194);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (224, 77, 195);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (225, 77, 196);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (226, 77, 197);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (227, 78, 200);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (228, 78, 198);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (229, 78, 199);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (230, 79, 201);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (231, 79, 202);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (232, 80, 203);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (233, 80, 204);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (234, 80, 205);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (235, 81, 208);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (236, 81, 206);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (237, 81, 207);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (238, 82, 209);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (239, 82, 210);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (240, 82, 211);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (241, 83, 212);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (242, 83, 213);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (243, 83, 214);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (244, 84, 216);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (245, 84, 217);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (246, 84, 215);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (247, 85, 218);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (248, 85, 219);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (249, 85, 220);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (250, 86, 220);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (251, 86, 221);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (252, 86, 222);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (253, 87, 224);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (254, 87, 225);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (255, 87, 223);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (256, 88, 226);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (257, 88, 227);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (258, 88, 228);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (259, 89, 216);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (260, 89, 229);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (261, 89, 230);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (262, 90, 232);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (263, 90, 233);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (264, 90, 231);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (265, 91, 234);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (266, 91, 235);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (267, 91, 230);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (268, 92, 234);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (269, 92, 236);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (270, 92, 230);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (271, 93, 220);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (272, 93, 237);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (273, 93, 238);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (274, 94, 240);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (275, 94, 241);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (276, 94, 239);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (277, 95, 242);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (278, 95, 243);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (279, 95, 87);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (280, 96, 244);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (281, 96, 245);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (282, 96, 87);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (283, 97, 248);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (284, 97, 246);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (285, 97, 247);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (286, 98, 240);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (287, 98, 249);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (288, 98, 246);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (289, 99, 250);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (290, 99, 251);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (291, 99, 252);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (292, 100, 253);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (293, 100, 254);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (294, 100, 255);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (295, 101, 256);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (296, 101, 257);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (297, 101, 258);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (298, 102, 259);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (299, 102, 260);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (300, 102, 261);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (301, 103, 264);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (302, 103, 262);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (303, 103, 263);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (304, 104, 265);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (305, 104, 266);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (306, 104, 267);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (307, 105, 268);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (308, 105, 269);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (309, 105, 71);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (310, 106, 144);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (311, 106, 270);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (312, 106, 271);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (313, 107, 272);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (314, 107, 273);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (315, 107, 274);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (316, 108, 275);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (317, 108, 69);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (318, 108, 79);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (319, 109, 276);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (320, 109, 277);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (321, 109, 278);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (322, 110, 276);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (323, 110, 277);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (324, 110, 279);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (325, 111, 280);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (326, 111, 281);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (327, 111, 282);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (328, 112, 169);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (329, 112, 283);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (330, 112, 284);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (331, 113, 285);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (332, 113, 286);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (333, 113, 287);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (334, 114, 288);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (335, 114, 162);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (336, 114, 246);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (337, 115, 1);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (338, 115, 162);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (339, 115, 289);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (340, 116, 290);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (341, 116, 291);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (342, 116, 278);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (343, 117, 292);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (344, 117, 293);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (345, 117, 294);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (346, 118, 296);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (347, 118, 283);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (348, 118, 295);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (349, 119, 297);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (350, 119, 298);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (351, 119, 299);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (352, 120, 56);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (353, 120, 297);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (354, 120, 298);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (355, 121, 297);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (356, 121, 300);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (357, 121, 301);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (358, 122, 1);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (359, 122, 302);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (360, 122, 303);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (361, 123, 289);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (362, 123, 162);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (363, 123, 302);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (364, 124, 304);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (365, 124, 305);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (366, 124, 306);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (367, 125, 307);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (368, 125, 283);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (369, 125, 308);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (370, 126, 283);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (371, 126, 285);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (372, 126, 295);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (373, 127, 310);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (374, 127, 309);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (375, 127, 102);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (376, 128, 312);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (377, 128, 313);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (378, 128, 311);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (379, 129, 162);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (380, 129, 315);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (381, 129, 314);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (382, 130, 316);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (383, 130, 317);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (384, 130, 318);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (385, 131, 320);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (386, 131, 319);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (387, 132, 321);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (388, 132, 322);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (389, 132, 153);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (390, 133, 242);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (391, 133, 323);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (392, 133, 324);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (393, 134, 155);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (394, 134, 325);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (395, 134, 134);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (396, 135, 314);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (397, 135, 326);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (398, 135, 327);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (399, 136, 328);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (400, 136, 329);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (401, 136, 330);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (402, 137, 331);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (403, 137, 332);
INSERT INTO public.movie_movie_actors (id, movie_id, actor_id) VALUES (404, 137, 333);


--
-- Data for Name: movie_movie_countries; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (2, 2, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (3, 2, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (4, 2, 3);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (5, 2, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (6, 3, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (7, 3, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (8, 3, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (9, 4, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (10, 4, 3);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (11, 5, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (12, 5, 3);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (13, 5, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (14, 5, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (15, 6, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (16, 6, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (17, 7, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (18, 7, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (19, 7, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (20, 8, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (21, 8, 6);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (22, 9, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (23, 10, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (24, 11, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (25, 12, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (26, 13, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (27, 13, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (28, 13, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (29, 13, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (30, 13, 9);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (31, 14, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (32, 15, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (33, 16, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (34, 17, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (35, 18, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (36, 19, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (37, 20, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (38, 21, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (39, 22, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (40, 23, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (41, 24, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (42, 25, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (43, 26, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (44, 27, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (45, 27, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (46, 28, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (47, 29, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (48, 29, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (49, 29, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (50, 30, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (51, 31, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (52, 32, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (53, 33, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (54, 33, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (55, 33, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (56, 33, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (57, 33, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (58, 33, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (59, 34, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (60, 34, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (61, 34, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (62, 35, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (63, 36, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (64, 37, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (65, 38, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (66, 39, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (67, 39, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (68, 40, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (69, 41, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (70, 41, 11);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (71, 42, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (72, 43, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (73, 43, 11);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (74, 44, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (75, 45, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (76, 46, 11);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (77, 47, 11);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (78, 49, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (79, 49, 12);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (80, 49, 13);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (81, 50, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (82, 50, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (83, 51, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (84, 51, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (85, 52, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (86, 53, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (87, 54, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (88, 55, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (89, 56, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (90, 56, 15);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (91, 57, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (92, 58, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (93, 58, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (94, 59, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (95, 60, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (96, 61, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (97, 62, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (98, 63, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (99, 63, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (100, 63, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (101, 64, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (102, 64, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (103, 64, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (104, 65, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (105, 66, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (106, 66, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (107, 66, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (108, 67, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (109, 67, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (110, 68, 16);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (111, 68, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (112, 68, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (113, 69, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (114, 70, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (115, 71, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (116, 72, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (117, 72, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (118, 73, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (119, 73, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (120, 74, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (121, 75, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (122, 76, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (123, 77, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (124, 78, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (125, 79, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (126, 80, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (127, 81, 17);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (128, 81, 18);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (129, 82, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (130, 83, 18);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (131, 84, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (132, 84, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (133, 85, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (134, 85, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (135, 86, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (136, 87, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (137, 88, 19);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (138, 89, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (139, 90, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (140, 91, 8);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (141, 91, 18);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (142, 92, 18);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (143, 92, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (144, 93, 17);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (145, 93, 18);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (146, 93, 14);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (147, 93, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (148, 94, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (149, 94, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (150, 95, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (151, 96, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (152, 97, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (153, 97, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (154, 98, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (155, 99, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (156, 99, 6);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (157, 100, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (158, 101, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (159, 102, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (160, 102, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (161, 103, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (162, 103, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (163, 104, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (164, 104, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (165, 105, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (166, 105, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (167, 106, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (168, 106, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (169, 106, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (170, 107, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (171, 107, 10);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (172, 107, 20);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (173, 108, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (174, 108, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (175, 109, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (176, 110, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (177, 110, 2);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (178, 111, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (179, 111, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (180, 112, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (181, 113, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (182, 113, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (183, 114, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (184, 114, 4);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (185, 114, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (186, 115, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (187, 115, 5);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (188, 115, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (189, 116, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (190, 116, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (191, 117, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (192, 118, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (193, 119, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (194, 120, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (195, 121, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (196, 122, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (197, 123, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (198, 123, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (199, 124, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (200, 125, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (201, 126, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (202, 127, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (203, 127, 7);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (204, 128, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (205, 129, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (206, 130, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (207, 131, 21);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (208, 132, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (209, 133, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (210, 134, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (211, 135, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (212, 136, 1);
INSERT INTO public.movie_movie_countries (id, movie_id, country_id) VALUES (213, 137, 1);


--
-- Data for Name: movie_movie_directors; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (2, 1, 2);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (3, 2, 1);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (4, 2, 3);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (5, 3, 4);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (6, 4, 5);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (7, 5, 6);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (8, 6, 7);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (9, 7, 8);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (10, 7, 9);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (11, 7, 10);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (12, 8, 11);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (13, 8, 12);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (14, 9, 13);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (15, 9, 14);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (16, 9, 15);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (17, 10, 16);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (18, 10, 17);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (19, 11, 18);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (20, 12, 19);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (21, 13, 20);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (22, 14, 18);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (23, 15, 21);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (24, 16, 22);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (25, 17, 23);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (26, 18, 24);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (27, 19, 24);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (28, 20, 25);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (29, 21, 26);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (30, 22, 27);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (31, 23, 24);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (32, 24, 27);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (33, 25, 28);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (34, 26, 29);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (35, 27, 30);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (36, 28, 31);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (37, 29, 32);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (38, 30, 33);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (39, 31, 34);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (40, 32, 35);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (41, 32, 36);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (42, 33, 37);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (43, 33, 38);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (44, 34, 39);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (45, 35, 40);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (46, 36, 41);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (47, 36, 42);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (48, 37, 41);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (49, 37, 43);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (50, 37, 44);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (51, 38, 45);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (52, 38, 46);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (53, 39, 47);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (54, 40, 48);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (55, 41, 49);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (56, 42, 50);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (57, 43, 41);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (58, 43, 42);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (59, 44, 51);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (60, 45, 48);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (61, 45, 52);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (62, 46, 53);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (63, 47, 53);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (64, 49, 54);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (65, 50, 55);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (66, 51, 56);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (67, 52, 57);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (68, 53, 58);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (69, 53, 59);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (70, 54, 60);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (71, 55, 61);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (72, 56, 62);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (73, 57, 64);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (74, 57, 65);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (75, 57, 63);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (76, 58, 66);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (77, 58, 67);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (78, 59, 68);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (79, 60, 11);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (80, 60, 69);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (81, 60, 70);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (82, 61, 71);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (83, 62, 1);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (84, 63, 72);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (85, 63, 11);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (86, 64, 73);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (87, 64, 74);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (88, 65, 75);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (89, 65, 76);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (90, 66, 77);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (91, 66, 78);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (92, 67, 80);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (93, 67, 79);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (94, 68, 13);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (95, 68, 14);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (96, 69, 13);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (97, 69, 14);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (98, 70, 13);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (99, 70, 14);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (100, 71, 81);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (101, 71, 82);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (102, 71, 83);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (103, 72, 82);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (104, 72, 84);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (105, 73, 48);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (106, 73, 85);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (107, 74, 86);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (108, 75, 86);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (109, 76, 87);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (110, 78, 88);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (111, 79, 89);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (112, 80, 88);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (113, 81, 90);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (114, 83, 91);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (115, 84, 92);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (116, 85, 93);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (117, 86, 94);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (118, 86, 95);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (119, 87, 96);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (120, 88, 97);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (121, 89, 98);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (122, 90, 99);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (123, 91, 100);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (124, 92, 101);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (125, 93, 102);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (126, 94, 103);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (127, 95, 34);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (128, 96, 104);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (129, 97, 105);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (130, 98, 106);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (131, 99, 107);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (132, 100, 108);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (133, 101, 109);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (134, 102, 110);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (135, 103, 111);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (136, 104, 37);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (137, 104, 38);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (138, 105, 112);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (139, 106, 112);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (140, 107, 113);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (141, 108, 112);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (142, 109, 45);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (143, 110, 114);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (144, 110, 115);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (145, 111, 116);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (146, 112, 117);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (147, 113, 118);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (148, 114, 119);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (149, 115, 119);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (150, 116, 120);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (151, 117, 121);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (152, 118, 117);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (153, 119, 122);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (154, 120, 123);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (155, 120, 124);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (156, 121, 125);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (157, 122, 126);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (158, 123, 127);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (159, 124, 128);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (160, 125, 117);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (161, 126, 117);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (162, 127, 129);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (163, 128, 130);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (164, 128, 131);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (165, 129, 129);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (166, 130, 132);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (167, 130, 69);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (168, 131, 133);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (169, 131, 134);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (170, 132, 135);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (171, 133, 136);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (172, 134, 137);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (173, 135, 138);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (174, 136, 139);
INSERT INTO public.movie_movie_directors (id, movie_id, director_id) VALUES (175, 137, 140);


--
-- Data for Name: movie_movie_genres; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (2, 1, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (3, 1, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (4, 2, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (5, 2, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (6, 2, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (7, 3, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (8, 3, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (9, 3, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (10, 4, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (11, 4, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (12, 4, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (13, 5, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (14, 5, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (15, 5, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (16, 6, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (17, 6, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (18, 6, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (19, 7, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (20, 7, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (21, 7, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (22, 8, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (23, 8, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (24, 8, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (25, 9, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (26, 9, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (27, 9, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (28, 10, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (29, 10, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (30, 10, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (31, 11, 8);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (32, 11, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (33, 11, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (34, 12, 9);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (35, 12, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (36, 13, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (37, 13, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (38, 13, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (39, 14, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (40, 14, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (41, 14, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (42, 15, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (43, 15, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (44, 15, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (45, 16, 11);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (46, 16, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (47, 17, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (48, 17, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (49, 18, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (50, 18, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (51, 19, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (52, 20, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (53, 21, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (54, 22, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (55, 22, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (56, 23, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (57, 23, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (58, 24, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (59, 24, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (60, 25, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (61, 25, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (62, 25, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (63, 26, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (64, 26, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (65, 27, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (66, 27, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (67, 27, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (68, 28, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (69, 28, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (70, 28, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (71, 29, 9);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (72, 29, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (73, 29, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (74, 30, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (75, 30, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (76, 31, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (77, 31, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (78, 31, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (79, 32, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (80, 32, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (81, 32, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (82, 33, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (83, 33, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (84, 33, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (85, 34, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (86, 34, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (87, 34, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (88, 35, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (89, 35, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (90, 35, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (91, 36, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (92, 36, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (93, 36, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (94, 37, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (95, 37, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (96, 37, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (97, 38, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (98, 38, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (99, 38, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (100, 39, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (101, 39, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (102, 39, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (103, 40, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (104, 40, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (105, 40, 15);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (106, 41, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (107, 41, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (108, 41, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (109, 41, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (110, 41, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (111, 41, 15);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (112, 42, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (113, 42, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (114, 42, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (115, 43, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (116, 43, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (117, 43, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (118, 43, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (119, 43, 15);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (120, 43, 16);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (121, 44, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (122, 44, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (123, 44, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (124, 45, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (125, 45, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (126, 45, 15);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (127, 46, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (128, 47, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (129, 49, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (130, 49, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (131, 49, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (132, 50, 8);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (133, 50, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (134, 50, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (135, 51, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (136, 51, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (137, 51, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (138, 52, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (139, 52, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (140, 52, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (141, 53, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (142, 53, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (143, 53, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (144, 54, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (145, 54, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (146, 54, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (147, 55, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (148, 55, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (149, 55, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (150, 56, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (151, 56, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (152, 56, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (153, 57, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (154, 57, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (155, 57, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (156, 58, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (157, 58, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (158, 58, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (159, 59, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (160, 59, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (161, 59, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (162, 60, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (163, 60, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (164, 60, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (165, 61, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (166, 61, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (167, 61, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (168, 62, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (169, 62, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (170, 62, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (171, 63, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (172, 63, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (173, 63, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (174, 64, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (175, 64, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (176, 64, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (177, 65, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (178, 65, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (179, 65, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (180, 66, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (181, 66, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (182, 66, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (183, 67, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (184, 67, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (185, 67, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (186, 68, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (187, 68, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (188, 68, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (189, 69, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (190, 69, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (191, 69, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (192, 70, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (193, 70, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (194, 70, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (195, 71, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (196, 71, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (197, 71, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (198, 72, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (199, 72, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (200, 72, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (201, 73, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (202, 73, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (203, 73, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (204, 74, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (205, 74, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (206, 74, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (207, 75, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (208, 75, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (209, 75, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (210, 76, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (211, 76, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (212, 77, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (213, 77, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (214, 77, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (215, 78, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (216, 78, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (217, 78, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (218, 79, 6);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (219, 80, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (220, 80, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (221, 80, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (222, 81, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (223, 81, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (224, 82, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (225, 82, 11);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (226, 83, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (227, 83, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (228, 83, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (229, 84, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (230, 84, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (231, 85, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (232, 85, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (233, 85, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (234, 86, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (235, 86, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (236, 86, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (237, 87, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (238, 88, 11);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (239, 88, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (240, 89, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (241, 89, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (242, 89, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (243, 90, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (244, 91, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (245, 91, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (246, 92, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (247, 92, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (248, 92, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (249, 93, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (250, 93, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (251, 93, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (252, 94, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (253, 94, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (254, 95, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (255, 95, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (256, 96, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (257, 96, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (258, 97, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (259, 97, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (260, 97, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (261, 98, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (262, 98, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (263, 99, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (264, 99, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (265, 99, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (266, 100, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (267, 100, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (268, 100, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (269, 101, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (270, 102, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (271, 102, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (272, 102, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (273, 103, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (274, 103, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (275, 103, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (276, 104, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (277, 104, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (278, 105, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (279, 105, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (280, 105, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (281, 106, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (282, 106, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (283, 106, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (284, 107, 18);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (285, 107, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (286, 107, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (287, 108, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (288, 108, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (289, 108, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (290, 109, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (291, 109, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (292, 109, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (293, 110, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (294, 110, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (295, 110, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (296, 111, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (297, 111, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (298, 112, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (299, 113, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (300, 114, 19);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (301, 114, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (302, 114, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (303, 115, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (304, 116, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (305, 117, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (306, 118, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (307, 119, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (308, 119, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (309, 119, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (310, 120, 17);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (311, 120, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (312, 120, 7);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (313, 121, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (314, 121, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (315, 122, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (316, 122, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (317, 123, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (318, 123, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (319, 124, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (320, 125, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (321, 125, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (322, 125, 4);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (323, 126, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (324, 126, 14);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (325, 127, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (326, 127, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (327, 128, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (328, 129, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (329, 129, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (330, 130, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (331, 130, 2);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (332, 130, 3);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (333, 131, 1);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (334, 131, 15);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (335, 132, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (336, 132, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (337, 133, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (338, 134, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (339, 134, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (340, 135, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (341, 135, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (342, 135, 13);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (343, 136, 10);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (344, 136, 5);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (345, 137, 19);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (346, 137, 12);
INSERT INTO public.movie_movie_genres (id, movie_id, genre_id) VALUES (347, 137, 5);


--
-- Data for Name: movie_movie_languages; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (2, 1, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (3, 1, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (4, 1, 4);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (5, 2, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (6, 2, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (7, 2, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (8, 2, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (9, 2, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (10, 3, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (11, 4, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (12, 4, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (13, 4, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (14, 4, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (15, 4, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (16, 4, 10);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (17, 5, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (18, 5, 11);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (19, 6, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (20, 7, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (21, 8, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (22, 8, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (23, 9, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (24, 9, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (25, 10, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (26, 11, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (27, 11, 12);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (28, 12, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (29, 12, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (30, 12, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (31, 12, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (32, 12, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (33, 12, 13);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (34, 12, 14);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (35, 12, 15);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (36, 13, 16);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (37, 13, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (38, 13, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (39, 13, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (40, 14, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (41, 15, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (42, 16, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (43, 16, 17);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (44, 16, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (45, 17, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (46, 17, 18);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (47, 17, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (48, 18, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (49, 19, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (50, 19, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (51, 20, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (52, 21, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (53, 22, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (54, 23, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (55, 24, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (56, 24, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (57, 25, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (58, 25, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (59, 26, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (60, 27, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (61, 27, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (62, 27, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (63, 27, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (64, 27, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (65, 27, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (66, 28, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (67, 28, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (68, 28, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (69, 28, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (70, 29, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (71, 29, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (72, 29, 19);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (73, 29, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (74, 30, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (75, 30, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (76, 30, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (77, 30, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (78, 31, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (79, 31, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (80, 32, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (81, 32, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (82, 32, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (83, 32, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (84, 33, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (85, 34, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (86, 34, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (87, 34, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (88, 35, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (89, 35, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (90, 36, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (91, 37, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (92, 38, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (93, 39, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (94, 40, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (95, 41, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (96, 42, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (97, 43, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (98, 44, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (99, 45, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (100, 46, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (101, 47, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (102, 49, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (103, 50, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (104, 51, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (105, 52, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (106, 53, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (107, 53, 20);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (108, 53, 21);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (109, 53, 22);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (110, 54, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (111, 55, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (112, 56, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (113, 57, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (114, 58, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (115, 58, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (116, 59, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (117, 59, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (118, 60, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (119, 61, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (120, 61, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (121, 61, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (122, 61, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (123, 61, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (124, 61, 19);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (125, 62, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (126, 63, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (127, 63, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (128, 63, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (129, 64, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (130, 64, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (131, 64, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (132, 64, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (133, 64, 19);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (134, 64, 23);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (135, 65, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (136, 66, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (137, 67, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (138, 68, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (139, 68, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (140, 69, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (141, 70, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (142, 70, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (143, 71, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (144, 71, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (145, 72, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (146, 72, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (147, 73, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (148, 73, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (149, 74, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (150, 75, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (151, 76, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (152, 77, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (153, 78, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (154, 79, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (155, 80, 13);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (156, 81, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (157, 82, 13);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (158, 83, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (159, 84, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (160, 84, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (161, 84, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (162, 84, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (163, 85, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (164, 85, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (165, 85, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (166, 85, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (167, 85, 25);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (168, 85, 26);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (169, 86, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (170, 86, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (171, 86, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (172, 87, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (173, 87, 27);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (174, 88, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (175, 88, 27);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (176, 89, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (177, 89, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (178, 90, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (179, 90, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (180, 90, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (181, 91, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (182, 91, 28);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (183, 91, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (184, 91, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (185, 92, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (186, 93, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (187, 93, 13);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (188, 94, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (189, 94, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (190, 94, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (191, 94, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (192, 95, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (193, 96, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (194, 97, 32);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (195, 97, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (196, 97, 33);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (197, 97, 17);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (198, 97, 29);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (199, 97, 30);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (200, 97, 31);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (201, 98, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (202, 98, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (203, 99, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (204, 99, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (205, 99, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (206, 99, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (207, 100, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (208, 101, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (209, 102, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (210, 102, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (211, 103, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (212, 103, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (213, 104, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (214, 105, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (215, 105, 3);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (216, 105, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (217, 106, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (218, 107, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (219, 108, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (220, 108, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (221, 109, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (222, 109, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (223, 110, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (224, 110, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (225, 111, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (226, 111, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (227, 111, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (228, 112, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (229, 112, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (230, 112, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (231, 113, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (232, 113, 34);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (233, 113, 35);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (234, 113, 36);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (235, 113, 12);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (236, 114, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (237, 114, 9);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (238, 115, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (239, 116, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (240, 117, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (241, 117, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (242, 117, 37);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (243, 117, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (244, 118, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (245, 118, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (246, 119, 24);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (247, 119, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (248, 119, 27);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (249, 120, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (250, 120, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (251, 121, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (252, 122, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (253, 123, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (254, 123, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (255, 124, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (256, 125, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (257, 125, 38);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (258, 126, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (259, 126, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (260, 127, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (261, 128, 8);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (262, 128, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (263, 128, 39);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (264, 129, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (265, 129, 35);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (266, 129, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (267, 129, 37);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (268, 129, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (269, 130, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (270, 131, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (271, 132, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (272, 132, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (273, 132, 7);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (274, 133, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (275, 134, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (276, 135, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (277, 135, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (278, 135, 35);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (279, 135, 4);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (280, 136, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (281, 136, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (282, 136, 18);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (283, 137, 1);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (284, 137, 2);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (285, 137, 5);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (286, 137, 6);
INSERT INTO public.movie_movie_languages (id, movie_id, language_id) VALUES (287, 137, 8);


--
-- Data for Name: movie_writer; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_writer (id, full_name) VALUES (1, 'John Lasseter');
INSERT INTO public.movie_writer (id, full_name) VALUES (2, 'Joe Ranft');
INSERT INTO public.movie_writer (id, full_name) VALUES (3, 'Jorgen Klubien');
INSERT INTO public.movie_writer (id, full_name) VALUES (4, 'Bradford Lewis');
INSERT INTO public.movie_writer (id, full_name) VALUES (5, 'Dan Fogelman');
INSERT INTO public.movie_writer (id, full_name) VALUES (6, 'Brian Fee');
INSERT INTO public.movie_writer (id, full_name) VALUES (7, 'Ben Queen');
INSERT INTO public.movie_writer (id, full_name) VALUES (8, 'Eyal Podell');
INSERT INTO public.movie_writer (id, full_name) VALUES (9, 'Klay Hall');
INSERT INTO public.movie_writer (id, full_name) VALUES (10, 'Jeffrey M. Howard');
INSERT INTO public.movie_writer (id, full_name) VALUES (11, 'Bobs Gannaway');
INSERT INTO public.movie_writer (id, full_name) VALUES (12, 'Bob Peterson');
INSERT INTO public.movie_writer (id, full_name) VALUES (13, 'Peter Sohn');
INSERT INTO public.movie_writer (id, full_name) VALUES (14, 'Erik Benson');
INSERT INTO public.movie_writer (id, full_name) VALUES (15, 'Brenda Chapman');
INSERT INTO public.movie_writer (id, full_name) VALUES (16, 'Mark Andrews');
INSERT INTO public.movie_writer (id, full_name) VALUES (17, 'Steve Purcell');
INSERT INTO public.movie_writer (id, full_name) VALUES (18, 'Lee Unkrich');
INSERT INTO public.movie_writer (id, full_name) VALUES (19, 'Jason Katz');
INSERT INTO public.movie_writer (id, full_name) VALUES (20, 'Matthew Aldrich');
INSERT INTO public.movie_writer (id, full_name) VALUES (21, 'Jared Bush');
INSERT INTO public.movie_writer (id, full_name) VALUES (22, 'Ron Clements');
INSERT INTO public.movie_writer (id, full_name) VALUES (23, 'John Musker');
INSERT INTO public.movie_writer (id, full_name) VALUES (24, 'Jennifer Lee');
INSERT INTO public.movie_writer (id, full_name) VALUES (25, 'Hans Christian Andersen');
INSERT INTO public.movie_writer (id, full_name) VALUES (26, 'Chris Buck');
INSERT INTO public.movie_writer (id, full_name) VALUES (27, 'Andrew Davenport');
INSERT INTO public.movie_writer (id, full_name) VALUES (28, 'N/A');
INSERT INTO public.movie_writer (id, full_name) VALUES (29, 'Eric Warren Singer');
INSERT INTO public.movie_writer (id, full_name) VALUES (30, 'Ashley E. Miller');
INSERT INTO public.movie_writer (id, full_name) VALUES (31, 'Amy Jump');
INSERT INTO public.movie_writer (id, full_name) VALUES (32, 'Ben Wheatley');
INSERT INTO public.movie_writer (id, full_name) VALUES (33, 'Lawrence Wright');
INSERT INTO public.movie_writer (id, full_name) VALUES (34, 'Menno Meyjes');
INSERT INTO public.movie_writer (id, full_name) VALUES (35, 'Edward Zwick');
INSERT INTO public.movie_writer (id, full_name) VALUES (36, 'Tom Schulman');
INSERT INTO public.movie_writer (id, full_name) VALUES (37, 'John Hughes');
INSERT INTO public.movie_writer (id, full_name) VALUES (38, 'Seth Rogen');
INSERT INTO public.movie_writer (id, full_name) VALUES (39, 'Evan Goldberg');
INSERT INTO public.movie_writer (id, full_name) VALUES (40, 'Adam Herz');
INSERT INTO public.movie_writer (id, full_name) VALUES (41, 'Cameron Crowe');
INSERT INTO public.movie_writer (id, full_name) VALUES (42, 'Amy Heckerling');
INSERT INTO public.movie_writer (id, full_name) VALUES (43, 'Karen McCullah');
INSERT INTO public.movie_writer (id, full_name) VALUES (44, 'Kirsten Smith');
INSERT INTO public.movie_writer (id, full_name) VALUES (45, 'William Shakespeare');
INSERT INTO public.movie_writer (id, full_name) VALUES (46, 'R. Lee Fleming Jr.');
INSERT INTO public.movie_writer (id, full_name) VALUES (47, 'Peter Morgan');
INSERT INTO public.movie_writer (id, full_name) VALUES (48, 'Jez Butterworth');
INSERT INTO public.movie_writer (id, full_name) VALUES (49, 'John-Henry Butterworth');
INSERT INTO public.movie_writer (id, full_name) VALUES (50, 'Jason Keller');
INSERT INTO public.movie_writer (id, full_name) VALUES (51, 'Manish Pandey');
INSERT INTO public.movie_writer (id, full_name) VALUES (52, 'Robert Alan Aurthur');
INSERT INTO public.movie_writer (id, full_name) VALUES (53, 'John Frankenheimer');
INSERT INTO public.movie_writer (id, full_name) VALUES (54, 'William Hanley');
INSERT INTO public.movie_writer (id, full_name) VALUES (55, 'Robert Towne');
INSERT INTO public.movie_writer (id, full_name) VALUES (56, 'Tom Cruise');
INSERT INTO public.movie_writer (id, full_name) VALUES (57, 'Harry Kleiner');
INSERT INTO public.movie_writer (id, full_name) VALUES (58, 'John T. Kelley');
INSERT INTO public.movie_writer (id, full_name) VALUES (59, 'Lilly Wachowski');
INSERT INTO public.movie_writer (id, full_name) VALUES (60, 'Lana Wachowski');
INSERT INTO public.movie_writer (id, full_name) VALUES (61, 'Tatsuo Yoshida');
INSERT INTO public.movie_writer (id, full_name) VALUES (62, 'Jan Skrentny');
INSERT INTO public.movie_writer (id, full_name) VALUES (63, 'Neal Tabachnick');
INSERT INTO public.movie_writer (id, full_name) VALUES (64, 'Sylvester Stallone');
INSERT INTO public.movie_writer (id, full_name) VALUES (65, 'Mark Bomback');
INSERT INTO public.movie_writer (id, full_name) VALUES (66, 'Garth Stein');
INSERT INTO public.movie_writer (id, full_name) VALUES (67, 'William Steig');
INSERT INTO public.movie_writer (id, full_name) VALUES (68, 'Ted Elliott');
INSERT INTO public.movie_writer (id, full_name) VALUES (69, 'Terry Rossio');
INSERT INTO public.movie_writer (id, full_name) VALUES (70, 'Andrew Adamson');
INSERT INTO public.movie_writer (id, full_name) VALUES (71, 'Joe Stillman');
INSERT INTO public.movie_writer (id, full_name) VALUES (72, 'Jeffrey Price');
INSERT INTO public.movie_writer (id, full_name) VALUES (73, 'Josh Klausner');
INSERT INTO public.movie_writer (id, full_name) VALUES (74, 'Darren Lemke');
INSERT INTO public.movie_writer (id, full_name) VALUES (75, 'Gary Trousdale');
INSERT INTO public.movie_writer (id, full_name) VALUES (76, 'Sean Bishop');
INSERT INTO public.movie_writer (id, full_name) VALUES (77, 'Theresa Cullen');
INSERT INTO public.movie_writer (id, full_name) VALUES (78, 'William Steig (characters)');
INSERT INTO public.movie_writer (id, full_name) VALUES (79, 'David Lipman');
INSERT INTO public.movie_writer (id, full_name) VALUES (80, 'David Lindsay-Abaire');
INSERT INTO public.movie_writer (id, full_name) VALUES (81, 'Elaine Rogan');
INSERT INTO public.movie_writer (id, full_name) VALUES (82, 'David Feiss');
INSERT INTO public.movie_writer (id, full_name) VALUES (83, 'Writer One');
INSERT INTO public.movie_writer (id, full_name) VALUES (84, 'Bill Kelly');
INSERT INTO public.movie_writer (id, full_name) VALUES (85, 'Jenny Bicks');
INSERT INTO public.movie_writer (id, full_name) VALUES (86, 'Bill Condon');
INSERT INTO public.movie_writer (id, full_name) VALUES (87, 'Jerry Juhl');
INSERT INTO public.movie_writer (id, full_name) VALUES (88, 'Jack Burns');
INSERT INTO public.movie_writer (id, full_name) VALUES (89, 'Bill Walsh');
INSERT INTO public.movie_writer (id, full_name) VALUES (90, 'Don DaGradi');
INSERT INTO public.movie_writer (id, full_name) VALUES (91, 'P.L. Travers');
INSERT INTO public.movie_writer (id, full_name) VALUES (92, 'Irene Mecchi');
INSERT INTO public.movie_writer (id, full_name) VALUES (93, 'Jonathan Roberts');
INSERT INTO public.movie_writer (id, full_name) VALUES (94, 'Linda Woolverton');
INSERT INTO public.movie_writer (id, full_name) VALUES (95, 'William Goldman');
INSERT INTO public.movie_writer (id, full_name) VALUES (96, 'Roald Dahl');
INSERT INTO public.movie_writer (id, full_name) VALUES (97, 'Nicholas Kazan');
INSERT INTO public.movie_writer (id, full_name) VALUES (98, 'Robin Swicord');
INSERT INTO public.movie_writer (id, full_name) VALUES (99, 'Wolfgang Petersen');
INSERT INTO public.movie_writer (id, full_name) VALUES (100, 'Herman Weigel');
INSERT INTO public.movie_writer (id, full_name) VALUES (101, 'Michael Ende');
INSERT INTO public.movie_writer (id, full_name) VALUES (102, 'Noel Langley');
INSERT INTO public.movie_writer (id, full_name) VALUES (103, 'Florence Ryerson');
INSERT INTO public.movie_writer (id, full_name) VALUES (104, 'Edgar Allan Woolf');
INSERT INTO public.movie_writer (id, full_name) VALUES (105, 'Garth Jennings');
INSERT INTO public.movie_writer (id, full_name) VALUES (106, 'Georg Hurdalek');
INSERT INTO public.movie_writer (id, full_name) VALUES (107, 'Howard Lindsay');
INSERT INTO public.movie_writer (id, full_name) VALUES (108, 'Russel Crouse');
INSERT INTO public.movie_writer (id, full_name) VALUES (109, 'Pete Docter');
INSERT INTO public.movie_writer (id, full_name) VALUES (110, 'Jill Culton');
INSERT INTO public.movie_writer (id, full_name) VALUES (111, 'Jeff Pidgeon');
INSERT INTO public.movie_writer (id, full_name) VALUES (112, 'Brad Bird');
INSERT INTO public.movie_writer (id, full_name) VALUES (113, 'Andrew Stanton');
INSERT INTO public.movie_writer (id, full_name) VALUES (114, 'David Reynolds');
INSERT INTO public.movie_writer (id, full_name) VALUES (115, 'Mark Burton');
INSERT INTO public.movie_writer (id, full_name) VALUES (116, 'Billy Frolick');
INSERT INTO public.movie_writer (id, full_name) VALUES (117, 'Eric Darnell');
INSERT INTO public.movie_writer (id, full_name) VALUES (118, 'Michael J. Wilson');
INSERT INTO public.movie_writer (id, full_name) VALUES (119, 'Michael Berg');
INSERT INTO public.movie_writer (id, full_name) VALUES (120, 'Peter Ackerman');
INSERT INTO public.movie_writer (id, full_name) VALUES (121, 'William Davies');
INSERT INTO public.movie_writer (id, full_name) VALUES (122, 'Dean DeBlois');
INSERT INTO public.movie_writer (id, full_name) VALUES (123, 'Chris Sanders');
INSERT INTO public.movie_writer (id, full_name) VALUES (124, 'Cinco Paul');
INSERT INTO public.movie_writer (id, full_name) VALUES (125, 'Ken Daurio');
INSERT INTO public.movie_writer (id, full_name) VALUES (126, 'Sergio Pablos');
INSERT INTO public.movie_writer (id, full_name) VALUES (127, 'Greg Erb');
INSERT INTO public.movie_writer (id, full_name) VALUES (128, 'Charise Castro Smith');
INSERT INTO public.movie_writer (id, full_name) VALUES (129, 'Byron Howard');
INSERT INTO public.movie_writer (id, full_name) VALUES (130, 'Jacob Grimm');
INSERT INTO public.movie_writer (id, full_name) VALUES (131, 'Wilhelm Grimm');
INSERT INTO public.movie_writer (id, full_name) VALUES (132, 'Dirk Ahner');
INSERT INTO public.movie_writer (id, full_name) VALUES (133, 'Eberhard Alexander Burgh');
INSERT INTO public.movie_writer (id, full_name) VALUES (134, 'Sebastian Niemann');
INSERT INTO public.movie_writer (id, full_name) VALUES (135, 'Jean Chalopin');
INSERT INTO public.movie_writer (id, full_name) VALUES (136, 'Jennifer L. Liu');
INSERT INTO public.movie_writer (id, full_name) VALUES (137, 'Guofu He');
INSERT INTO public.movie_writer (id, full_name) VALUES (138, 'Kuang Ni');
INSERT INTO public.movie_writer (id, full_name) VALUES (139, 'Chiang Shen');
INSERT INTO public.movie_writer (id, full_name) VALUES (140, 'Lulu Wang');
INSERT INTO public.movie_writer (id, full_name) VALUES (141, 'Peter Chiarelli');
INSERT INTO public.movie_writer (id, full_name) VALUES (142, 'Adele Lim');
INSERT INTO public.movie_writer (id, full_name) VALUES (143, 'Kevin Kwan');
INSERT INTO public.movie_writer (id, full_name) VALUES (144, 'Daniel Kwan');
INSERT INTO public.movie_writer (id, full_name) VALUES (145, 'Daniel Scheinert');
INSERT INTO public.movie_writer (id, full_name) VALUES (146, 'Lee Isaac Chung');
INSERT INTO public.movie_writer (id, full_name) VALUES (147, 'Bong Joon Ho');
INSERT INTO public.movie_writer (id, full_name) VALUES (148, 'Han Jin-won');
INSERT INTO public.movie_writer (id, full_name) VALUES (149, 'Dave Callaham');
INSERT INTO public.movie_writer (id, full_name) VALUES (150, 'Destin Daniel Cretton');
INSERT INTO public.movie_writer (id, full_name) VALUES (151, 'Andrew Lanham');
INSERT INTO public.movie_writer (id, full_name) VALUES (152, 'Amy Tan');
INSERT INTO public.movie_writer (id, full_name) VALUES (153, 'Ron Bass');
INSERT INTO public.movie_writer (id, full_name) VALUES (154, 'Wong Kar-Wai');
INSERT INTO public.movie_writer (id, full_name) VALUES (155, 'Feng Li');
INSERT INTO public.movie_writer (id, full_name) VALUES (156, 'Yimou Zhang');
INSERT INTO public.movie_writer (id, full_name) VALUES (157, 'Bin Wang');
INSERT INTO public.movie_writer (id, full_name) VALUES (158, 'Hui-Ling Wang');
INSERT INTO public.movie_writer (id, full_name) VALUES (159, 'James Schamus');
INSERT INTO public.movie_writer (id, full_name) VALUES (160, 'Kuo Jung Tsai');
INSERT INTO public.movie_writer (id, full_name) VALUES (161, 'Sofia Coppola');
INSERT INTO public.movie_writer (id, full_name) VALUES (162, 'Jim Cash');
INSERT INTO public.movie_writer (id, full_name) VALUES (163, 'Jack Epps Jr.');
INSERT INTO public.movie_writer (id, full_name) VALUES (164, 'Ehud Yonay');
INSERT INTO public.movie_writer (id, full_name) VALUES (165, 'Peter Craig');
INSERT INTO public.movie_writer (id, full_name) VALUES (166, 'Mark Fergus');
INSERT INTO public.movie_writer (id, full_name) VALUES (167, 'Hawk Ostby');
INSERT INTO public.movie_writer (id, full_name) VALUES (168, 'Art Marcum');
INSERT INTO public.movie_writer (id, full_name) VALUES (169, 'Joss Whedon');
INSERT INTO public.movie_writer (id, full_name) VALUES (170, 'Zak Penn');
INSERT INTO public.movie_writer (id, full_name) VALUES (171, 'Travis Beacham');
INSERT INTO public.movie_writer (id, full_name) VALUES (172, 'Guillermo del Toro');
INSERT INTO public.movie_writer (id, full_name) VALUES (173, 'Dean Devlin');
INSERT INTO public.movie_writer (id, full_name) VALUES (174, 'Roland Emmerich');
INSERT INTO public.movie_writer (id, full_name) VALUES (175, 'Peter Bonavita');
INSERT INTO public.movie_writer (id, full_name) VALUES (176, 'George Lucas');
INSERT INTO public.movie_writer (id, full_name) VALUES (177, 'James Cameron');
INSERT INTO public.movie_writer (id, full_name) VALUES (178, 'George Miller');
INSERT INTO public.movie_writer (id, full_name) VALUES (179, 'Brendan McCarthy');
INSERT INTO public.movie_writer (id, full_name) VALUES (180, 'Nick Lathouris');
INSERT INTO public.movie_writer (id, full_name) VALUES (181, 'Christopher Nolan');
INSERT INTO public.movie_writer (id, full_name) VALUES (182, 'Jonathan Nolan');
INSERT INTO public.movie_writer (id, full_name) VALUES (183, 'Hampton Fancher');
INSERT INTO public.movie_writer (id, full_name) VALUES (184, 'Michael Green');
INSERT INTO public.movie_writer (id, full_name) VALUES (185, 'Philip K. Dick');
INSERT INTO public.movie_writer (id, full_name) VALUES (186, 'David S. Goyer');
INSERT INTO public.movie_writer (id, full_name) VALUES (187, 'Tom Wheeler');
INSERT INTO public.movie_writer (id, full_name) VALUES (188, 'Brian Lynch');
INSERT INTO public.movie_writer (id, full_name) VALUES (189, 'Paul Fisher');
INSERT INTO public.movie_writer (id, full_name) VALUES (190, 'Tommy Swerdlow');
INSERT INTO public.movie_writer (id, full_name) VALUES (191, 'Stefan Zweig');
INSERT INTO public.movie_writer (id, full_name) VALUES (192, 'Wes Anderson');
INSERT INTO public.movie_writer (id, full_name) VALUES (193, 'Hugo Guinness');
INSERT INTO public.movie_writer (id, full_name) VALUES (194, 'Will Ferrell');
INSERT INTO public.movie_writer (id, full_name) VALUES (195, 'Adam McKay');
INSERT INTO public.movie_writer (id, full_name) VALUES (196, 'Sacha Baron Cohen');
INSERT INTO public.movie_writer (id, full_name) VALUES (197, 'Anthony Hines');
INSERT INTO public.movie_writer (id, full_name) VALUES (198, 'Peter Baynham');
INSERT INTO public.movie_writer (id, full_name) VALUES (199, 'Justin Theroux');
INSERT INTO public.movie_writer (id, full_name) VALUES (200, 'Ben Stiller');
INSERT INTO public.movie_writer (id, full_name) VALUES (201, 'Etan Cohen');
INSERT INTO public.movie_writer (id, full_name) VALUES (202, 'Drake Sather');
INSERT INTO public.movie_writer (id, full_name) VALUES (203, 'John Hamburg');
INSERT INTO public.movie_writer (id, full_name) VALUES (204, 'Jon Lucas');
INSERT INTO public.movie_writer (id, full_name) VALUES (205, 'Scott Moore');
INSERT INTO public.movie_writer (id, full_name) VALUES (206, 'Kristen Wiig');
INSERT INTO public.movie_writer (id, full_name) VALUES (207, 'Annie Mumolo');
INSERT INTO public.movie_writer (id, full_name) VALUES (208, 'John C. Reilly');
INSERT INTO public.movie_writer (id, full_name) VALUES (209, 'Judd Apatow');
INSERT INTO public.movie_writer (id, full_name) VALUES (210, 'Jason Stone');
INSERT INTO public.movie_writer (id, full_name) VALUES (211, 'Steve Faber');
INSERT INTO public.movie_writer (id, full_name) VALUES (212, 'Bob Fisher');
INSERT INTO public.movie_writer (id, full_name) VALUES (213, 'Rawson Marshall Thurber');
INSERT INTO public.movie_writer (id, full_name) VALUES (214, 'Jared Hess');
INSERT INTO public.movie_writer (id, full_name) VALUES (215, 'Jerusha Hess');
INSERT INTO public.movie_writer (id, full_name) VALUES (216, 'Chris Henchy');
INSERT INTO public.movie_writer (id, full_name) VALUES (217, 'Mike Myers');
INSERT INTO public.movie_writer (id, full_name) VALUES (218, 'Peter Farrelly');
INSERT INTO public.movie_writer (id, full_name) VALUES (219, 'Bennett Yellin');
INSERT INTO public.movie_writer (id, full_name) VALUES (220, 'Bobby Farrelly');
INSERT INTO public.movie_writer (id, full_name) VALUES (221, 'Greg Glienna');
INSERT INTO public.movie_writer (id, full_name) VALUES (222, 'Mary Ruth Clarke');
INSERT INTO public.movie_writer (id, full_name) VALUES (223, 'Jim Herzfeld');
INSERT INTO public.movie_writer (id, full_name) VALUES (224, 'Tom McCarthy');
INSERT INTO public.movie_writer (id, full_name) VALUES (225, 'Cas van de Pol');
INSERT INTO public.movie_writer (id, full_name) VALUES (226, 'Brian Bear');
INSERT INTO public.movie_writer (id, full_name) VALUES (227, 'Christopher Yeh');
INSERT INTO public.movie_writer (id, full_name) VALUES (228, 'Quentin Tarantino');
INSERT INTO public.movie_writer (id, full_name) VALUES (229, 'Roger Avary');
INSERT INTO public.movie_writer (id, full_name) VALUES (230, 'Stephen King');
INSERT INTO public.movie_writer (id, full_name) VALUES (231, 'Frank Darabont');
INSERT INTO public.movie_writer (id, full_name) VALUES (232, 'Winston Groom');
INSERT INTO public.movie_writer (id, full_name) VALUES (233, 'Eric Roth');
INSERT INTO public.movie_writer (id, full_name) VALUES (234, 'Nicholas Pileggi');
INSERT INTO public.movie_writer (id, full_name) VALUES (235, 'Martin Scorsese');
INSERT INTO public.movie_writer (id, full_name) VALUES (236, 'Mario Puzo');
INSERT INTO public.movie_writer (id, full_name) VALUES (237, 'Francis Ford Coppola');
INSERT INTO public.movie_writer (id, full_name) VALUES (238, 'Philip G. Epstein');
INSERT INTO public.movie_writer (id, full_name) VALUES (239, 'Julius J. Epstein');
INSERT INTO public.movie_writer (id, full_name) VALUES (240, 'Howard Koch');


--
-- Data for Name: movie_movie_writers; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (1, 1, 1);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (2, 1, 2);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (3, 1, 3);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (4, 2, 1);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (5, 2, 4);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (6, 2, 5);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (7, 3, 8);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (8, 3, 6);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (9, 3, 7);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (10, 4, 1);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (11, 4, 10);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (12, 4, 9);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (13, 5, 10);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (14, 5, 11);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (15, 6, 12);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (16, 6, 13);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (17, 6, 14);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (18, 7, 16);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (19, 7, 17);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (20, 7, 15);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (21, 8, 18);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (22, 8, 19);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (23, 8, 20);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (24, 9, 21);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (25, 9, 22);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (26, 9, 23);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (27, 10, 24);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (28, 10, 25);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (29, 10, 26);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (30, 11, 27);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (31, 12, 28);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (32, 13, 29);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (33, 14, 30);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (34, 15, 32);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (35, 15, 31);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (36, 16, 33);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (37, 16, 34);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (38, 16, 35);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (39, 17, 36);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (40, 18, 37);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (41, 19, 37);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (42, 20, 38);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (43, 20, 39);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (44, 21, 40);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (45, 22, 41);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (46, 23, 37);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (47, 24, 42);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (48, 25, 43);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (49, 25, 44);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (50, 25, 45);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (51, 26, 46);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (52, 27, 47);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (53, 28, 48);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (54, 28, 49);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (55, 28, 50);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (56, 29, 51);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (57, 30, 52);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (58, 30, 53);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (59, 30, 54);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (60, 31, 56);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (61, 31, 55);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (62, 32, 57);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (63, 32, 58);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (64, 33, 59);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (65, 33, 60);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (66, 33, 61);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (67, 34, 64);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (68, 34, 62);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (69, 34, 63);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (70, 35, 65);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (71, 35, 66);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (72, 36, 67);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (73, 36, 68);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (74, 36, 69);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (75, 37, 67);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (76, 37, 70);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (77, 37, 71);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (78, 38, 72);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (79, 38, 67);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (80, 38, 70);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (81, 39, 73);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (82, 39, 74);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (83, 39, 67);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (84, 40, 75);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (85, 40, 76);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (86, 40, 77);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (87, 41, 78);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (88, 41, 79);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (89, 42, 80);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (90, 42, 67);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (91, 42, 68);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (92, 43, 28);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (93, 44, 68);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (94, 44, 69);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (95, 44, 71);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (96, 45, 81);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (97, 45, 82);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (98, 45, 76);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (99, 46, 83);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (100, 47, 83);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (101, 49, 84);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (102, 50, 85);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (103, 50, 86);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (104, 51, 88);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (105, 51, 87);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (106, 52, 89);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (107, 52, 90);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (108, 52, 91);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (109, 53, 92);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (110, 53, 93);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (111, 53, 94);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (112, 54, 95);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (113, 55, 96);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (114, 55, 97);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (115, 55, 98);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (116, 56, 99);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (117, 56, 100);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (118, 56, 101);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (119, 57, 104);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (120, 57, 102);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (121, 57, 103);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (122, 58, 105);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (123, 59, 106);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (124, 59, 107);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (125, 59, 108);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (126, 60, 109);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (127, 60, 110);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (128, 60, 111);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (129, 61, 112);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (130, 62, 1);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (131, 62, 109);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (132, 62, 113);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (133, 63, 113);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (134, 63, 114);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (135, 63, 12);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (136, 64, 115);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (137, 64, 116);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (138, 64, 117);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (139, 65, 120);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (140, 65, 118);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (141, 65, 119);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (142, 66, 121);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (143, 66, 122);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (144, 66, 123);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (145, 67, 124);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (146, 67, 125);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (147, 67, 126);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (148, 68, 127);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (149, 68, 22);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (150, 68, 23);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (151, 69, 68);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (152, 69, 22);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (153, 69, 23);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (154, 70, 25);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (155, 70, 22);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (156, 70, 23);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (157, 71, 128);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (158, 71, 129);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (159, 71, 21);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (160, 72, 130);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (161, 72, 131);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (162, 72, 5);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (163, 73, 123);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (164, 73, 94);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (165, 73, 15);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (166, 74, 132);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (167, 74, 133);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (168, 74, 134);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (169, 75, 132);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (170, 75, 134);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (171, 76, 136);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (172, 76, 135);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (173, 79, 137);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (174, 81, 138);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (175, 83, 139);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (176, 84, 140);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (177, 85, 141);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (178, 85, 142);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (179, 85, 143);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (180, 86, 144);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (181, 86, 145);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (182, 87, 146);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (183, 88, 147);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (184, 88, 148);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (185, 89, 149);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (186, 89, 150);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (187, 89, 151);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (188, 90, 152);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (189, 90, 153);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (190, 91, 154);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (191, 92, 155);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (192, 92, 156);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (193, 92, 157);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (194, 93, 160);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (195, 93, 158);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (196, 93, 159);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (197, 94, 161);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (198, 95, 162);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (199, 95, 163);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (200, 95, 164);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (201, 96, 162);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (202, 96, 163);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (203, 96, 165);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (204, 97, 168);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (205, 97, 166);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (206, 97, 167);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (207, 98, 169);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (208, 98, 170);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (209, 99, 171);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (210, 99, 172);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (211, 100, 173);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (212, 100, 174);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (213, 101, 176);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (214, 101, 175);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (215, 102, 177);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (216, 103, 178);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (217, 103, 179);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (218, 103, 180);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (219, 104, 59);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (220, 104, 60);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (221, 105, 181);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (222, 106, 181);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (223, 106, 182);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (224, 107, 184);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (225, 107, 185);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (226, 107, 183);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (227, 108, 186);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (228, 108, 181);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (229, 108, 182);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (230, 109, 121);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (231, 109, 187);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (232, 109, 188);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (233, 110, 187);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (234, 110, 189);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (235, 110, 190);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (236, 111, 192);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (237, 111, 193);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (238, 111, 191);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (239, 112, 194);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (240, 112, 195);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (241, 113, 196);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (242, 113, 197);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (243, 113, 198);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (244, 114, 200);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (245, 114, 201);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (246, 114, 199);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (247, 115, 200);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (248, 115, 202);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (249, 115, 203);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (250, 116, 204);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (251, 116, 205);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (252, 117, 206);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (253, 117, 207);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (254, 118, 208);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (255, 118, 194);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (256, 118, 195);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (257, 119, 209);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (258, 119, 38);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (259, 119, 39);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (260, 120, 210);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (261, 120, 38);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (262, 120, 39);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (263, 121, 209);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (264, 122, 211);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (265, 122, 212);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (266, 123, 213);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (267, 124, 214);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (268, 124, 215);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (269, 125, 216);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (270, 125, 195);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (271, 126, 194);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (272, 126, 195);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (273, 127, 217);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (274, 128, 218);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (275, 128, 219);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (276, 128, 220);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (277, 129, 221);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (278, 129, 222);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (279, 129, 223);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (280, 130, 224);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (281, 130, 12);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (282, 130, 109);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (283, 131, 225);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (284, 131, 226);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (285, 131, 227);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (286, 132, 228);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (287, 132, 229);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (288, 133, 230);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (289, 133, 231);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (290, 134, 232);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (291, 134, 233);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (292, 135, 234);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (293, 135, 235);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (294, 136, 236);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (295, 136, 237);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (296, 137, 240);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (297, 137, 238);
INSERT INTO public.movie_movie_writers (id, movie_id, writer_id) VALUES (298, 137, 239);


--
-- Data for Name: movie_rating; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (1, 'Internet Movie Database', '7.3/10', '2025-09-14 10:49:55.546354+00', 1);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (2, 'Rotten Tomatoes', '74%', '2025-09-14 10:49:55.547073+00', 1);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (3, 'Metacritic', '73/100', '2025-09-14 10:49:55.548403+00', 1);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (4, 'Internet Movie Database', '6.2/10', '2025-09-14 10:49:56.093436+00', 2);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (5, 'Rotten Tomatoes', '40%', '2025-09-14 10:49:56.094147+00', 2);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (6, 'Metacritic', '57/100', '2025-09-14 10:49:56.09485+00', 2);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (7, 'Internet Movie Database', '6.7/10', '2025-09-14 10:49:56.731402+00', 3);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (8, 'Rotten Tomatoes', '70%', '2025-09-14 10:49:56.732124+00', 3);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (9, 'Metacritic', '59/100', '2025-09-14 10:49:56.732833+00', 3);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (10, 'Internet Movie Database', '5.7/10', '2025-09-14 10:49:57.662165+00', 4);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (11, 'Rotten Tomatoes', '26%', '2025-09-14 10:49:57.662878+00', 4);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (12, 'Metacritic', '39/100', '2025-09-14 10:49:57.664001+00', 4);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (13, 'Internet Movie Database', '5.9/10', '2025-09-14 10:49:58.175321+00', 5);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (14, 'Rotten Tomatoes', '44%', '2025-09-14 10:49:58.17604+00', 5);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (15, 'Metacritic', '48/100', '2025-09-14 10:49:58.176739+00', 5);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (16, 'Internet Movie Database', '6.7/10', '2025-09-14 10:55:48.705833+00', 6);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (17, 'Rotten Tomatoes', '76%', '2025-09-14 10:55:48.706613+00', 6);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (18, 'Metacritic', '66/100', '2025-09-14 10:55:48.707326+00', 6);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (19, 'Internet Movie Database', '7.1/10', '2025-09-14 10:55:49.325064+00', 7);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (20, 'Rotten Tomatoes', '78%', '2025-09-14 10:55:49.32579+00', 7);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (21, 'Metacritic', '69/100', '2025-09-14 10:55:49.326497+00', 7);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (22, 'Internet Movie Database', '8.4/10', '2025-09-14 10:55:49.712236+00', 8);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (23, 'Rotten Tomatoes', '97%', '2025-09-14 10:55:49.712928+00', 8);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (24, 'Metacritic', '81/100', '2025-09-14 10:55:49.713591+00', 8);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (25, 'Internet Movie Database', '7.6/10', '2025-09-14 10:55:50.210079+00', 9);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (26, 'Rotten Tomatoes', '95%', '2025-09-14 10:55:50.211202+00', 9);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (27, 'Metacritic', '81/100', '2025-09-14 10:55:50.211917+00', 9);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (28, 'Internet Movie Database', '7.4/10', '2025-09-14 10:55:50.73614+00', 10);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (29, 'Rotten Tomatoes', '89%', '2025-09-14 10:55:50.736855+00', 10);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (30, 'Metacritic', '75/100', '2025-09-14 10:55:50.737558+00', 10);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (31, 'Internet Movie Database', '3.9/10', '2025-09-14 11:02:37.73923+00', 11);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (32, 'Internet Movie Database', '7.6/10', '2025-09-14 12:52:28.586556+00', 12);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (33, 'Internet Movie Database', '6.5/10', '2025-09-14 12:52:29.05313+00', 13);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (34, 'Rotten Tomatoes', '57%', '2025-09-14 12:52:29.053848+00', 13);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (35, 'Metacritic', '52/100', '2025-09-14 12:52:29.054562+00', 13);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (36, 'Internet Movie Database', '7.7/10', '2025-09-14 12:52:29.592688+00', 14);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (37, 'Internet Movie Database', '6.3/10', '2025-09-14 12:55:37.446007+00', 15);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (38, 'Rotten Tomatoes', '69%', '2025-09-14 12:55:37.446756+00', 15);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (39, 'Metacritic', '63/100', '2025-09-14 12:55:37.447639+00', 15);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (40, 'Internet Movie Database', '6.4/10', '2025-09-14 12:55:44.085229+00', 16);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (41, 'Rotten Tomatoes', '44%', '2025-09-14 12:55:44.086006+00', 16);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (42, 'Metacritic', '53/100', '2025-09-14 12:55:44.086756+00', 16);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (43, 'Internet Movie Database', '8.1/10', '2025-09-14 13:01:00.261153+00', 17);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (44, 'Rotten Tomatoes', '84%', '2025-09-14 13:01:00.261881+00', 17);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (45, 'Metacritic', '79/100', '2025-09-14 13:01:00.262592+00', 17);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (46, 'Internet Movie Database', '7.8/10', '2025-09-14 13:01:00.619995+00', 18);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (47, 'Rotten Tomatoes', '87%', '2025-09-14 13:01:00.62071+00', 18);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (48, 'Metacritic', '66/100', '2025-09-14 13:01:00.621412+00', 18);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (49, 'Internet Movie Database', '7.8/10', '2025-09-14 13:01:01.030732+00', 19);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (50, 'Rotten Tomatoes', '83%', '2025-09-14 13:01:01.031458+00', 19);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (51, 'Metacritic', '61/100', '2025-09-14 13:01:01.032164+00', 19);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (52, 'Internet Movie Database', '7.6/10', '2025-09-14 13:01:01.379762+00', 20);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (53, 'Rotten Tomatoes', '88%', '2025-09-14 13:01:01.380704+00', 20);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (54, 'Metacritic', '76/100', '2025-09-14 13:01:01.381578+00', 20);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (55, 'Internet Movie Database', '7.0/10', '2025-09-14 13:01:01.758752+00', 21);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (56, 'Rotten Tomatoes', '62%', '2025-09-14 13:01:01.759615+00', 21);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (57, 'Metacritic', '58/100', '2025-09-14 13:01:01.760536+00', 21);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (58, 'Internet Movie Database', '7.1/10', '2025-09-14 13:01:02.117738+00', 22);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (59, 'Rotten Tomatoes', '78%', '2025-09-14 13:01:02.118447+00', 22);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (60, 'Metacritic', '61/100', '2025-09-14 13:01:02.119153+00', 22);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (61, 'Internet Movie Database', '7.0/10', '2025-09-14 13:01:02.455674+00', 23);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (62, 'Rotten Tomatoes', '81%', '2025-09-14 13:01:02.456391+00', 23);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (63, 'Metacritic', '61/100', '2025-09-14 13:01:02.457092+00', 23);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (64, 'Internet Movie Database', '6.9/10', '2025-09-14 13:01:02.77471+00', 24);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (65, 'Metacritic', '73/100', '2025-09-14 13:01:02.77543+00', 24);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (66, 'Internet Movie Database', '7.4/10', '2025-09-14 13:01:03.141917+00', 25);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (67, 'Rotten Tomatoes', '71%', '2025-09-14 13:01:03.142626+00', 25);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (68, 'Metacritic', '70/100', '2025-09-14 13:01:03.14334+00', 25);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (69, 'Internet Movie Database', '5.9/10', '2025-09-14 13:01:03.718003+00', 26);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (70, 'Rotten Tomatoes', '42%', '2025-09-14 13:01:03.718729+00', 26);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (71, 'Metacritic', '51/100', '2025-09-14 13:01:03.719429+00', 26);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (72, 'Internet Movie Database', '8.1/10', '2025-09-14 13:17:46.424507+00', 27);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (73, 'Rotten Tomatoes', '89%', '2025-09-14 13:17:46.425329+00', 27);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (74, 'Metacritic', '74/100', '2025-09-14 13:17:46.426131+00', 27);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (75, 'Internet Movie Database', '8.1/10', '2025-09-14 13:17:46.849505+00', 28);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (76, 'Rotten Tomatoes', '92%', '2025-09-14 13:17:46.850618+00', 28);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (77, 'Metacritic', '81/100', '2025-09-14 13:17:46.851372+00', 28);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (78, 'Internet Movie Database', '8.5/10', '2025-09-14 13:17:47.548457+00', 29);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (79, 'Rotten Tomatoes', '93%', '2025-09-14 13:17:47.549181+00', 29);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (80, 'Metacritic', '79/100', '2025-09-14 13:17:47.549914+00', 29);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (81, 'Internet Movie Database', '7.2/10', '2025-09-14 13:17:48.062656+00', 30);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (82, 'Rotten Tomatoes', '92%', '2025-09-14 13:17:48.063586+00', 30);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (83, 'Metacritic', '72/100', '2025-09-14 13:17:48.064458+00', 30);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (84, 'Internet Movie Database', '6.1/10', '2025-09-14 13:17:48.572202+00', 31);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (85, 'Rotten Tomatoes', '37%', '2025-09-14 13:17:48.572918+00', 31);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (86, 'Metacritic', '60/100', '2025-09-14 13:17:48.573625+00', 31);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (87, 'Internet Movie Database', '6.7/10', '2025-09-14 13:17:48.930752+00', 32);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (88, 'Rotten Tomatoes', '71%', '2025-09-14 13:17:48.931477+00', 32);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (89, 'Metacritic', '52/100', '2025-09-14 13:17:48.932187+00', 32);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (90, 'Internet Movie Database', '6.1/10', '2025-09-14 13:17:49.409411+00', 33);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (91, 'Rotten Tomatoes', '42%', '2025-09-14 13:17:49.409679+00', 33);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (92, 'Metacritic', '37/100', '2025-09-14 13:17:49.409944+00', 33);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (93, 'Internet Movie Database', '4.6/10', '2025-09-14 13:17:49.751486+00', 34);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (94, 'Rotten Tomatoes', '13%', '2025-09-14 13:17:49.752363+00', 34);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (95, 'Metacritic', '29/100', '2025-09-14 13:17:49.753089+00', 34);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (96, 'Internet Movie Database', '7.6/10', '2025-09-14 13:17:50.304918+00', 35);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (97, 'Rotten Tomatoes', '44%', '2025-09-14 13:17:50.305635+00', 35);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (98, 'Metacritic', '43/100', '2025-09-14 13:17:50.306343+00', 35);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (99, 'Internet Movie Database', '7.9/10', '2025-09-14 13:18:51.615374+00', 36);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (100, 'Rotten Tomatoes', '88%', '2025-09-14 13:18:51.616092+00', 36);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (101, 'Metacritic', '84/100', '2025-09-14 13:18:51.616801+00', 36);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (102, 'Internet Movie Database', '7.4/10', '2025-09-14 13:18:52.112549+00', 37);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (103, 'Rotten Tomatoes', '89%', '2025-09-14 13:18:52.113258+00', 37);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (104, 'Metacritic', '75/100', '2025-09-14 13:18:52.11421+00', 37);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (105, 'Internet Movie Database', '6.1/10', '2025-09-14 13:18:52.5116+00', 38);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (106, 'Rotten Tomatoes', '41%', '2025-09-14 13:18:52.512842+00', 38);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (107, 'Metacritic', '58/100', '2025-09-14 13:18:52.514065+00', 38);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (108, 'Internet Movie Database', '6.3/10', '2025-09-14 13:18:53.078886+00', 39);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (109, 'Rotten Tomatoes', '58%', '2025-09-14 13:18:53.079633+00', 39);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (110, 'Metacritic', '58/100', '2025-09-14 13:18:53.080349+00', 39);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (111, 'Internet Movie Database', '6.4/10', '2025-09-14 13:18:53.473528+00', 40);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (112, 'Internet Movie Database', '6.3/10', '2025-09-14 13:18:53.969477+00', 41);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (113, 'Internet Movie Database', '6.9/10', '2025-09-14 13:18:54.364053+00', 42);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (114, 'Internet Movie Database', '7.0/10', '2025-09-14 13:18:54.674838+00', 43);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (115, 'Internet Movie Database', '7.4/10', '2025-09-14 13:18:55.103223+00', 44);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (116, 'Internet Movie Database', '6.2/10', '2025-09-14 13:18:55.591434+00', 45);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (121, 'IMDB', '7.1', '2025-10-04 10:07:43.154495+00', 46);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (122, 'Rotten', '83%', '2025-10-04 10:07:43.155997+00', 46);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (123, 'Internet Movie Database', '7.1/10', '2025-10-04 10:15:04.51822+00', 49);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (124, 'Rotten Tomatoes', '93%', '2025-10-04 10:15:04.518244+00', 49);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (125, 'Metacritic', '75/100', '2025-10-04 10:15:04.518255+00', 49);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (126, 'Internet Movie Database', '7.5/10', '2025-10-04 10:15:05.026779+00', 50);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (127, 'Rotten Tomatoes', '56%', '2025-10-04 10:15:05.026808+00', 50);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (128, 'Metacritic', '48/100', '2025-10-04 10:15:05.026822+00', 50);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (129, 'Internet Movie Database', '7.6/10', '2025-10-04 10:15:05.388349+00', 51);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (130, 'Rotten Tomatoes', '89%', '2025-10-04 10:15:05.388371+00', 51);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (131, 'Metacritic', '74/100', '2025-10-04 10:15:05.388383+00', 51);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (132, 'Internet Movie Database', '7.8/10', '2025-10-04 10:15:05.824482+00', 52);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (133, 'Rotten Tomatoes', '97%', '2025-10-04 10:15:05.824508+00', 52);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (134, 'Metacritic', '88/100', '2025-10-04 10:15:05.82452+00', 52);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (135, 'Internet Movie Database', '8.5/10', '2025-10-04 10:15:06.35094+00', 53);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (136, 'Rotten Tomatoes', '92%', '2025-10-04 10:15:06.350962+00', 53);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (137, 'Metacritic', '88/100', '2025-10-04 10:15:06.350974+00', 53);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (138, 'Internet Movie Database', '8.0/10', '2025-10-04 10:15:06.863258+00', 54);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (139, 'Rotten Tomatoes', '96%', '2025-10-04 10:15:06.863282+00', 54);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (140, 'Metacritic', '78/100', '2025-10-04 10:15:06.863295+00', 54);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (141, 'Internet Movie Database', '7.0/10', '2025-10-04 10:53:20.725943+00', 55);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (142, 'Rotten Tomatoes', '92%', '2025-10-04 10:53:20.725964+00', 55);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (143, 'Metacritic', '72/100', '2025-10-04 10:53:20.725975+00', 55);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (144, 'Internet Movie Database', '7.3/10', '2025-10-04 10:53:20.845809+00', 56);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (145, 'Rotten Tomatoes', '84%', '2025-10-04 10:53:20.84583+00', 56);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (146, 'Metacritic', '49/100', '2025-10-04 10:53:20.845841+00', 56);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (147, 'Internet Movie Database', '8.1/10', '2025-10-04 10:55:11.833983+00', 57);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (148, 'Rotten Tomatoes', '98%', '2025-10-04 10:55:11.83401+00', 57);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (149, 'Metacritic', '92/100', '2025-10-04 10:55:11.834023+00', 57);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (150, 'Internet Movie Database', '7.1/10', '2025-10-04 10:55:12.268269+00', 58);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (151, 'Rotten Tomatoes', '71%', '2025-10-04 10:55:12.268296+00', 58);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (152, 'Metacritic', '59/100', '2025-10-04 10:55:12.268311+00', 58);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (153, 'Internet Movie Database', '8.1/10', '2025-10-04 10:55:12.694481+00', 59);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (154, 'Rotten Tomatoes', '83%', '2025-10-04 10:55:12.694505+00', 59);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (155, 'Metacritic', '63/100', '2025-10-04 10:55:12.694517+00', 59);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (156, 'Internet Movie Database', '8.1/10', '2025-10-19 09:11:03.738835+00', 60);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (157, 'Rotten Tomatoes', '96%', '2025-10-19 09:11:03.738873+00', 60);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (158, 'Metacritic', '79/100', '2025-10-19 09:11:03.738889+00', 60);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (159, 'Internet Movie Database', '8.0/10', '2025-10-19 09:11:04.168303+00', 61);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (160, 'Metacritic', '90/100', '2025-10-19 09:11:04.168328+00', 61);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (161, 'Internet Movie Database', '8.3/10', '2025-10-19 09:11:04.604035+00', 62);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (162, 'Rotten Tomatoes', '100%', '2025-10-19 09:11:04.604061+00', 62);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (163, 'Metacritic', '96/100', '2025-10-19 09:11:04.604072+00', 62);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (164, 'Internet Movie Database', '8.2/10', '2025-10-19 09:11:05.071461+00', 63);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (165, 'Rotten Tomatoes', '99%', '2025-10-19 09:11:05.071496+00', 63);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (166, 'Metacritic', '90/100', '2025-10-19 09:11:05.071513+00', 63);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (167, 'Internet Movie Database', '6.9/10', '2025-10-19 09:11:05.510229+00', 64);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (168, 'Rotten Tomatoes', '55%', '2025-10-19 09:11:05.510264+00', 64);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (169, 'Metacritic', '57/100', '2025-10-19 09:11:05.510284+00', 64);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (170, 'Internet Movie Database', '7.5/10', '2025-10-19 09:11:06.018954+00', 65);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (171, 'Rotten Tomatoes', '76%', '2025-10-19 09:11:06.018978+00', 65);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (172, 'Metacritic', '61/100', '2025-10-19 09:11:06.018989+00', 65);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (173, 'Internet Movie Database', '8.1/10', '2025-10-19 09:11:06.426696+00', 66);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (174, 'Rotten Tomatoes', '99%', '2025-10-19 09:11:06.426727+00', 66);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (175, 'Metacritic', '75/100', '2025-10-19 09:11:06.426743+00', 66);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (176, 'Internet Movie Database', '7.6/10', '2025-10-19 09:11:06.847279+00', 67);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (177, 'Rotten Tomatoes', '80%', '2025-10-19 09:11:06.847384+00', 67);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (178, 'Metacritic', '72/100', '2025-10-19 09:11:06.847404+00', 67);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (179, 'Internet Movie Database', '7.2/10', '2025-10-19 09:11:07.338807+00', 68);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (180, 'Rotten Tomatoes', '86%', '2025-10-19 09:11:07.338841+00', 68);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (181, 'Metacritic', '73/100', '2025-10-19 09:11:07.338857+00', 68);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (182, 'Internet Movie Database', '8.0/10', '2025-10-19 11:04:48.358938+00', 69);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (183, 'Rotten Tomatoes', '96%', '2025-10-19 11:04:48.358949+00', 69);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (184, 'Metacritic', '86/100', '2025-10-19 11:04:48.358953+00', 69);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (185, 'Internet Movie Database', '7.6/10', '2025-10-19 11:04:48.697909+00', 70);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (186, 'Rotten Tomatoes', '92%', '2025-10-19 11:04:48.697934+00', 70);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (187, 'Metacritic', '88/100', '2025-10-19 11:04:48.697947+00', 70);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (188, 'Internet Movie Database', '7.2/10', '2025-10-19 11:04:49.135429+00', 71);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (189, 'Metacritic', '75/100', '2025-10-19 11:04:49.135457+00', 71);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (190, 'Internet Movie Database', '7.7/10', '2025-10-19 11:04:49.52793+00', 72);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (191, 'Rotten Tomatoes', '89%', '2025-10-19 11:04:49.527955+00', 72);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (192, 'Metacritic', '71/100', '2025-10-19 11:04:49.527967+00', 72);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (193, 'Internet Movie Database', '8.0/10', '2025-10-19 11:04:49.933236+00', 73);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (194, 'Rotten Tomatoes', '95%', '2025-10-19 11:04:49.933262+00', 73);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (195, 'Metacritic', '95/100', '2025-10-19 11:04:49.933274+00', 73);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (196, 'Internet Movie Database', '4.8/10', '2025-10-19 11:05:31.917714+00', 74);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (197, 'Internet Movie Database', '5.2/10', '2025-10-19 11:05:32.322447+00', 75);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (198, 'Internet Movie Database', '6.2/10', '2025-10-19 11:16:13.835478+00', 76);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (199, 'Internet Movie Database', '5.9/10', '2025-10-19 11:16:14.169056+00', 77);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (200, 'Internet Movie Database', '5.1/10', '2025-10-19 11:16:14.484796+00', 78);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (201, 'Internet Movie Database', '7.5/10', '2025-10-19 11:16:14.837447+00', 79);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (202, 'Internet Movie Database', '5.5/10', '2025-10-19 11:16:15.160108+00', 80);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (203, 'Internet Movie Database', '6.4/10', '2025-10-19 11:16:15.46112+00', 81);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (204, 'Internet Movie Database', '6.5/10', '2025-10-19 11:16:16.103585+00', 83);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (205, 'Internet Movie Database', '7.5/10', '2025-10-19 11:16:38.652605+00', 84);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (206, 'Rotten Tomatoes', '97%', '2025-10-19 11:16:38.652626+00', 84);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (207, 'Metacritic', '89/100', '2025-10-19 11:16:38.652636+00', 84);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (208, 'Internet Movie Database', '6.9/10', '2025-10-19 11:16:39.059946+00', 85);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (209, 'Rotten Tomatoes', '91%', '2025-10-19 11:16:39.059968+00', 85);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (210, 'Metacritic', '74/100', '2025-10-19 11:16:39.059979+00', 85);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (211, 'Internet Movie Database', '7.8/10', '2025-10-19 11:16:39.440859+00', 86);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (212, 'Rotten Tomatoes', '93%', '2025-10-19 11:16:39.44088+00', 86);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (213, 'Metacritic', '81/100', '2025-10-19 11:16:39.440891+00', 86);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (214, 'Internet Movie Database', '7.4/10', '2025-10-19 11:16:39.778789+00', 87);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (215, 'Rotten Tomatoes', '98%', '2025-10-19 11:16:39.778809+00', 87);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (216, 'Metacritic', '89/100', '2025-10-19 11:16:39.778819+00', 87);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (217, 'Internet Movie Database', '8.5/10', '2025-10-19 11:16:40.182864+00', 88);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (218, 'Rotten Tomatoes', '99%', '2025-10-19 11:16:40.182885+00', 88);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (219, 'Metacritic', '97/100', '2025-10-19 11:16:40.182897+00', 88);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (220, 'Internet Movie Database', '7.3/10', '2025-10-19 11:16:40.596628+00', 89);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (221, 'Rotten Tomatoes', '92%', '2025-10-19 11:16:40.596651+00', 89);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (222, 'Metacritic', '71/100', '2025-10-19 11:16:40.596662+00', 89);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (223, 'Internet Movie Database', '7.7/10', '2025-10-19 11:16:40.944455+00', 90);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (224, 'Rotten Tomatoes', '86%', '2025-10-19 11:16:40.944475+00', 90);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (225, 'Metacritic', '84/100', '2025-10-19 11:16:40.944485+00', 90);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (226, 'Internet Movie Database', '8.1/10', '2025-10-19 11:16:41.34003+00', 91);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (227, 'Rotten Tomatoes', '92%', '2025-10-19 11:16:41.34005+00', 91);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (228, 'Metacritic', '87/100', '2025-10-19 11:16:41.34006+00', 91);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (229, 'Internet Movie Database', '7.9/10', '2025-10-19 11:16:41.723463+00', 92);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (230, 'Metacritic', '85/100', '2025-10-19 11:16:41.723487+00', 92);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (231, 'Internet Movie Database', '7.9/10', '2025-10-19 11:16:42.126449+00', 93);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (232, 'Rotten Tomatoes', '98%', '2025-10-19 11:16:42.126475+00', 93);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (233, 'Metacritic', '94/100', '2025-10-19 11:16:42.126486+00', 93);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (234, 'Internet Movie Database', '7.7/10', '2025-10-19 11:19:33.483399+00', 94);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (235, 'Rotten Tomatoes', '95%', '2025-10-19 11:19:33.483421+00', 94);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (236, 'Metacritic', '91/100', '2025-10-19 11:19:33.483431+00', 94);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (237, 'Internet Movie Database', '7.0/10', '2025-10-19 11:20:04.96812+00', 95);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (238, 'Rotten Tomatoes', '59%', '2025-10-19 11:20:04.968141+00', 95);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (239, 'Metacritic', '50/100', '2025-10-19 11:20:04.968151+00', 95);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (240, 'Internet Movie Database', '8.2/10', '2025-10-19 11:20:05.371727+00', 96);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (241, 'Rotten Tomatoes', '96%', '2025-10-19 11:20:05.371748+00', 96);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (242, 'Metacritic', '78/100', '2025-10-19 11:20:05.371758+00', 96);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (243, 'Internet Movie Database', '7.9/10', '2025-10-19 11:20:05.711775+00', 97);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (244, 'Rotten Tomatoes', '94%', '2025-10-19 11:20:05.711795+00', 97);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (245, 'Metacritic', '79/100', '2025-10-19 11:20:05.711806+00', 97);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (246, 'Internet Movie Database', '8.0/10', '2025-10-19 11:20:06.205897+00', 98);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (247, 'Rotten Tomatoes', '91%', '2025-10-19 11:20:06.205917+00', 98);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (248, 'Metacritic', '69/100', '2025-10-19 11:20:06.205928+00', 98);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (249, 'Internet Movie Database', '6.9/10', '2025-10-19 11:20:06.633192+00', 99);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (250, 'Rotten Tomatoes', '72%', '2025-10-19 11:20:06.633213+00', 99);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (251, 'Metacritic', '65/100', '2025-10-19 11:20:06.633224+00', 99);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (252, 'Internet Movie Database', '7.0/10', '2025-10-19 11:20:06.99084+00', 100);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (253, 'Rotten Tomatoes', '68%', '2025-10-19 11:20:06.990861+00', 100);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (254, 'Metacritic', '59/100', '2025-10-19 11:20:06.990871+00', 100);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (255, 'Internet Movie Database', '7.9/10', '2025-10-19 11:20:07.750471+00', 102);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (256, 'Rotten Tomatoes', '81%', '2025-10-19 11:20:07.750492+00', 102);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (257, 'Metacritic', '83/100', '2025-10-19 11:20:07.750503+00', 102);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (258, 'Internet Movie Database', '8.1/10', '2025-10-19 11:20:08.147361+00', 103);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (259, 'Rotten Tomatoes', '97%', '2025-10-19 11:20:08.147382+00', 103);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (260, 'Metacritic', '90/100', '2025-10-19 11:20:08.147394+00', 103);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (261, 'Internet Movie Database', '8.7/10', '2025-10-19 11:23:58.769431+00', 104);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (262, 'Rotten Tomatoes', '83%', '2025-10-19 11:23:58.769455+00', 104);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (263, 'Metacritic', '73/100', '2025-10-19 11:23:58.769465+00', 104);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (264, 'Internet Movie Database', '8.8/10', '2025-10-19 11:23:59.120628+00', 105);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (265, 'Rotten Tomatoes', '87%', '2025-10-19 11:23:59.120648+00', 105);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (266, 'Metacritic', '74/100', '2025-10-19 11:23:59.120659+00', 105);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (267, 'Internet Movie Database', '8.7/10', '2025-10-19 11:23:59.433609+00', 106);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (268, 'Rotten Tomatoes', '73%', '2025-10-19 11:23:59.433629+00', 106);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (269, 'Metacritic', '74/100', '2025-10-19 11:23:59.433639+00', 106);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (270, 'Internet Movie Database', '8.0/10', '2025-10-19 11:23:59.804295+00', 107);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (271, 'Rotten Tomatoes', '88%', '2025-10-19 11:23:59.804316+00', 107);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (272, 'Metacritic', '81/100', '2025-10-19 11:23:59.804328+00', 107);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (273, 'Internet Movie Database', '9.1/10', '2025-10-19 11:24:00.171818+00', 108);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (274, 'Rotten Tomatoes', '94%', '2025-10-19 11:24:00.171839+00', 108);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (275, 'Metacritic', '85/100', '2025-10-19 11:24:00.171849+00', 108);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (276, 'Internet Movie Database', '6.6/10', '2025-10-19 12:03:19.205903+00', 109);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (277, 'Rotten Tomatoes', '85%', '2025-10-19 12:03:19.205925+00', 109);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (278, 'Metacritic', '65/100', '2025-10-19 12:03:19.205936+00', 109);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (279, 'Internet Movie Database', '7.8/10', '2025-10-19 12:03:19.629871+00', 110);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (280, 'Metacritic', '73/100', '2025-10-19 12:03:19.629902+00', 110);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (281, 'Internet Movie Database', '8.1/10', '2025-10-19 12:03:32.213545+00', 111);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (282, 'Rotten Tomatoes', '92%', '2025-10-19 12:03:32.213566+00', 111);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (283, 'Metacritic', '88/100', '2025-10-19 12:03:32.213577+00', 111);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (284, 'Internet Movie Database', '7.1/10', '2025-10-19 12:03:32.602162+00', 112);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (285, 'Rotten Tomatoes', '66%', '2025-10-19 12:03:32.602182+00', 112);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (286, 'Metacritic', '63/100', '2025-10-19 12:03:32.602193+00', 112);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (287, 'Internet Movie Database', '7.4/10', '2025-10-19 12:03:33.025563+00', 113);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (288, 'Rotten Tomatoes', '90%', '2025-10-19 12:03:33.025583+00', 113);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (289, 'Metacritic', '89/100', '2025-10-19 12:03:33.025594+00', 113);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (290, 'Internet Movie Database', '7.1/10', '2025-10-19 12:03:33.428599+00', 114);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (291, 'Rotten Tomatoes', '82%', '2025-10-19 12:03:33.42862+00', 114);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (292, 'Metacritic', '71/100', '2025-10-19 12:03:33.428631+00', 114);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (293, 'Internet Movie Database', '6.5/10', '2025-10-19 12:03:33.782621+00', 115);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (294, 'Rotten Tomatoes', '64%', '2025-10-19 12:03:33.782642+00', 115);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (295, 'Metacritic', '61/100', '2025-10-19 12:03:33.782653+00', 115);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (296, 'Internet Movie Database', '7.7/10', '2025-10-19 12:03:34.151122+00', 116);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (297, 'Rotten Tomatoes', '79%', '2025-10-19 12:03:34.151151+00', 116);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (298, 'Metacritic', '73/100', '2025-10-19 12:03:34.151166+00', 116);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (299, 'Internet Movie Database', '6.8/10', '2025-10-19 12:03:34.560307+00', 117);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (300, 'Rotten Tomatoes', '89%', '2025-10-19 12:03:34.560327+00', 117);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (301, 'Metacritic', '75/100', '2025-10-19 12:03:34.560338+00', 117);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (302, 'Internet Movie Database', '6.9/10', '2025-10-19 12:03:34.971854+00', 118);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (303, 'Rotten Tomatoes', '54%', '2025-10-19 12:03:34.971881+00', 118);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (304, 'Metacritic', '51/100', '2025-10-19 12:03:34.971893+00', 118);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (305, 'Internet Movie Database', '6.9/10', '2025-10-19 12:03:35.381086+00', 119);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (306, 'Metacritic', '64/100', '2025-10-19 12:03:35.381106+00', 119);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (307, 'Internet Movie Database', '6.6/10', '2025-10-19 12:03:35.788402+00', 120);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (308, 'Rotten Tomatoes', '82%', '2025-10-19 12:03:35.788425+00', 120);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (309, 'Metacritic', '67/100', '2025-10-19 12:03:35.788436+00', 120);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (310, 'Internet Movie Database', '6.9/10', '2025-10-19 12:03:36.120262+00', 121);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (311, 'Rotten Tomatoes', '90%', '2025-10-19 12:03:36.120283+00', 121);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (312, 'Metacritic', '85/100', '2025-10-19 12:03:36.120294+00', 121);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (313, 'Internet Movie Database', '7.0/10', '2025-10-19 12:03:36.513894+00', 122);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (314, 'Rotten Tomatoes', '75%', '2025-10-19 12:03:36.513916+00', 122);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (315, 'Metacritic', '64/100', '2025-10-19 12:03:36.513928+00', 122);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (316, 'Internet Movie Database', '6.7/10', '2025-10-19 12:03:36.90604+00', 123);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (317, 'Rotten Tomatoes', '72%', '2025-10-19 12:03:36.906063+00', 123);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (318, 'Metacritic', '55/100', '2025-10-19 12:03:36.906075+00', 123);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (319, 'Internet Movie Database', '7.0/10', '2025-10-19 12:03:37.274128+00', 124);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (320, 'Rotten Tomatoes', '72%', '2025-10-19 12:03:37.274148+00', 124);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (321, 'Metacritic', '64/100', '2025-10-19 12:03:37.274158+00', 124);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (322, 'Internet Movie Database', '6.7/10', '2025-10-19 12:03:37.625325+00', 125);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (323, 'Rotten Tomatoes', '78%', '2025-10-19 12:03:37.625345+00', 125);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (324, 'Metacritic', '64/100', '2025-10-19 12:03:37.625356+00', 125);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (325, 'Internet Movie Database', '6.6/10', '2025-10-19 12:03:38.021309+00', 126);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (326, 'Rotten Tomatoes', '72%', '2025-10-19 12:03:38.021331+00', 126);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (327, 'Metacritic', '66/100', '2025-10-19 12:03:38.021343+00', 126);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (328, 'Internet Movie Database', '7.0/10', '2025-10-19 12:03:38.370878+00', 127);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (329, 'Rotten Tomatoes', '72%', '2025-10-19 12:03:38.370898+00', 127);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (330, 'Metacritic', '51/100', '2025-10-19 12:03:38.370911+00', 127);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (331, 'Internet Movie Database', '7.3/10', '2025-10-19 12:03:38.760986+00', 128);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (332, 'Rotten Tomatoes', '68%', '2025-10-19 12:03:38.761007+00', 128);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (333, 'Metacritic', '41/100', '2025-10-19 12:03:38.761017+00', 128);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (334, 'Internet Movie Database', '7.0/10', '2025-10-19 12:03:39.161661+00', 129);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (335, 'Rotten Tomatoes', '85%', '2025-10-19 12:03:39.161684+00', 129);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (336, 'Metacritic', '73/100', '2025-10-19 12:03:39.161695+00', 129);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (337, 'Internet Movie Database', '8.3/10', '2025-10-24 18:54:19.803646+00', 130);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (338, 'Rotten Tomatoes', '98%', '2025-10-24 18:54:19.803673+00', 130);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (339, 'Metacritic', '88/100', '2025-10-24 18:54:19.803685+00', 130);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (340, 'Internet Movie Database', '8.8/10', '2025-10-24 19:36:41.801861+00', 132);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (341, 'Rotten Tomatoes', '92%', '2025-10-24 19:36:41.801892+00', 132);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (342, 'Metacritic', '95/100', '2025-10-24 19:36:41.801907+00', 132);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (343, 'Internet Movie Database', '9.3/10', '2025-10-24 19:36:55.425338+00', 133);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (344, 'Rotten Tomatoes', '89%', '2025-10-24 19:36:55.425359+00', 133);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (345, 'Metacritic', '82/100', '2025-10-24 19:36:55.425369+00', 133);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (346, 'Internet Movie Database', '8.8/10', '2025-10-24 19:36:55.830297+00', 134);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (347, 'Rotten Tomatoes', '75%', '2025-10-24 19:36:55.830318+00', 134);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (348, 'Metacritic', '82/100', '2025-10-24 19:36:55.830329+00', 134);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (349, 'Internet Movie Database', '8.7/10', '2025-10-24 19:36:56.356087+00', 135);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (350, 'Rotten Tomatoes', '93%', '2025-10-24 19:36:56.356104+00', 135);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (351, 'Metacritic', '92/100', '2025-10-24 19:36:56.356115+00', 135);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (352, 'Internet Movie Database', '9.2/10', '2025-10-24 19:36:56.772298+00', 136);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (353, 'Rotten Tomatoes', '97%', '2025-10-24 19:36:56.772324+00', 136);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (354, 'Metacritic', '100/100', '2025-10-24 19:36:56.772337+00', 136);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (355, 'Internet Movie Database', '8.5/10', '2025-10-24 19:36:57.160824+00', 137);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (356, 'Rotten Tomatoes', '99%', '2025-10-24 19:36:57.160848+00', 137);
INSERT INTO public.movie_rating (id, source, value, created_at, movie_id) VALUES (357, 'Metacritic', '100/100', '2025-10-24 19:36:57.160861+00', 137);


--
-- Data for Name: movie_recommendedmovie; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (13, '2025-07-04', '2025-07-04 10:15:07.062+00', 53, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (6, '2025-07-04', '2025-07-04 10:15:07.062+00', 8, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (7, '2025-07-04', '2025-07-04 10:15:07.062+00', 9, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (4, '2025-07-04', '2025-07-04 10:15:07.062+00', 46, 5, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (5, '2025-07-04', '2025-07-04 10:15:07.062+00', 36, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (9, '2025-07-04', '2025-07-04 10:15:07.062+00', 49, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (14, '2025-07-04', '2025-07-04 10:15:07.062+00', 54, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (12, '2025-07-04', '2025-07-04 10:15:07.062+00', 52, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (8, '2025-07-04', '2025-07-04 10:15:07.062+00', 10, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (11, '2025-07-04', '2025-07-04 10:15:07.062+00', 51, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (10, '2025-07-04', '2025-07-04 10:15:07.062+00', 50, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (17, '2025-06-04', '2025-10-04 10:53:20.968167+00', 10, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (23, '2025-06-04', '2025-10-04 10:53:20.96825+00', 55, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (19, '2025-06-04', '2025-10-04 10:53:20.968195+00', 50, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (22, '2025-06-04', '2025-10-04 10:53:20.968237+00', 54, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (21, '2025-06-04', '2025-10-04 10:53:20.968222+00', 53, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (20, '2025-06-04', '2025-10-04 10:53:20.968209+00', 52, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (16, '2025-06-04', '2025-10-04 10:53:20.968151+00', 9, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (18, '2025-06-04', '2025-10-04 10:53:20.968181+00', 49, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (15, '2025-06-04', '2025-10-04 10:53:20.968123+00', 36, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (24, '2025-06-04', '2025-10-04 10:53:20.968264+00', 56, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (25, '2025-10-04', '2025-10-04 10:55:13.007885+00', 8, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (26, '2025-10-04', '2025-10-04 10:55:13.007915+00', 9, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (27, '2025-10-04', '2025-10-04 10:55:13.007931+00', 10, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (28, '2025-10-04', '2025-10-04 10:55:13.007947+00', 49, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (29, '2025-10-04', '2025-10-04 10:55:13.007961+00', 52, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (30, '2025-10-04', '2025-10-04 10:55:13.007976+00', 53, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (31, '2025-10-04', '2025-10-04 10:55:13.00799+00', 54, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (32, '2025-10-04', '2025-10-04 10:55:13.008005+00', 57, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (33, '2025-10-04', '2025-10-04 10:55:13.00802+00', 58, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (34, '2025-10-04', '2025-10-04 10:55:13.008035+00', 59, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (35, '2025-10-19', '2025-10-19 11:04:50.044567+00', 68, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (36, '2025-10-19', '2025-10-19 11:04:50.044597+00', 69, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (37, '2025-10-19', '2025-10-19 11:04:50.044616+00', 70, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (38, '2025-10-19', '2025-10-19 11:04:50.044636+00', 71, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (39, '2025-10-19', '2025-10-19 11:04:50.044652+00', 8, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (40, '2025-10-19', '2025-10-19 11:04:50.044668+00', 9, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (41, '2025-10-19', '2025-10-19 11:04:50.044683+00', 10, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (42, '2025-10-19', '2025-10-19 11:04:50.044698+00', 72, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (43, '2025-10-19', '2025-10-19 11:04:50.044712+00', 73, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (44, '2025-10-19', '2025-10-19 11:04:50.044727+00', 53, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (45, '2025-10-24', '2025-10-24 18:54:20.388623+00', 1, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (46, '2025-10-24', '2025-10-24 18:54:20.388652+00', 130, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (47, '2025-10-24', '2025-10-24 18:54:20.388669+00', 131, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (48, '2025-10-24', '2025-10-24 18:54:20.388685+00', 36, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (49, '2025-10-24', '2025-10-24 18:54:20.388699+00', 8, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (50, '2025-10-24', '2025-10-24 18:54:20.388713+00', 9, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (51, '2025-10-24', '2025-10-24 18:54:20.388727+00', 60, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (52, '2025-10-24', '2025-10-24 18:54:20.388741+00', 61, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (53, '2025-10-24', '2025-10-24 18:54:20.388754+00', 62, 1, NULL, true);
INSERT INTO public.movie_recommendedmovie (id, recommendation_date, created_at, movie_id, user_id, deactivated_at, is_active) VALUES (54, '2025-10-24', '2025-10-24 18:54:20.388768+00', 63, 1, NULL, true);


--
-- Data for Name: movie_watchlatermovie; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movie_watchlatermovie (id, created_at, updated_at, movie_id, user_id) VALUES (1, '2025-09-14 13:21:09.272855+00', '2025-09-14 13:21:09.272877+00', 11, 1);
INSERT INTO public.movie_watchlatermovie (id, created_at, updated_at, movie_id, user_id) VALUES (5, '2025-10-04 10:07:43.191135+00', '2025-10-04 10:07:43.191147+00', 47, 5);
INSERT INTO public.movie_watchlatermovie (id, created_at, updated_at, movie_id, user_id) VALUES (7, '2025-10-19 11:06:24.294107+00', '2025-10-19 11:06:24.294127+00', 4, 1);
INSERT INTO public.movie_watchlatermovie (id, created_at, updated_at, movie_id, user_id) VALUES (8, '2025-10-24 18:56:21.515819+00', '2025-10-24 18:56:21.515844+00', 3, 1);


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 1, false);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_app_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_app_user_groups_id_seq', 1, false);


--
-- Name: auth_app_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_app_user_id_seq', 5, true);


--
-- Name: auth_app_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_app_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 100, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 25, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 51, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: movie_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_actor_id_seq', 333, true);


--
-- Name: movie_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_country_id_seq', 21, true);


--
-- Name: movie_director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_director_id_seq', 140, true);


--
-- Name: movie_genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_genre_id_seq', 19, true);


--
-- Name: movie_language_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_language_id_seq', 39, true);


--
-- Name: movie_likemovie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_likemovie_id_seq', 6, true);


--
-- Name: movie_movie_actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_actors_id_seq', 404, true);


--
-- Name: movie_movie_countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_countries_id_seq', 213, true);


--
-- Name: movie_movie_directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_directors_id_seq', 175, true);


--
-- Name: movie_movie_genres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_genres_id_seq', 347, true);


--
-- Name: movie_movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_id_seq', 137, true);


--
-- Name: movie_movie_languages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_languages_id_seq', 287, true);


--
-- Name: movie_movie_writers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_movie_writers_id_seq', 298, true);


--
-- Name: movie_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_rating_id_seq', 357, true);


--
-- Name: movie_recommendedmovie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_recommendedmovie_id_seq', 54, true);


--
-- Name: movie_watchlatermovie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_watchlatermovie_id_seq', 8, true);


--
-- Name: movie_writer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movie_writer_id_seq', 240, true);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict JOOOFm2RnEaf1F019WJSYViwYkK9lweUobCrE1EzrtWGvRVgh3LMzrLSdCrG7xn

