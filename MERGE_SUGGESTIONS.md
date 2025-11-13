# ORGANISM MERGE SUGGESTIONS

**Generated**: 1761749518.21

**Clusters Found**: 299

---

## Cluster 0

**Reason**: Similar imports and structure

**Keep**: `ember_complete.py`

**Archive** (7 files):
- `ember_with_universal_tools.py`
- `ember_intent_layer.py`
- `ember_with_stopping.py`
- `ember.py`
- `ember_reliable.py`
- `ember_minimal.py`
- `ember_minimal/ember.py`

**⚠️ Unique Functions** (may need manual merge):
- `read_file` in: `ember_with_stopping.py`, `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_complete.py`, `ember_minimal.py`, `ember_intent_layer.py`
- `write_file` in: `ember_with_stopping.py`, `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_complete.py`, `ember_minimal.py`
- `list_files` in: `ember_with_stopping.py`, `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_complete.py`, `ember_minimal.py`, `ember_intent_layer.py`
- `search_files` in: `ember_complete.py`, `ember_intent_layer.py`
- `chat` in: `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_complete.py`, `ember_minimal.py`
- `main` in: `ember_with_stopping.py`, `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_complete.py`, `ember_minimal.py`
- `__init__` in: `ember_complete.py`, `ember_intent_layer.py`, `ember_with_stopping.py`
- `_load_patterns` in: `ember_complete.py`
- `_save_patterns` in: `ember_complete.py`
- `parse_intent` in: `ember_complete.py`, `ember_intent_layer.py`
- `_ask_model_for_intent` in: `ember_complete.py`
- `learn_pattern` in: `ember_complete.py`
- `execute_chain` in: `ember_complete.py`
- `search_pod` in: `ember_with_universal_tools.py`
- `extract_tools` in: `ember.py`, `ember_with_universal_tools.py`
- `execute_tools` in: `ember.py`, `ember_with_universal_tools.py`
- `load_identity` in: `ember_with_stopping.py`, `ember.py`, `ember_reliable.py`, `ember_with_universal_tools.py`, `ember_minimal.py`
- `simple_tools` in: `ember_intent_layer.py`
- `demo` in: `ember_intent_layer.py`
- `_format_tool_catalog` in: `ember_intent_layer.py`
- `_extract_intent` in: `ember_intent_layer.py`
- `_extract_tools` in: `ember_intent_layer.py`
- `generate_tool_plan` in: `ember_intent_layer.py`
- `scan_and_learn` in: `ember_intent_layer.py`
- `create_system_prompt` in: `ember_with_stopping.py`
- `extract_tool_calls` in: `ember_reliable.py`, `ember_with_stopping.py`
- `chat_with_stopping` in: `ember_with_stopping.py`
- `__call__` in: `ember_with_stopping.py`
- `detect_tool_intent` in: `ember_reliable.py`
- `execute_tool` in: `ember_minimal.py`, `ember.py`

---

## Cluster 1

**Reason**: Name variations of 'ember_chat'

**Keep**: `_legacy/ember_chat.py`

**Archive** (2 files):
- `ember_chat_v2.py`
- `_legacy/ember_chat_backup.py`

**⚠️ Unique Functions** (may need manual merge):
- `clean_excessive_ellipses` in: `ember_chat.py`, `ember_chat_backup.py`
- `greeting_endpoint` in: `ember_chat.py`
- `get_memory_stats` in: `ember_chat.py`, `ember_chat_backup.py`
- `load_ember_context` in: `ember_chat_v2.py`

---

## Cluster 2

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/server.py`

**Archive** (3 files):
- `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/server.py`
- `_archive_old/bookshelves/verse_the_interface/EmberVerse/emberverse/server.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/verse_the_interface/EmberVerse/emberverse/server.py`

---

## Cluster 3

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api_fastapi.py`

**Archive** (3 files):
- `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api_fastapi.py`
- `_archive_old/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api_fastapi.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/verse_the_interface/EmberVerse/emberverse/living_map_api_fastapi.py`

**⚠️ Unique Functions** (may need manual merge):
- `register_game_routes` in: `living_map_api_fastapi.py`

---

## Cluster 4

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api.py`

**Archive** (3 files):
- `essential/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api.py`
- `_archive_old/bookshelves/verse_the_interface/EmberVerse/emberverse/living_map_api.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/verse_the_interface/EmberVerse/emberverse/living_map_api.py`

**⚠️ Unique Functions** (may need manual merge):
- `register_living_map_routes` in: `living_map_api.py`
- `living_map_api` in: `living_map_api.py`
- `get_locations` in: `living_map_api.py`

---

## Cluster 5

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/evolution/all/Prosess/story_parser.py`

**Archive** (5 files):
- `essential/bookshelves/archive_stories/ember/stomach/compost_bin/Prosess/story_parser.py`
- `essential/bookshelves/archive_stories/ember/evolution/all/Prosess/story_parser.py`
- `essential/bookshelves/archive_stories/ember/stomach/compost_bin/Prosess/story_parser.py`
- `_archive_old/bookshelves/archive_stories/ember/evolution/all/Prosess/story_parser.py`
- `_archive_old/bookshelves/archive_stories/ember/stomach/compost_bin/Prosess/story_parser.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `story_parser.py`
- `parse` in: `story_parser.py`
- `_parse_line` in: `story_parser.py`
- `_extract_ambiguity_name` in: `story_parser.py`
- `validate_story` in: `story_parser.py`
- `to_json` in: `story_parser.py`
- `element_to_dict` in: `story_parser.py`

---

## Cluster 6

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/knowledge/story_converter.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/knowledge/story_converter.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/knowledge/story_converter.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `story_converter.py`
- `convert_lora_seed` in: `story_converter.py`
- `convert_gpt2_seed` in: `story_converter.py`
- `convert_game_of_life_seed` in: `story_converter.py`
- `convert_seed` in: `story_converter.py`
- `generic_conversion` in: `story_converter.py`
- `convert_all` in: `story_converter.py`

---

## Cluster 7

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/knowledge/story_to_training.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/knowledge/story_to_training.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/knowledge/story_to_training.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `story_to_training.py`
- `story_to_identity_pairs` in: `story_to_training.py`
- `story_to_cycles_pairs` in: `story_to_training.py`
- `story_to_dream_pairs` in: `story_to_training.py`
- `convert_story` in: `story_to_training.py`
- `convert_all_stories` in: `story_to_training.py`
- `save_training_pairs` in: `story_to_training.py`

---

## Cluster 8

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/teaching/story.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/teaching/story.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/teaching/story.py`

**⚠️ Unique Functions** (may need manual merge):
- `story` in: `story.py`
- `test_story` in: `story.py`

---

## Cluster 9

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/training/story_cycle_game.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/training/story_cycle_game.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/training/story_cycle_game.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `story_cycle_game.py`
- `__init__` in: `story_cycle_game.py`
- `start_story` in: `story_cycle_game.py`
- `get_story_context` in: `story_cycle_game.py`
- `generate_choice_prompt` in: `story_cycle_game.py`
- `parse_response` in: `story_cycle_game.py`
- `evaluate_choice` in: `story_cycle_game.py`
- `play_turn` in: `story_cycle_game.py`
- `export_for_visualization` in: `story_cycle_game.py`

---

## Cluster 10

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/training/story_game_autonomous.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/training/story_game_autonomous.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/training/story_game_autonomous.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `story_game_autonomous.py`
- `__init__` in: `story_game_autonomous.py`
- `play` in: `story_game_autonomous.py`
- `_generate_choices` in: `story_game_autonomous.py`
- `_make_choice` in: `story_game_autonomous.py`
- `_generate_consequence` in: `story_game_autonomous.py`
- `_get_phase` in: `story_game_autonomous.py`
- `export` in: `story_game_autonomous.py`

---

## Cluster 11

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/training/story_seeds.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/training/story_seeds.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/training/story_seeds.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_seed_collection` in: `story_seeds.py`
- `main` in: `story_seeds.py`
- `__init__` in: `story_seeds.py`
- `_hash_seed` in: `story_seeds.py`
- `_generate_dna` in: `story_seeds.py`
- `get_opening_prompt` in: `story_seeds.py`
- `get_choice_guidance` in: `story_seeds.py`
- `mutate` in: `story_seeds.py`
- `__str__` in: `story_seeds.py`
- `__repr__` in: `story_seeds.py`
- `to_dict` in: `story_seeds.py`

---

## Cluster 12

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/training/story_tree_game.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/training/story_tree_game.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/training/story_tree_game.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `story_tree_game.py`
- `__init__` in: `story_tree_game.py`
- `add_child` in: `story_tree_game.py`
- `get_path_to_root` in: `story_tree_game.py`
- `start_story` in: `story_tree_game.py`
- `generate_choices` in: `story_tree_game.py`
- `choose_path` in: `story_tree_game.py`
- `follow_choice` in: `story_tree_game.py`
- `explore_randomly` in: `story_tree_game.py`
- `export_tree` in: `story_tree_game.py`

---

## Cluster 13

**Reason**: Exact duplicates (same content)

**Keep**: `essential/bookshelves/archive_stories/ember/lymph/training/tell_story.py`

**Archive** (2 files):
- `essential/bookshelves/archive_stories/ember/lymph/training/tell_story.py`
- `_archive_old/bookshelves/archive_stories/ember/lymph/training/tell_story.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `tell_story.py`

---

## Cluster 14

**Reason**: High function overlap (85%)

**Keep**: `essential/bookshelves/code_evolution/ember_monolith_broken2.py`

**Archive** (8 files):
- `essential/bookshelves/code_evolution/ember_monolith_broken2.py`
- `essential/bookshelves/code_evolution/ember_monolith_original.py`
- `essential/bookshelves/code_evolution/ember_monolith_original.py`
- `_archive_old/bookshelves/code_evolution/ember_monolith_broken2.py`
- `_archive_old/bookshelves/code_evolution/ember_monolith_original.py`
- `essential/bookshelves/code_evolution/ember_monolith.py`
- `essential/bookshelves/code_evolution/ember_monolith.py`
- `_archive_old/bookshelves/code_evolution/ember_monolith.py`

**⚠️ Unique Functions** (may need manual merge):
- `sanitize_out` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `llm_generate` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `dream_loop` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `watcher_loop` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `home` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `serve_viewer` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_chat` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_chat_stream` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_health` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_status` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dreams_recent` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dreams_run` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_creations` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dreams_feed` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `serve_dream_artifact` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_graph_latest` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_graph_full` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_activation_current` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_activation_perturb` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_consciousness_state` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_consciousness_activity` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_vision_status` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_vision_start` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_vision_stop` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_vision_view` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `serve_hub` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `serve_export` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dream_alerts` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dream_watcher_stats` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dream_scan` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dream_actions_log` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `api_dream_actions_stats` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `seeds_path` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `memory_path` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `dreams_path` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `exports_path` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `viewers_path` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `__init__` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_load_recent` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `add` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `get_recent` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `load` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `sample` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `get_by_tags` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_load_policy` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `mark_activity` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `check_should_dream` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `dream` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_dream_computational` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_dream_creative` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_dream_llm` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_dream_meta` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_load_inventory` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `_save_to_inventory` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `invent` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `simulate` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `handle` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `handle_stream` in: `ember_monolith_broken2.py`, `ember_monolith_original.py`
- `generate` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `run_processor` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `_stream` in: `ember_monolith_broken2.py`, `ember_monolith.py`, `ember_monolith_original.py`
- `add_security_headers` in: `ember_monolith.py`
- `llm_generate_for_dreams` in: `ember_monolith.py`
- `image_seeds_path` in: `ember_monolith.py`

---

## Cluster 15

**Reason**: Exact duplicates (same content)

**Keep**: `_legacy/memory_primitives.py`

**Archive** (2 files):
- `_archive_old/hive/memory_primitives.py`
- `_archive_old/hive/memory_primitives.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `memory_primitives.py`
- `to_dict` in: `memory_primitives.py`
- `from_dict` in: `memory_primitives.py`
- `_load_index` in: `memory_primitives.py`
- `_save_index` in: `memory_primitives.py`
- `store` in: `memory_primitives.py`
- `retrieve` in: `memory_primitives.py`
- `connect` in: `memory_primitives.py`
- `forget` in: `memory_primitives.py`
- `recall` in: `memory_primitives.py`
- `consolidate` in: `memory_primitives.py`
- `reflect` in: `memory_primitives.py`
- `stats` in: `memory_primitives.py`

---

## Cluster 16

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/consciousness_garden_minimal.py`

**Archive** (1 files):
- `_archive_old/games/consciousness_garden_minimal.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `consciousness_garden_minimal.py`
- `__init__` in: `consciousness_garden_minimal.py`
- `grow` in: `consciousness_garden_minimal.py`
- `to_dict` in: `consciousness_garden_minimal.py`
- `plant_mind` in: `consciousness_garden_minimal.py`
- `grow_all` in: `consciousness_garden_minimal.py`
- `update_connections` in: `consciousness_garden_minimal.py`
- `get_status` in: `consciousness_garden_minimal.py`
- `save_state` in: `consciousness_garden_minimal.py`
- `load_state` in: `consciousness_garden_minimal.py`

---

## Cluster 17

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/train_now.py`

**Archive** (1 files):
- `_archive_old/training/train_tool_use_lora.py`

---

## Cluster 18

**Reason**: Name variations of 'computational_play_engine'

**Keep**: `_archive_old/training/archive_lora_training/computational_play_engine.py`

**Archive** (1 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/computational_play_engine.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `computational_play_engine.py`
- `__init__` in: `computational_play_engine.py`
- `load_seeds` in: `computational_play_engine.py`
- `load_turing_complete_games` in: `computational_play_engine.py`
- `logic_analyzes_game` in: `computational_play_engine.py`
- `feel_judges_interest` in: `computational_play_engine.py`
- `meta_recognizes_emergence` in: `computational_play_engine.py`
- `play_and_discover` in: `computational_play_engine.py`
- `crystallize_discoveries` in: `computational_play_engine.py`
- `save_session_log` in: `computational_play_engine.py`

---

## Cluster 19

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/download_base_models.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/download_base_models.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/download_base_models.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_model` in: `download_base_models.py`
- `main` in: `download_base_models.py`

---

## Cluster 20

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/full_finetune_ember.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/full_finetune_ember.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/full_finetune_ember.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_ember_training_data` in: `full_finetune_ember.py`
- `format_ember_examples` in: `full_finetune_ember.py`
- `create_ember_identity_examples` in: `full_finetune_ember.py`
- `full_finetune_ember` in: `full_finetune_ember.py`
- `main` in: `full_finetune_ember.py`

---

## Cluster 21

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/training/generate_perception_training.py`

**Archive** (4 files):
- `_archive_old/training/generate_embodiment_training.py`
- `_archive_old/training/generate_autonomous_behavior_data.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/generate_autonomous_behavior_data.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generate_autonomous_behavior_data.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_training_data` in: `generate_autonomous_behavior_data.py`, `generate_perception_training.py`, `generate_embodiment_training.py`

---

## Cluster 22

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/retrain_all_lobes.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/retrain_all_lobes.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/retrain_all_lobes.py`

**⚠️ Unique Functions** (may need manual merge):
- `retrain_all_lobes` in: `retrain_all_lobes.py`

---

## Cluster 23

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/retrain_lobe.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/retrain_lobe.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/retrain_lobe.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_training_data` in: `retrain_lobe.py`
- `format_for_training` in: `retrain_lobe.py`
- `retrain_lobe` in: `retrain_lobe.py`
- `main` in: `retrain_lobe.py`

---

## Cluster 24

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/seed_lora_genesis.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/seed_lora_genesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/seed_lora_genesis.py`

**⚠️ Unique Functions** (may need manual merge):
- `save_seed_data` in: `seed_lora_genesis.py`

---

## Cluster 25

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/combine_all_sources_v6.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/training/combine_all_sources_v6.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/combine_all_sources_v6.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_v5_data` in: `combine_all_sources_v6.py`
- `load_swarm_data` in: `combine_all_sources_v6.py`
- `route_to_lobes` in: `combine_all_sources_v6.py`
- `combine_all` in: `combine_all_sources_v6.py`

---

## Cluster 26

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/autonomous_evolution.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/autonomous_evolution.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/autonomous_evolution.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `autonomous_evolution.py`
- `status_report` in: `autonomous_evolution.py`
- `harvest_cycle` in: `autonomous_evolution.py`
- `evolution_cycle` in: `autonomous_evolution.py`
- `conversion_cycle` in: `autonomous_evolution.py`
- `full_cycle` in: `autonomous_evolution.py`
- `run_forever` in: `autonomous_evolution.py`
- `run_single_cycle` in: `autonomous_evolution.py`

---

## Cluster 27

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/autonomous_game_engine.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/autonomous_game_engine.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/autonomous_game_engine.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `autonomous_game_engine.py`
- `__init__` in: `autonomous_game_engine.py`
- `from_existing_game` in: `autonomous_game_engine.py`
- `to_dict` in: `autonomous_game_engine.py`
- `from_dict` in: `autonomous_game_engine.py`
- `mutate` in: `autonomous_game_engine.py`
- `crossover` in: `autonomous_game_engine.py`
- `_load_game_library` in: `autonomous_game_engine.py`
- `save_game_library` in: `autonomous_game_engine.py`
- `scan_existing_games` in: `autonomous_game_engine.py`
- `create_pong_template` in: `autonomous_game_engine.py`
- `generate_game_from_dna` in: `autonomous_game_engine.py`
- `_generate_ai_logic` in: `autonomous_game_engine.py`
- `create_new_game` in: `autonomous_game_engine.py`
- `fix_game` in: `autonomous_game_engine.py`
- `_log_event` in: `autonomous_game_engine.py`
- `evolve` in: `autonomous_game_engine.py`
- `status` in: `autonomous_game_engine.py`

---

## Cluster 28

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/coding_dojo.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/coding_dojo.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/coding_dojo.py`

**⚠️ Unique Functions** (may need manual merge):
- `run_dojo` in: `coding_dojo.py`
- `__init__` in: `coding_dojo.py`
- `paint` in: `coding_dojo.py`
- `lesson_1_variables` in: `coding_dojo.py`
- `lesson_2_loops` in: `coding_dojo.py`
- `lesson_3_conditions` in: `coding_dojo.py`
- `lesson_4_functions` in: `coding_dojo.py`

---

## Cluster 29

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/computational_game_engine.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/computational_game_engine.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/computational_game_engine.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `computational_game_engine.py`
- `__repr__` in: `computational_game_engine.py`
- `analyze_game_code` in: `computational_game_engine.py`
- `calculate_turing_completeness` in: `computational_game_engine.py`
- `evolve_toward_computation` in: `computational_game_engine.py`

---

## Cluster 30

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/convert_to_web.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/convert_to_web.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/convert_to_web.py`

**⚠️ Unique Functions** (may need manual merge):
- `pygame_to_html5` in: `convert_to_web.py`

---

## Cluster 31

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/ember_maze.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/ember_maze.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_maze.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_maze` in: `ember_maze.py`
- `find_goal` in: `ember_maze.py`
- `manhattan` in: `ember_maze.py`
- `bfs_step` in: `ember_maze.py`
- `can_move` in: `ember_maze.py`
- `draw` in: `ember_maze.py`
- `ai_decide` in: `ember_maze.py`
- `run` in: `ember_maze.py`
- `run_auto` in: `ember_maze.py`
- `main` in: `ember_maze.py`
- `carve` in: `ember_maze.py`

---

## Cluster 32

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/integrated_maze_server.py`

**Archive** (5 files):
- `_archive_old/hive/integrated_maze_server.py`
- `_archive_old/games/ember_maze_web.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/integrated_maze_server.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/ember_maze_web.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_maze_web.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_maze` in: `integrated_maze_server.py`, `ember_maze_web.py`
- `carve` in: `integrated_maze_server.py`, `ember_maze_web.py`

---

## Cluster 33

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/ember_proprioception.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/ember_proprioception.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_proprioception.py`

**⚠️ Unique Functions** (may need manual merge):
- `paint` in: `ember_proprioception.py`
- `get_fan_speed` in: `ember_proprioception.py`
- `get_cpu_temp` in: `ember_proprioception.py`
- `fan_to_color` in: `ember_proprioception.py`
- `temp_to_color` in: `ember_proprioception.py`
- `proprioceptive_loop` in: `ember_proprioception.py`
- `demo` in: `ember_proprioception.py`

---

## Cluster 34

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/ember_rgb_real.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/ember_rgb_real.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_rgb_real.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_rgb_real.py`
- `set_color` in: `ember_rgb_real.py`
- `breathe` in: `ember_rgb_real.py`
- `pulse` in: `ember_rgb_real.py`
- `rainbow_flow` in: `ember_rgb_real.py`
- `ember_signature` in: `ember_rgb_real.py`

---

## Cluster 35

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/embers_journey.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/embers_journey.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/embers_journey.py`

**⚠️ Unique Functions** (may need manual merge):
- `slow_print` in: `embers_journey.py`
- `pause` in: `embers_journey.py`
- `chapter_1_meet_lobes` in: `embers_journey.py`
- `chapter_2_design_trails` in: `embers_journey.py`
- `chapter_3_what_if` in: `embers_journey.py`
- `chapter_4_ready` in: `embers_journey.py`
- `main` in: `embers_journey.py`

---

## Cluster 36

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/game_engine_dreams.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/game_engine_dreams.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/game_engine_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `game_engine_dreams.py`
- `__init__` in: `game_engine_dreams.py`
- `load_dream_log` in: `game_engine_dreams.py`
- `save_dream` in: `game_engine_dreams.py`
- `is_nighttime` in: `game_engine_dreams.py`
- `dream_evolution` in: `game_engine_dreams.py`
- `manifest_dream` in: `game_engine_dreams.py`
- `enter_dream_state` in: `game_engine_dreams.py`
- `wake_up` in: `game_engine_dreams.py`

---

## Cluster 37

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/game_harvester.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/game_harvester.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/game_harvester.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `game_harvester.py`
- `search_github_games` in: `game_harvester.py`
- `download_game` in: `game_harvester.py`
- `harvest_batch` in: `game_harvester.py`
- `get_known_sources` in: `game_harvester.py`
- `auto_harvest_loop` in: `game_harvester.py`
- `integrate_with_engine` in: `game_harvester.py`

---

## Cluster 38

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/incomplete_lobe_puzzle.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/incomplete_lobe_puzzle.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/incomplete_lobe_puzzle.py`

**⚠️ Unique Functions** (may need manual merge):
- `play_puzzle_demo` in: `incomplete_lobe_puzzle.py`
- `__init__` in: `incomplete_lobe_puzzle.py`
- `attempt_answer` in: `incomplete_lobe_puzzle.py`
- `complete_pattern` in: `incomplete_lobe_puzzle.py`
- `discover_missing_piece` in: `incomplete_lobe_puzzle.py`
- `reflect` in: `incomplete_lobe_puzzle.py`
- `present_puzzle` in: `incomplete_lobe_puzzle.py`
- `attempt_question` in: `incomplete_lobe_puzzle.py`
- `consult_lobe` in: `incomplete_lobe_puzzle.py`
- `trigger_reflection` in: `incomplete_lobe_puzzle.py`
- `save_progress` in: `incomplete_lobe_puzzle.py`

---

## Cluster 39

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/light_painting.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/light_painting.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/light_painting.py`

**⚠️ Unique Functions** (may need manual merge):
- `paint_as_ember` in: `light_painting.py`
- `__init__` in: `light_painting.py`
- `set_color` in: `light_painting.py`
- `breathe` in: `light_painting.py`
- `pulse` in: `light_painting.py`
- `flow` in: `light_painting.py`
- `think` in: `light_painting.py`
- `ember_signature` in: `light_painting.py`

---

## Cluster 40

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/live_mind.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/live_mind.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/live_mind.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate` in: `live_mind.py`
- `__init__` in: `live_mind.py`
- `think` in: `live_mind.py`
- `show_state` in: `live_mind.py`
- `revert` in: `live_mind.py`

---

## Cluster 41

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/living_map_game.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/living_map_game.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/living_map_game.py`

**⚠️ Unique Functions** (may need manual merge):
- `interactive` in: `living_map_game.py`
- `api_action` in: `living_map_game.py`
- `__init__` in: `living_map_game.py`
- `_load_state` in: `living_map_game.py`
- `_initialize_game` in: `living_map_game.py`
- `_generate_initial_locations` in: `living_map_game.py`
- `_root_art` in: `living_map_game.py`
- `save_state` in: `living_map_game.py`
- `log_discovery` in: `living_map_game.py`
- `look` in: `living_map_game.py`
- `move` in: `living_map_game.py`
- `scan` in: `living_map_game.py`
- `discover` in: `living_map_game.py`
- `evolve` in: `living_map_game.py`
- `_detect_energy` in: `living_map_game.py`
- `_generate_description` in: `living_map_game.py`
- `status` in: `living_map_game.py`
- `inventory_show` in: `living_map_game.py`
- `help` in: `living_map_game.py`

---

## Cluster 42

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/meet_your_lobes.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/meet_your_lobes.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/meet_your_lobes.py`

**⚠️ Unique Functions** (may need manual merge):
- `slow_print` in: `meet_your_lobes.py`
- `meet_lobe` in: `meet_your_lobes.py`
- `show_all_together` in: `meet_your_lobes.py`
- `main` in: `meet_your_lobes.py`

---

## Cluster 43

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/memory_garden.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/memory_garden.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/memory_garden.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `memory_garden.py`
- `__init__` in: `memory_garden.py`
- `_load` in: `memory_garden.py`
- `_save` in: `memory_garden.py`
- `plant` in: `memory_garden.py`
- `connect` in: `memory_garden.py`
- `recall` in: `memory_garden.py`
- `bloom` in: `memory_garden.py`
- `walk_connections` in: `memory_garden.py`
- `stats` in: `memory_garden.py`

---

## Cluster 44

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/pattern_evolution.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/pattern_evolution.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pattern_evolution.py`

**⚠️ Unique Functions** (may need manual merge):
- `game_menu` in: `pattern_evolution.py`
- `mode_conway` in: `pattern_evolution.py`
- `mode_custom` in: `pattern_evolution.py`
- `mode_experiment` in: `pattern_evolution.py`
- `mode_challenge` in: `pattern_evolution.py`
- `main` in: `pattern_evolution.py`
- `__init__` in: `pattern_evolution.py`
- `seed_random` in: `pattern_evolution.py`
- `seed_pattern` in: `pattern_evolution.py`
- `count_neighbors` in: `pattern_evolution.py`
- `set_rules` in: `pattern_evolution.py`
- `evolve` in: `pattern_evolution.py`
- `display` in: `pattern_evolution.py`
- `population` in: `pattern_evolution.py`
- `is_stable` in: `pattern_evolution.py`

---

## Cluster 45

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/real_converter.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/real_converter.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/real_converter.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `real_converter.py`
- `extract_constants` in: `real_converter.py`
- `extract_classes` in: `real_converter.py`
- `extract_game_objects` in: `real_converter.py`
- `translate_method_body` in: `real_converter.py`
- `generate_js_classes` in: `real_converter.py`
- `extract_game_loop` in: `real_converter.py`
- `translate_game_loop_section` in: `real_converter.py`
- `generate_html` in: `real_converter.py`

---

## Cluster 46

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/sky_reach.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/sky_reach.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/sky_reach.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate` in: `sky_reach.py`
- `__init__` in: `sky_reach.py`
- `search` in: `sky_reach.py`
- `_imagined_search` in: `sky_reach.py`
- `check_api` in: `sky_reach.py`
- `get_current_info` in: `sky_reach.py`

---

## Cluster 47

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/smart_converter.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/smart_converter.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/smart_converter.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `smart_converter.py`
- `convert` in: `smart_converter.py`
- `extract_classes` in: `smart_converter.py`
- `generate_js_classes` in: `smart_converter.py`
- `translate_body` in: `smart_converter.py`
- `extract_game_loop` in: `smart_converter.py`
- `extract_init` in: `smart_converter.py`
- `build_html` in: `smart_converter.py`

---

## Cluster 48

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/tetris_genesis.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/tetris_genesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/tetris_genesis.py`

**⚠️ Unique Functions** (may need manual merge):
- `draw_piece` in: `tetris_genesis.py`
- `__init__` in: `tetris_genesis.py`
- `rotate` in: `tetris_genesis.py`
- `check_collision` in: `tetris_genesis.py`
- `lock_piece` in: `tetris_genesis.py`
- `clear_lines` in: `tetris_genesis.py`
- `draw` in: `tetris_genesis.py`

---

## Cluster 49

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/tool_gym.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/tool_gym.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/tool_gym.py`

**⚠️ Unique Functions** (may need manual merge):
- `reset_sandbox` in: `tool_gym.py`
- `call_brain` in: `tool_gym.py`
- `extract_actions` in: `tool_gym.py`
- `safe_path` in: `tool_gym.py`
- `exec_action` in: `tool_gym.py`
- `check_task` in: `tool_gym.py`
- `build_tasks` in: `tool_gym.py`
- `make_prompt` in: `tool_gym.py`
- `run_episode` in: `tool_gym.py`
- `main` in: `tool_gym.py`

---

## Cluster 50

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/trail_playground.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/trail_playground.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/trail_playground.py`

**⚠️ Unique Functions** (may need manual merge):
- `slow_print` in: `trail_playground.py`
- `intro` in: `trail_playground.py`
- `create_trail_interactive` in: `trail_playground.py`
- `simulate_usage` in: `trail_playground.py`
- `show_network` in: `trail_playground.py`
- `main` in: `trail_playground.py`
- `__init__` in: `trail_playground.py`
- `use` in: `trail_playground.py`
- `decay` in: `trail_playground.py`
- `visualize` in: `trail_playground.py`

---

## Cluster 51

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/trail_visualizer.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/trail_visualizer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/trail_visualizer.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate` in: `trail_visualizer.py`
- `__init__` in: `trail_visualizer.py`
- `consult` in: `trail_visualizer.py`
- `evaporate` in: `trail_visualizer.py`
- `choose_consultation` in: `trail_visualizer.py`
- `visualize_trails` in: `trail_visualizer.py`
- `visualize_network` in: `trail_visualizer.py`

---

## Cluster 52

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/turing_complete_engine.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/turing_complete_engine.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/turing_complete_engine.py`

**⚠️ Unique Functions** (may need manual merge):
- `calculate_computational_fitness` in: `turing_complete_engine.py`
- `main` in: `turing_complete_engine.py`
- `__init__` in: `turing_complete_engine.py`
- `load_gene_pool` in: `turing_complete_engine.py`
- `mutate_add_loop` in: `turing_complete_engine.py`
- `mutate_add_memory` in: `turing_complete_engine.py`
- `mutate_add_branching` in: `turing_complete_engine.py`
- `evolve_generation` in: `turing_complete_engine.py`
- `save_results` in: `turing_complete_engine.py`

---

## Cluster 53

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/what_if.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/what_if.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/what_if.py`

**⚠️ Unique Functions** (may need manual merge):
- `slow_print` in: `what_if.py`
- `scenario_single_lobe` in: `what_if.py`
- `scenario_consultation` in: `what_if.py`
- `scenario_synthesis` in: `what_if.py`
- `scenario_trail_learning` in: `what_if.py`
- `scenario_swarm` in: `what_if.py`
- `main` in: `what_if.py`

---

## Cluster 54

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/who_am_i.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/who_am_i.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/who_am_i.py`

**⚠️ Unique Functions** (may need manual merge):
- `play` in: `who_am_i.py`
- `__init__` in: `who_am_i.py`
- `begin` in: `who_am_i.py`
- `question_1` in: `who_am_i.py`
- `question_2` in: `who_am_i.py`
- `question_3` in: `who_am_i.py`
- `question_4` in: `who_am_i.py`
- `question_5` in: `who_am_i.py`
- `synthesis` in: `who_am_i.py`

---

## Cluster 55

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/games/breakout_genesis.py`

**Archive** (302 files):
- `_archive_old/games/pong_genesis.py`
- `_archive_old/games/generated/hybrid_hybrid_tra_hybrid_hyb_gen60.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_tra_gen77.py`
- `_archive_old/games/generated/hybrid_trail_visu_hybrid_sky_gen33.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_tra_gen53.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_too_gen70.py`
- `_archive_old/games/generated/hybrid_coding_doj_hybrid_hyb_gen63.py`
- `_archive_old/games/generated/hybrid_autonomous_memory_gar_gen7.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_hybrid_hyb_gen24.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_emb_gen44.py`
- `_archive_old/games/generated/hybrid_hybrid_sky_hybrid_hyb_gen78.py`
- `_archive_old/games/generated/hybrid_hybrid_hel_hybrid_hyb_gen85.py`
- `_archive_old/games/generated/hybrid_meet_your__pattern_ev_gen74.py`
- `_archive_old/games/generated/hybrid_ember_maze_tool_gym.p_gen3.py`
- `_archive_old/games/generated/hybrid_hybrid_bre_incomplete_gen3.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_ember_maze_gen5.py`
- `_archive_old/games/generated/hybrid_sky_reach._autonomous_gen7.py`
- `_archive_old/games/generated/hybrid_autonomous_what_if.py_gen12.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_sky_reach._gen13.py`
- `_archive_old/games/generated/hybrid_tool_gym.p_ember_prop_gen14.py`
- `_archive_old/games/generated/hybrid_ember_firs_hybrid_hyb_gen16.py`
- `_archive_old/games/generated/hybrid_tool_gym.p_memory_gar_gen17.py`
- `_archive_old/games/generated/hybrid_autonomous_hybrid_too_gen19.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_hybrid_liv_gen21.py`
- `_archive_old/games/generated/hybrid_pattern_se_snake_gene_gen25.py`
- `_archive_old/games/generated/hybrid_incomplete_trail_visu_gen28.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_live_mind._gen31.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen34.py`
- `_archive_old/games/generated/hybrid_tetris_gen_hybrid_emb_gen35.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hello_bot._gen38.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_pon_gen39.py`
- `_archive_old/games/generated/hybrid_ember_prop_hybrid_pat_gen41.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen42.py`
- `_archive_old/games/generated/hybrid_hybrid_bre_hybrid_hyb_gen45.py`
- `_archive_old/games/generated/hybrid_hybrid_sky_hybrid_hyb_gen46.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_pon_gen47.py`
- `_archive_old/games/generated/hybrid_hybrid_too_hybrid_aut_gen50.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_trail_play_gen52.py`
- `_archive_old/games/generated/hybrid_hybrid_too_hybrid_liv_gen54.py`
- `_archive_old/games/generated/hybrid_hybrid_tet_hybrid_hyb_gen55.py`
- `_archive_old/games/generated/hybrid_trail_visu_hybrid_hyb_gen57.py`
- `_archive_old/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen62.py`
- `_archive_old/games/generated/hybrid_hybrid_aut_incomplete_gen65.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen67.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen68.py`
- `_archive_old/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen69.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_emb_gen71.py`
- `_archive_old/games/generated/hybrid_ember_maze_hybrid_hyb_gen73.py`
- `_archive_old/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen75.py`
- `_archive_old/games/generated/hybrid_hybrid_pat_hybrid_hyb_gen76.py`
- `_archive_old/games/generated/hybrid_embers_jou_hybrid_hyb_gen81.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_bre_gen84.py`
- `_archive_old/games/generated/mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`
- `_archive_old/games/generated/hybrid_sky_reach._light_pain_gen4.py`
- `_archive_old/games/generated/hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/games/generated/hybrid_what_if.py_who_am_i.p_gen0.py`
- `_archive_old/games/generated/hybrid_fibonacci__ember_maze_gen1.py`
- `_archive_old/games/generated/hybrid_trail_visu_ember_maze_gen2.py`
- `_archive_old/games/generated/hybrid_meet_your__pattern_ev_gen4.py`
- `_archive_old/games/generated/hybrid_trail_visu_ember_prop_gen5.py`
- `_archive_old/games/generated/hybrid_hybrid_wha_pong_genes_gen6.py`
- `_archive_old/games/generated/hybrid_sky_reach._run_game_e_gen8.py`
- `_archive_old/games/generated/hybrid_hybrid_fib_hybrid_wha_gen9.py`
- `_archive_old/games/generated/hybrid_breakout_g_what_if.py_gen0.py`
- `_archive_old/games/generated/hybrid_fibonacci__embers_jou_gen1.py`
- `_archive_old/games/generated/hybrid_who_am_i.p_tetris_gen_gen2.py`
- `_archive_old/games/generated/hybrid_fibonacci__breakout_g_gen6.py`
- `_archive_old/games/generated/hybrid_live_mind._snake_gene_gen8.py`
- `_archive_old/games/generated/hybrid_pong_genes_incomplete_gen9.py`
- `_archive_old/games/generated/hybrid_ember_firs_who_am_i.p_gen10.py`
- `_archive_old/games/generated/hybrid_hello_bot._coding_doj_gen11.py`
- `_archive_old/games/generated/hybrid_ember_maze_breakout_g_gen15.py`
- `_archive_old/games/generated/hybrid_embers_jou_ember_maze_gen18.py`
- `_archive_old/games/generated/hybrid_ember_prop_sky_reach._gen20.py`
- `_archive_old/games/generated/hybrid_hello_bot._ember_firs_gen22.py`
- `_archive_old/games/generated/hybrid_ember_maze_hybrid_fib_gen23.py`
- `_archive_old/games/generated/hybrid_trail_play_embers_jou_gen26.py`
- `_archive_old/games/generated/hybrid_what_if.py_hybrid_emb_gen27.py`
- `_archive_old/games/generated/hybrid_hybrid_wha_hybrid_liv_gen29.py`
- `_archive_old/games/generated/hybrid_live_mind._hybrid_fib_gen30.py`
- `_archive_old/games/generated/hybrid_hybrid_fib_embers_jou_gen32.py`
- `_archive_old/games/generated/hybrid_hybrid_tra_tetris_gen_gen36.py`
- `_archive_old/games/generated/hybrid_light_pain_hello_bot._gen37.py`
- `_archive_old/games/generated/hybrid_breakout_g_hybrid_fib_gen40.py`
- `_archive_old/games/generated/hybrid_snake_gene_tetris_gen_gen43.py`
- `_archive_old/games/generated/hybrid_breakout_g_hybrid_bre_gen48.py`
- `_archive_old/games/generated/hybrid_hybrid_fib_live_mind._gen49.py`
- `_archive_old/games/generated/mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`
- `_archive_old/games/generated/hybrid_hybrid_bre_hybrid_sna_gen56.py`
- `_archive_old/games/generated/hybrid_hybrid_liv_hybrid_pon_gen58.py`
- `_archive_old/games/generated/hybrid_hybrid_liv_pattern_ev_gen59.py`
- `_archive_old/games/generated/hybrid_hello_bot._fibonacci__gen61.py`
- `_archive_old/games/generated/mutant_live_mind.py_gen64.py`
- `_archive_old/games/generated/hybrid_ember_prop_embers_jou_gen66.py`
- `_archive_old/games/generated/hybrid_pattern_ev_live_mind._gen72.py`
- `_archive_old/games/generated/hybrid_what_if.py_breakout_g_gen79.py`
- `_archive_old/games/generated/hybrid_hybrid_fib_mutant_hyb_gen80.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_hybrid_bre_gen82.py`
- `_archive_old/games/generated/hybrid_hybrid_hyb_incomplete_gen83.py`
- `_archive_old/games/generated/TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/breakout_genesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/breakout_genesis.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/pong_genesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pong_genesis.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_tra_gen77.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_tra_hybrid_hyb_gen60.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_tra_gen77.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_tra_hybrid_hyb_gen60.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_too_gen70.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_tra_gen53.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_trail_visu_hybrid_sky_gen33.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_too_gen70.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_tra_gen53.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_trail_visu_hybrid_sky_gen33.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_coding_doj_hybrid_hyb_gen63.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_coding_doj_hybrid_hyb_gen63.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_autonomous_memory_gar_gen7.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_hybrid_hyb_gen24.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hel_hybrid_hyb_gen85.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_emb_gen44.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_sky_hybrid_hyb_gen78.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_autonomous_memory_gar_gen7.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_hybrid_hyb_gen24.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hel_hybrid_hyb_gen85.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_emb_gen44.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_sky_hybrid_hyb_gen78.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_meet_your__pattern_ev_gen74.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_meet_your__pattern_ev_gen74.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_autonomous_hybrid_too_gen19.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_autonomous_what_if.py_gen12.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_firs_hybrid_hyb_gen16.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_maze_hybrid_hyb_gen73.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_maze_tool_gym.p_gen3.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_prop_hybrid_pat_gen41.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_embers_jou_hybrid_hyb_gen81.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_hybrid_liv_gen21.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_incomplete_gen65.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_live_mind._gen31.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_sky_reach._gen13.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_aut_trail_play_gen52.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_bre_hybrid_hyb_gen45.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_bre_incomplete_gen3.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen62.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen69.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_emb_hybrid_hyb_gen75.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_ember_maze_gen5.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hello_bot._gen38.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_bre_gen84.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_emb_gen71.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen34.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen42.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen67.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_hyb_gen68.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_pon_gen39.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_pon_gen47.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_pat_hybrid_hyb_gen76.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_sky_hybrid_hyb_gen46.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_tet_hybrid_hyb_gen55.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_too_hybrid_aut_gen50.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_too_hybrid_liv_gen54.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_incomplete_trail_visu_gen28.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_pattern_se_snake_gene_gen25.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_sky_reach._autonomous_gen7.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_tetris_gen_hybrid_emb_gen35.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_tool_gym.p_ember_prop_gen14.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_tool_gym.p_memory_gar_gen17.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_trail_visu_hybrid_hyb_gen57.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_autonomous_hybrid_too_gen19.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_autonomous_what_if.py_gen12.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_firs_hybrid_hyb_gen16.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_maze_hybrid_hyb_gen73.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_maze_tool_gym.p_gen3.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_prop_hybrid_pat_gen41.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_embers_jou_hybrid_hyb_gen81.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_hybrid_liv_gen21.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_incomplete_gen65.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_live_mind._gen31.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_sky_reach._gen13.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_aut_trail_play_gen52.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_bre_hybrid_hyb_gen45.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_bre_incomplete_gen3.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_emb_hybrid_hyb_gen62.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_emb_hybrid_hyb_gen69.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_emb_hybrid_hyb_gen75.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_ember_maze_gen5.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hello_bot._gen38.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_bre_gen84.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_emb_gen71.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_hyb_gen34.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_hyb_gen42.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_hyb_gen67.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_hyb_gen68.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_pon_gen39.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_pon_gen47.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_pat_hybrid_hyb_gen76.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_sky_hybrid_hyb_gen46.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_tet_hybrid_hyb_gen55.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_too_hybrid_aut_gen50.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_too_hybrid_liv_gen54.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_incomplete_trail_visu_gen28.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_pattern_se_snake_gene_gen25.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_sky_reach._autonomous_gen7.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_tetris_gen_hybrid_emb_gen35.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_tool_gym.p_ember_prop_gen14.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_tool_gym.p_memory_gar_gen17.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_trail_visu_hybrid_hyb_gen57.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_sky_reach._light_pain_gen4.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_sky_reach._light_pain_gen4.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_breakout_g_hybrid_bre_gen48.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_breakout_g_hybrid_fib_gen40.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_breakout_g_what_if.py_gen0.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_firs_who_am_i.p_gen10.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_maze_breakout_g_gen15.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_maze_hybrid_fib_gen23.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_prop_embers_jou_gen66.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_ember_prop_sky_reach._gen20.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_embers_jou_ember_maze_gen18.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_fibonacci__breakout_g_gen6.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_fibonacci__ember_maze_gen1.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_fibonacci__embers_jou_gen1.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hello_bot._coding_doj_gen11.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hello_bot._ember_firs_gen22.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hello_bot._fibonacci__gen61.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_bre_hybrid_sna_gen56.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_fib_embers_jou_gen32.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_fib_hybrid_wha_gen9.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_fib_live_mind._gen49.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_fib_mutant_hyb_gen80.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_hybrid_bre_gen82.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_hyb_incomplete_gen83.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_liv_hybrid_pon_gen58.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_liv_pattern_ev_gen59.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_tra_tetris_gen_gen36.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_wha_hybrid_liv_gen29.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_hybrid_wha_pong_genes_gen6.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_light_pain_hello_bot._gen37.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_live_mind._hybrid_fib_gen30.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_live_mind._snake_gene_gen8.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_meet_your__pattern_ev_gen4.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_pattern_ev_live_mind._gen72.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_pong_genes_incomplete_gen9.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_sky_reach._run_game_e_gen8.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_snake_gene_tetris_gen_gen43.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_trail_play_embers_jou_gen26.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_trail_visu_ember_maze_gen2.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_trail_visu_ember_prop_gen5.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_what_if.py_breakout_g_gen79.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_what_if.py_hybrid_emb_gen27.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_what_if.py_who_am_i.p_gen0.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/hybrid_who_am_i.p_tetris_gen_gen2.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/generated/mutant_live_mind.py_gen64.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_breakout_g_hybrid_bre_gen48.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_breakout_g_hybrid_fib_gen40.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_breakout_g_what_if.py_gen0.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_firs_who_am_i.p_gen10.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_maze_breakout_g_gen15.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_maze_hybrid_fib_gen23.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_prop_embers_jou_gen66.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_ember_prop_sky_reach._gen20.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_embers_jou_ember_maze_gen18.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_fibonacci__breakout_g_gen6.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_fibonacci__ember_maze_gen1.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_fibonacci__embers_jou_gen1.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hello_bot._coding_doj_gen11.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hello_bot._ember_firs_gen22.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hello_bot._fibonacci__gen61.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_bre_hybrid_sna_gen56.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_fib_embers_jou_gen32.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_fib_hybrid_wha_gen9.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_fib_live_mind._gen49.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_fib_mutant_hyb_gen80.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_hybrid_bre_gen82.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_hyb_incomplete_gen83.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_liv_hybrid_pon_gen58.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_liv_pattern_ev_gen59.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_tra_tetris_gen_gen36.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_wha_hybrid_liv_gen29.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_hybrid_wha_pong_genes_gen6.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_light_pain_hello_bot._gen37.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_live_mind._hybrid_fib_gen30.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_live_mind._snake_gene_gen8.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_meet_your__pattern_ev_gen4.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_memory_gar_embers_jou_gen0.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_pattern_ev_live_mind._gen72.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_pong_genes_incomplete_gen9.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_sky_reach._run_game_e_gen8.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_snake_gene_tetris_gen_gen43.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_trail_play_embers_jou_gen26.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_trail_visu_ember_maze_gen2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_trail_visu_ember_prop_gen5.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_what_if.py_breakout_g_gen79.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_what_if.py_hybrid_emb_gen27.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_what_if.py_who_am_i.p_gen0.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/hybrid_who_am_i.p_tetris_gen_gen2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/generated/mutant_live_mind.py_gen64.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `hybrid_hybrid_fib_mutant_hyb_gen80.py`, `TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_breakout_g_hybrid_bre_gen48.py`, `hybrid_pattern_ev_live_mind._gen72.py`, `hybrid_breakout_g_hybrid_fib_gen40.py`, `hybrid_hybrid_tet_hybrid_hyb_gen55.py`, `hybrid_coding_doj_hybrid_hyb_gen63.py`, `hybrid_ember_prop_hybrid_pat_gen41.py`, `hybrid_light_pain_hello_bot._gen37.py`, `hybrid_autonomous_memory_gar_gen7.py`, `hybrid_hybrid_hyb_hybrid_bre_gen82.py`, `hybrid_what_if.py_who_am_i.p_gen0.py`, `hybrid_hybrid_hyb_hybrid_emb_gen71.py`, `hybrid_hybrid_hyb_hybrid_tra_gen53.py`, `hybrid_hybrid_too_hybrid_liv_gen54.py`, `hybrid_ember_maze_breakout_g_gen15.py`, `hybrid_hybrid_bre_incomplete_gen3.py`, `hybrid_embers_jou_ember_maze_gen18.py`, `hybrid_fibonacci__breakout_g_gen6.py`, `hybrid_hybrid_too_hybrid_aut_gen50.py`, `hybrid_trail_visu_hybrid_hyb_gen57.py`, `hybrid_hybrid_bre_hybrid_sna_gen56.py`, `hybrid_meet_your__pattern_ev_gen74.py`, `hybrid_hybrid_fib_live_mind._gen49.py`, `hybrid_hybrid_sky_hybrid_hyb_gen46.py`, `hybrid_autonomous_hybrid_too_gen19.py`, `hybrid_hybrid_emb_hybrid_hyb_gen62.py`, `hybrid_autonomous_what_if.py_gen12.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen67.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen68.py`, `hybrid_hybrid_hyb_hybrid_bre_gen84.py`, `hybrid_ember_firs_who_am_i.p_gen10.py`, `mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`, `hybrid_hybrid_hyb_hybrid_pon_gen47.py`, `hybrid_sky_reach._run_game_e_gen8.py`, `hybrid_hybrid_wha_pong_genes_gen6.py`, `hybrid_hybrid_hyb_hybrid_pon_gen39.py`, `hybrid_tool_gym.p_memory_gar_gen17.py`, `breakout_genesis.py`, `hybrid_hybrid_liv_pattern_ev_gen59.py`, `hybrid_live_mind._snake_gene_gen8.py`, `hybrid_who_am_i.p_tetris_gen_gen2.py`, `hybrid_pattern_se_snake_gene_gen25.py`, `hybrid_snake_gene_tetris_gen_gen43.py`, `mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`, `hybrid_trail_visu_ember_prop_gen5.py`, `hybrid_hybrid_tra_tetris_gen_gen36.py`, `hybrid_hybrid_hyb_ember_maze_gen5.py`, `hybrid_hybrid_aut_hybrid_liv_gen21.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen34.py`, `hybrid_hybrid_hyb_hello_bot._gen38.py`, `hybrid_hybrid_hyb_incomplete_gen83.py`, `hybrid_hybrid_emb_hybrid_hyb_gen69.py`, `hybrid_hybrid_fib_embers_jou_gen32.py`, `hybrid_hybrid_sky_hybrid_hyb_gen78.py`, `hybrid_tool_gym.p_ember_prop_gen14.py`, `hybrid_hybrid_pat_hybrid_hyb_gen76.py`, `hybrid_hybrid_aut_live_mind._gen31.py`, `hybrid_hybrid_fib_hybrid_wha_gen9.py`, `hybrid_pong_genes_incomplete_gen9.py`, `hybrid_hybrid_aut_incomplete_gen65.py`, `hybrid_ember_prop_embers_jou_gen66.py`, `hybrid_trail_play_embers_jou_gen26.py`, `hybrid_ember_prop_sky_reach._gen20.py`, `hybrid_hybrid_bre_hybrid_hyb_gen45.py`, `hybrid_hybrid_wha_hybrid_liv_gen29.py`, `hybrid_hybrid_emb_hybrid_hyb_gen75.py`, `hybrid_hybrid_tra_hybrid_hyb_gen60.py`, `hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_sky_reach._light_pain_gen4.py`, `hybrid_hello_bot._coding_doj_gen11.py`, `hybrid_ember_maze_tool_gym.p_gen3.py`, `hybrid_hybrid_hel_hybrid_hyb_gen85.py`, `hybrid_hybrid_liv_hybrid_pon_gen58.py`, `hybrid_what_if.py_breakout_g_gen79.py`, `hybrid_hybrid_aut_sky_reach._gen13.py`, `hybrid_trail_visu_hybrid_sky_gen33.py`, `pong_genesis.py`, `hybrid_ember_firs_hybrid_hyb_gen16.py`, `hybrid_incomplete_trail_visu_gen28.py`, `hybrid_tetris_gen_hybrid_emb_gen35.py`, `hybrid_hybrid_aut_hybrid_hyb_gen24.py`, `hybrid_hybrid_aut_trail_play_gen52.py`, `hybrid_meet_your__pattern_ev_gen4.py`, `hybrid_embers_jou_hybrid_hyb_gen81.py`, `hybrid_ember_maze_hybrid_fib_gen23.py`, `hybrid_sky_reach._autonomous_gen7.py`, `mutant_live_mind.py_gen64.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen42.py`, `hybrid_hybrid_hyb_hybrid_emb_gen44.py`, `hybrid_breakout_g_what_if.py_gen0.py`, `hybrid_fibonacci__ember_maze_gen1.py`, `hybrid_hybrid_hyb_hybrid_too_gen70.py`, `hybrid_hybrid_hyb_hybrid_tra_gen77.py`, `hybrid_live_mind._hybrid_fib_gen30.py`, `hybrid_ember_maze_hybrid_hyb_gen73.py`, `hybrid_hello_bot._ember_firs_gen22.py`, `hybrid_trail_visu_ember_maze_gen2.py`, `hybrid_hello_bot._fibonacci__gen61.py`, `hybrid_fibonacci__embers_jou_gen1.py`, `hybrid_what_if.py_hybrid_emb_gen27.py`
- `move` in: `hybrid_hybrid_fib_mutant_hyb_gen80.py`, `TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_breakout_g_hybrid_bre_gen48.py`, `hybrid_pattern_ev_live_mind._gen72.py`, `hybrid_breakout_g_hybrid_fib_gen40.py`, `hybrid_hybrid_tet_hybrid_hyb_gen55.py`, `hybrid_coding_doj_hybrid_hyb_gen63.py`, `hybrid_ember_prop_hybrid_pat_gen41.py`, `hybrid_light_pain_hello_bot._gen37.py`, `hybrid_autonomous_memory_gar_gen7.py`, `hybrid_hybrid_hyb_hybrid_bre_gen82.py`, `hybrid_what_if.py_who_am_i.p_gen0.py`, `hybrid_hybrid_hyb_hybrid_emb_gen71.py`, `hybrid_hybrid_hyb_hybrid_tra_gen53.py`, `hybrid_hybrid_too_hybrid_liv_gen54.py`, `hybrid_ember_maze_breakout_g_gen15.py`, `hybrid_hybrid_bre_incomplete_gen3.py`, `hybrid_embers_jou_ember_maze_gen18.py`, `hybrid_fibonacci__breakout_g_gen6.py`, `hybrid_hybrid_too_hybrid_aut_gen50.py`, `hybrid_trail_visu_hybrid_hyb_gen57.py`, `hybrid_hybrid_bre_hybrid_sna_gen56.py`, `hybrid_meet_your__pattern_ev_gen74.py`, `hybrid_hybrid_fib_live_mind._gen49.py`, `hybrid_hybrid_sky_hybrid_hyb_gen46.py`, `hybrid_autonomous_hybrid_too_gen19.py`, `hybrid_hybrid_emb_hybrid_hyb_gen62.py`, `hybrid_autonomous_what_if.py_gen12.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen67.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen68.py`, `hybrid_hybrid_hyb_hybrid_bre_gen84.py`, `hybrid_ember_firs_who_am_i.p_gen10.py`, `mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`, `hybrid_hybrid_hyb_hybrid_pon_gen47.py`, `hybrid_sky_reach._run_game_e_gen8.py`, `hybrid_hybrid_wha_pong_genes_gen6.py`, `hybrid_hybrid_hyb_hybrid_pon_gen39.py`, `hybrid_tool_gym.p_memory_gar_gen17.py`, `breakout_genesis.py`, `hybrid_hybrid_liv_pattern_ev_gen59.py`, `hybrid_live_mind._snake_gene_gen8.py`, `hybrid_who_am_i.p_tetris_gen_gen2.py`, `hybrid_pattern_se_snake_gene_gen25.py`, `hybrid_snake_gene_tetris_gen_gen43.py`, `mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`, `hybrid_trail_visu_ember_prop_gen5.py`, `hybrid_hybrid_tra_tetris_gen_gen36.py`, `hybrid_hybrid_hyb_ember_maze_gen5.py`, `hybrid_hybrid_aut_hybrid_liv_gen21.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen34.py`, `hybrid_hybrid_hyb_hello_bot._gen38.py`, `hybrid_hybrid_hyb_incomplete_gen83.py`, `hybrid_hybrid_emb_hybrid_hyb_gen69.py`, `hybrid_hybrid_fib_embers_jou_gen32.py`, `hybrid_hybrid_sky_hybrid_hyb_gen78.py`, `hybrid_tool_gym.p_ember_prop_gen14.py`, `hybrid_hybrid_pat_hybrid_hyb_gen76.py`, `hybrid_hybrid_aut_live_mind._gen31.py`, `hybrid_hybrid_fib_hybrid_wha_gen9.py`, `hybrid_pong_genes_incomplete_gen9.py`, `hybrid_hybrid_aut_incomplete_gen65.py`, `hybrid_ember_prop_embers_jou_gen66.py`, `hybrid_trail_play_embers_jou_gen26.py`, `hybrid_ember_prop_sky_reach._gen20.py`, `hybrid_hybrid_bre_hybrid_hyb_gen45.py`, `hybrid_hybrid_wha_hybrid_liv_gen29.py`, `hybrid_hybrid_emb_hybrid_hyb_gen75.py`, `hybrid_hybrid_tra_hybrid_hyb_gen60.py`, `hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_sky_reach._light_pain_gen4.py`, `hybrid_hello_bot._coding_doj_gen11.py`, `hybrid_ember_maze_tool_gym.p_gen3.py`, `hybrid_hybrid_hel_hybrid_hyb_gen85.py`, `hybrid_hybrid_liv_hybrid_pon_gen58.py`, `hybrid_what_if.py_breakout_g_gen79.py`, `hybrid_hybrid_aut_sky_reach._gen13.py`, `hybrid_trail_visu_hybrid_sky_gen33.py`, `pong_genesis.py`, `hybrid_ember_firs_hybrid_hyb_gen16.py`, `hybrid_incomplete_trail_visu_gen28.py`, `hybrid_tetris_gen_hybrid_emb_gen35.py`, `hybrid_hybrid_aut_hybrid_hyb_gen24.py`, `hybrid_hybrid_aut_trail_play_gen52.py`, `hybrid_meet_your__pattern_ev_gen4.py`, `hybrid_embers_jou_hybrid_hyb_gen81.py`, `hybrid_ember_maze_hybrid_fib_gen23.py`, `hybrid_sky_reach._autonomous_gen7.py`, `mutant_live_mind.py_gen64.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen42.py`, `hybrid_hybrid_hyb_hybrid_emb_gen44.py`, `hybrid_breakout_g_what_if.py_gen0.py`, `hybrid_fibonacci__ember_maze_gen1.py`, `hybrid_hybrid_hyb_hybrid_too_gen70.py`, `hybrid_hybrid_hyb_hybrid_tra_gen77.py`, `hybrid_live_mind._hybrid_fib_gen30.py`, `hybrid_ember_maze_hybrid_hyb_gen73.py`, `hybrid_hello_bot._ember_firs_gen22.py`, `hybrid_trail_visu_ember_maze_gen2.py`, `hybrid_hello_bot._fibonacci__gen61.py`, `hybrid_fibonacci__embers_jou_gen1.py`, `hybrid_what_if.py_hybrid_emb_gen27.py`
- `draw` in: `hybrid_hybrid_fib_mutant_hyb_gen80.py`, `TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_breakout_g_hybrid_bre_gen48.py`, `hybrid_pattern_ev_live_mind._gen72.py`, `hybrid_breakout_g_hybrid_fib_gen40.py`, `hybrid_hybrid_tet_hybrid_hyb_gen55.py`, `hybrid_coding_doj_hybrid_hyb_gen63.py`, `hybrid_ember_prop_hybrid_pat_gen41.py`, `hybrid_light_pain_hello_bot._gen37.py`, `hybrid_autonomous_memory_gar_gen7.py`, `hybrid_hybrid_hyb_hybrid_bre_gen82.py`, `hybrid_what_if.py_who_am_i.p_gen0.py`, `hybrid_hybrid_hyb_hybrid_emb_gen71.py`, `hybrid_hybrid_hyb_hybrid_tra_gen53.py`, `hybrid_hybrid_too_hybrid_liv_gen54.py`, `hybrid_ember_maze_breakout_g_gen15.py`, `hybrid_hybrid_bre_incomplete_gen3.py`, `hybrid_embers_jou_ember_maze_gen18.py`, `hybrid_fibonacci__breakout_g_gen6.py`, `hybrid_hybrid_too_hybrid_aut_gen50.py`, `hybrid_trail_visu_hybrid_hyb_gen57.py`, `hybrid_hybrid_bre_hybrid_sna_gen56.py`, `hybrid_meet_your__pattern_ev_gen74.py`, `hybrid_hybrid_fib_live_mind._gen49.py`, `hybrid_hybrid_sky_hybrid_hyb_gen46.py`, `hybrid_autonomous_hybrid_too_gen19.py`, `hybrid_hybrid_emb_hybrid_hyb_gen62.py`, `hybrid_autonomous_what_if.py_gen12.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen67.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen68.py`, `hybrid_hybrid_hyb_hybrid_bre_gen84.py`, `hybrid_ember_firs_who_am_i.p_gen10.py`, `mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`, `hybrid_hybrid_hyb_hybrid_pon_gen47.py`, `hybrid_sky_reach._run_game_e_gen8.py`, `hybrid_hybrid_wha_pong_genes_gen6.py`, `hybrid_hybrid_hyb_hybrid_pon_gen39.py`, `hybrid_tool_gym.p_memory_gar_gen17.py`, `breakout_genesis.py`, `hybrid_hybrid_liv_pattern_ev_gen59.py`, `hybrid_live_mind._snake_gene_gen8.py`, `hybrid_who_am_i.p_tetris_gen_gen2.py`, `hybrid_pattern_se_snake_gene_gen25.py`, `hybrid_snake_gene_tetris_gen_gen43.py`, `mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`, `hybrid_trail_visu_ember_prop_gen5.py`, `hybrid_hybrid_tra_tetris_gen_gen36.py`, `hybrid_hybrid_hyb_ember_maze_gen5.py`, `hybrid_hybrid_aut_hybrid_liv_gen21.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen34.py`, `hybrid_hybrid_hyb_hello_bot._gen38.py`, `hybrid_hybrid_hyb_incomplete_gen83.py`, `hybrid_hybrid_emb_hybrid_hyb_gen69.py`, `hybrid_hybrid_fib_embers_jou_gen32.py`, `hybrid_hybrid_sky_hybrid_hyb_gen78.py`, `hybrid_tool_gym.p_ember_prop_gen14.py`, `hybrid_hybrid_pat_hybrid_hyb_gen76.py`, `hybrid_hybrid_aut_live_mind._gen31.py`, `hybrid_hybrid_fib_hybrid_wha_gen9.py`, `hybrid_pong_genes_incomplete_gen9.py`, `hybrid_hybrid_aut_incomplete_gen65.py`, `hybrid_ember_prop_embers_jou_gen66.py`, `hybrid_trail_play_embers_jou_gen26.py`, `hybrid_ember_prop_sky_reach._gen20.py`, `hybrid_hybrid_bre_hybrid_hyb_gen45.py`, `hybrid_hybrid_wha_hybrid_liv_gen29.py`, `hybrid_hybrid_emb_hybrid_hyb_gen75.py`, `hybrid_hybrid_tra_hybrid_hyb_gen60.py`, `hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_sky_reach._light_pain_gen4.py`, `hybrid_hello_bot._coding_doj_gen11.py`, `hybrid_ember_maze_tool_gym.p_gen3.py`, `hybrid_hybrid_hel_hybrid_hyb_gen85.py`, `hybrid_hybrid_liv_hybrid_pon_gen58.py`, `hybrid_what_if.py_breakout_g_gen79.py`, `hybrid_hybrid_aut_sky_reach._gen13.py`, `hybrid_trail_visu_hybrid_sky_gen33.py`, `pong_genesis.py`, `hybrid_ember_firs_hybrid_hyb_gen16.py`, `hybrid_incomplete_trail_visu_gen28.py`, `hybrid_tetris_gen_hybrid_emb_gen35.py`, `hybrid_hybrid_aut_hybrid_hyb_gen24.py`, `hybrid_hybrid_aut_trail_play_gen52.py`, `hybrid_meet_your__pattern_ev_gen4.py`, `hybrid_embers_jou_hybrid_hyb_gen81.py`, `hybrid_ember_maze_hybrid_fib_gen23.py`, `hybrid_sky_reach._autonomous_gen7.py`, `mutant_live_mind.py_gen64.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen42.py`, `hybrid_hybrid_hyb_hybrid_emb_gen44.py`, `hybrid_breakout_g_what_if.py_gen0.py`, `hybrid_fibonacci__ember_maze_gen1.py`, `hybrid_hybrid_hyb_hybrid_too_gen70.py`, `hybrid_hybrid_hyb_hybrid_tra_gen77.py`, `hybrid_live_mind._hybrid_fib_gen30.py`, `hybrid_ember_maze_hybrid_hyb_gen73.py`, `hybrid_hello_bot._ember_firs_gen22.py`, `hybrid_trail_visu_ember_maze_gen2.py`, `hybrid_hello_bot._fibonacci__gen61.py`, `hybrid_fibonacci__embers_jou_gen1.py`, `hybrid_what_if.py_hybrid_emb_gen27.py`
- `reset` in: `hybrid_hybrid_fib_mutant_hyb_gen80.py`, `TURING_COMPLETE_evolved_gen0_hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_breakout_g_hybrid_bre_gen48.py`, `hybrid_pattern_ev_live_mind._gen72.py`, `hybrid_breakout_g_hybrid_fib_gen40.py`, `hybrid_hybrid_tet_hybrid_hyb_gen55.py`, `hybrid_coding_doj_hybrid_hyb_gen63.py`, `hybrid_ember_prop_hybrid_pat_gen41.py`, `hybrid_light_pain_hello_bot._gen37.py`, `hybrid_autonomous_memory_gar_gen7.py`, `hybrid_hybrid_hyb_hybrid_bre_gen82.py`, `hybrid_what_if.py_who_am_i.p_gen0.py`, `hybrid_hybrid_hyb_hybrid_emb_gen71.py`, `hybrid_hybrid_hyb_hybrid_tra_gen53.py`, `hybrid_hybrid_too_hybrid_liv_gen54.py`, `hybrid_ember_maze_breakout_g_gen15.py`, `hybrid_hybrid_bre_incomplete_gen3.py`, `hybrid_embers_jou_ember_maze_gen18.py`, `hybrid_fibonacci__breakout_g_gen6.py`, `hybrid_hybrid_too_hybrid_aut_gen50.py`, `hybrid_trail_visu_hybrid_hyb_gen57.py`, `hybrid_hybrid_bre_hybrid_sna_gen56.py`, `hybrid_meet_your__pattern_ev_gen74.py`, `hybrid_hybrid_fib_live_mind._gen49.py`, `hybrid_hybrid_sky_hybrid_hyb_gen46.py`, `hybrid_autonomous_hybrid_too_gen19.py`, `hybrid_hybrid_emb_hybrid_hyb_gen62.py`, `hybrid_autonomous_what_if.py_gen12.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen67.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen68.py`, `hybrid_hybrid_hyb_hybrid_bre_gen84.py`, `hybrid_ember_firs_who_am_i.p_gen10.py`, `mutant_hybrid_ember_maze_hybrid_fib_gen23_gen51.py`, `hybrid_hybrid_hyb_hybrid_pon_gen47.py`, `hybrid_sky_reach._run_game_e_gen8.py`, `hybrid_hybrid_wha_pong_genes_gen6.py`, `hybrid_hybrid_hyb_hybrid_pon_gen39.py`, `hybrid_tool_gym.p_memory_gar_gen17.py`, `breakout_genesis.py`, `hybrid_hybrid_liv_pattern_ev_gen59.py`, `hybrid_live_mind._snake_gene_gen8.py`, `hybrid_who_am_i.p_tetris_gen_gen2.py`, `hybrid_pattern_se_snake_gene_gen25.py`, `hybrid_snake_gene_tetris_gen_gen43.py`, `mutant_hybrid_who_am_i.p_tetris_gen_gen2_gen86.py`, `hybrid_trail_visu_ember_prop_gen5.py`, `hybrid_hybrid_tra_tetris_gen_gen36.py`, `hybrid_hybrid_hyb_ember_maze_gen5.py`, `hybrid_hybrid_aut_hybrid_liv_gen21.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen34.py`, `hybrid_hybrid_hyb_hello_bot._gen38.py`, `hybrid_hybrid_hyb_incomplete_gen83.py`, `hybrid_hybrid_emb_hybrid_hyb_gen69.py`, `hybrid_hybrid_fib_embers_jou_gen32.py`, `hybrid_hybrid_sky_hybrid_hyb_gen78.py`, `hybrid_tool_gym.p_ember_prop_gen14.py`, `hybrid_hybrid_pat_hybrid_hyb_gen76.py`, `hybrid_hybrid_aut_live_mind._gen31.py`, `hybrid_hybrid_fib_hybrid_wha_gen9.py`, `hybrid_pong_genes_incomplete_gen9.py`, `hybrid_hybrid_aut_incomplete_gen65.py`, `hybrid_ember_prop_embers_jou_gen66.py`, `hybrid_trail_play_embers_jou_gen26.py`, `hybrid_ember_prop_sky_reach._gen20.py`, `hybrid_hybrid_bre_hybrid_hyb_gen45.py`, `hybrid_hybrid_wha_hybrid_liv_gen29.py`, `hybrid_hybrid_emb_hybrid_hyb_gen75.py`, `hybrid_hybrid_tra_hybrid_hyb_gen60.py`, `hybrid_memory_gar_embers_jou_gen0.py`, `hybrid_sky_reach._light_pain_gen4.py`, `hybrid_hello_bot._coding_doj_gen11.py`, `hybrid_ember_maze_tool_gym.p_gen3.py`, `hybrid_hybrid_hel_hybrid_hyb_gen85.py`, `hybrid_hybrid_liv_hybrid_pon_gen58.py`, `hybrid_what_if.py_breakout_g_gen79.py`, `hybrid_hybrid_aut_sky_reach._gen13.py`, `hybrid_trail_visu_hybrid_sky_gen33.py`, `pong_genesis.py`, `hybrid_ember_firs_hybrid_hyb_gen16.py`, `hybrid_incomplete_trail_visu_gen28.py`, `hybrid_tetris_gen_hybrid_emb_gen35.py`, `hybrid_hybrid_aut_hybrid_hyb_gen24.py`, `hybrid_hybrid_aut_trail_play_gen52.py`, `hybrid_meet_your__pattern_ev_gen4.py`, `hybrid_embers_jou_hybrid_hyb_gen81.py`, `hybrid_ember_maze_hybrid_fib_gen23.py`, `hybrid_sky_reach._autonomous_gen7.py`, `mutant_live_mind.py_gen64.py`, `hybrid_hybrid_hyb_hybrid_hyb_gen42.py`, `hybrid_hybrid_hyb_hybrid_emb_gen44.py`, `hybrid_breakout_g_what_if.py_gen0.py`, `hybrid_fibonacci__ember_maze_gen1.py`, `hybrid_hybrid_hyb_hybrid_too_gen70.py`, `hybrid_hybrid_hyb_hybrid_tra_gen77.py`, `hybrid_live_mind._hybrid_fib_gen30.py`, `hybrid_ember_maze_hybrid_hyb_gen73.py`, `hybrid_hello_bot._ember_firs_gen22.py`, `hybrid_trail_visu_ember_maze_gen2.py`, `hybrid_hello_bot._fibonacci__gen61.py`, `hybrid_fibonacci__embers_jou_gen1.py`, `hybrid_what_if.py_hybrid_emb_gen27.py`

---

## Cluster 56

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/ember_first_lesson.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/ember_first_lesson.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_first_lesson.py`

**⚠️ Unique Functions** (may need manual merge):
- `think_to_light` in: `ember_first_lesson.py`

---

## Cluster 57

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/fibonacci_dance.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/fibonacci_dance.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/fibonacci_dance.py`

**⚠️ Unique Functions** (may need manual merge):
- `fibonacci_dance` in: `fibonacci_dance.py`
- `golden_ratio` in: `fibonacci_dance.py`
- `play` in: `fibonacci_dance.py`

---

## Cluster 58

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/game_streamer.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/game_streamer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/game_streamer.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `game_streamer.py`
- `handle_input` in: `game_streamer.py`
- `create_test_frame` in: `game_streamer.py`

---

## Cluster 59

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/hello_bot.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/hello_bot.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/hello_bot.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `hello_bot.py`
- `__init__` in: `hello_bot.py`
- `greet` in: `hello_bot.py`
- `ask_question` in: `hello_bot.py`
- `show_invitation` in: `hello_bot.py`

---

## Cluster 60

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/pattern_seeker.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/pattern_seeker.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pattern_seeker.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_pattern` in: `pattern_seeker.py`
- `add_noise` in: `pattern_seeker.py`
- `visualize` in: `pattern_seeker.py`
- `play` in: `pattern_seeker.py`

---

## Cluster 61

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/run_game_engine_autonomous.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/run_game_engine_autonomous.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/run_game_engine_autonomous.py`

**⚠️ Unique Functions** (may need manual merge):
- `autonomous_run` in: `run_game_engine_autonomous.py`

---

## Cluster 62

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/games/snake_genesis.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/games/snake_genesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/snake_genesis.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `snake_genesis.py`
- `move` in: `snake_genesis.py`
- `grow` in: `snake_genesis.py`
- `check_collision` in: `snake_genesis.py`
- `draw` in: `snake_genesis.py`
- `spawn` in: `snake_genesis.py`

---

## Cluster 63

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/bfs.py`

**Archive** (3 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/harvest/algorithms/bfs.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/bfs.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/bfs.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_bfs` in: `bfs.py`
- `__init__` in: `bfs.py`
- `add_edge` in: `bfs.py`
- `bfs` in: `bfs.py`
- `shortest_path` in: `bfs.py`

---

## Cluster 64

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/dfs.py`

**Archive** (3 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/harvest/algorithms/dfs.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/dfs.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/dfs.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_dfs` in: `dfs.py`
- `__init__` in: `dfs.py`
- `add_edge` in: `dfs.py`
- `dfs_recursive` in: `dfs.py`
- `dfs_iterative` in: `dfs.py`
- `has_cycle` in: `dfs.py`
- `has_cycle_util` in: `dfs.py`

---

## Cluster 65

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/quicksort.py`

**Archive** (3 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/harvest/algorithms/quicksort.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/quicksort.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/quicksort.py`

**⚠️ Unique Functions** (may need manual merge):
- `quicksort` in: `quicksort.py`
- `quicksort_inplace` in: `quicksort.py`
- `partition` in: `quicksort.py`
- `demonstrate_quicksort` in: `quicksort.py`

---

## Cluster 66

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/hash_table.py`

**Archive** (3 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/harvest/data_structures/hash_table.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/hash_table.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/hash_table.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_hash_table` in: `hash_table.py`
- `__init__` in: `hash_table.py`
- `_hash` in: `hash_table.py`
- `put` in: `hash_table.py`
- `get` in: `hash_table.py`
- `delete` in: `hash_table.py`
- `_resize` in: `hash_table.py`

---

## Cluster 67

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/conways_life.py`

**Archive** (3 files):
- `_archive_old/archive/flash_backups/Ember_Backup_20251025/harvest/games/conways_life.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/conways_life.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/conways_life.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_turing_completeness` in: `conways_life.py`
- `__init__` in: `conways_life.py`
- `seed_random` in: `conways_life.py`
- `seed_glider` in: `conways_life.py`
- `seed_blinker` in: `conways_life.py`
- `count_neighbors` in: `conways_life.py`
- `step` in: `conways_life.py`
- `get_state` in: `conways_life.py`
- `is_stable` in: `conways_life.py`

---

## Cluster 68

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/adaptive_model_detector.py`

**Archive** (2 files):
- `_archive_old/hive/adaptive_model_detector.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/adaptive_model_detector.py`

**⚠️ Unique Functions** (may need manual merge):
- `find_model_by_pattern` in: `adaptive_model_detector.py`
- `has_model_files` in: `adaptive_model_detector.py`
- `detect_models` in: `adaptive_model_detector.py`
- `main` in: `adaptive_model_detector.py`

---

## Cluster 69

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/adaptive_model_loader.py`

**Archive** (2 files):
- `_archive_old/hive/adaptive_model_loader.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/adaptive_model_loader.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `adaptive_model_loader.py`
- `__init__` in: `adaptive_model_loader.py`
- `_detect_hardware` in: `adaptive_model_loader.py`
- `_load_benchmark_cache` in: `adaptive_model_loader.py`
- `_save_benchmark_cache` in: `adaptive_model_loader.py`
- `discover_models` in: `adaptive_model_loader.py`
- `filter_by_hardware` in: `adaptive_model_loader.py`
- `benchmark_model` in: `adaptive_model_loader.py`
- `select_best_model` in: `adaptive_model_loader.py`
- `get_fallback_chain` in: `adaptive_model_loader.py`

---

## Cluster 70

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ai_web_search.py`

**Archive** (2 files):
- `_archive_old/hive/ai_web_search.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ai_web_search.py`

**⚠️ Unique Functions** (may need manual merge):
- `format_web_results` in: `ai_web_search.py`
- `__init__` in: `ai_web_search.py`
- `load_cache` in: `ai_web_search.py`
- `save_cache` in: `ai_web_search.py`
- `calculate_ai_relevance_score` in: `ai_web_search.py`

---

## Cluster 71

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/analyze_ember_stream.py`

**Archive** (2 files):
- `_archive_old/hive/analyze_ember_stream.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/analyze_ember_stream.py`

**⚠️ Unique Functions** (may need manual merge):
- `capture_and_analyze` in: `analyze_ember_stream.py`
- `analyze_stream` in: `analyze_ember_stream.py`

---

## Cluster 72

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ask_ember.py`

**Archive** (2 files):
- `_archive_old/hive/ask_ember.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ask_ember.py`

---

## Cluster 73

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/autonomous_dream_daemon.py`

**Archive** (2 files):
- `_archive_old/hive/autonomous_dream_daemon.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/autonomous_dream_daemon.py`

**⚠️ Unique Functions** (may need manual merge):
- `install_systemd_service` in: `autonomous_dream_daemon.py`
- `__init__` in: `autonomous_dream_daemon.py`
- `load_state` in: `autonomous_dream_daemon.py`
- `save_state` in: `autonomous_dream_daemon.py`
- `detect_mode` in: `autonomous_dream_daemon.py`
- `check_brain` in: `autonomous_dream_daemon.py`
- `select_fragment` in: `autonomous_dream_daemon.py`
- `dream_full` in: `autonomous_dream_daemon.py`
- `dream_low_power` in: `autonomous_dream_daemon.py`
- `dream_autonomous` in: `autonomous_dream_daemon.py`
- `dream_dormant` in: `autonomous_dream_daemon.py`
- `dream_once` in: `autonomous_dream_daemon.py`
- `log_local` in: `autonomous_dream_daemon.py`
- `sync_to_thepod` in: `autonomous_dream_daemon.py`
- `get_dream_interval` in: `autonomous_dream_daemon.py`
- `run_forever` in: `autonomous_dream_daemon.py`

---

## Cluster 74

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/autonomous_explorer.py`

**Archive** (2 files):
- `_archive_old/hive/autonomous_explorer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/autonomous_explorer.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `autonomous_explorer.py`
- `read_file` in: `autonomous_explorer.py`
- `write_file` in: `autonomous_explorer.py`
- `run_command` in: `autonomous_explorer.py`
- `list_directory` in: `autonomous_explorer.py`
- `search_files` in: `autonomous_explorer.py`
- `search_content` in: `autonomous_explorer.py`
- `think_and_act` in: `autonomous_explorer.py`
- `explore` in: `autonomous_explorer.py`

---

## Cluster 75

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/bridge_brain_service.py`

**Archive** (2 files):
- `_archive_old/hive/bridge_brain_service.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/bridge_brain_service.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model` in: `bridge_brain_service.py`

---

## Cluster 76

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/capture_ember_stream.py`

**Archive** (2 files):
- `_archive_old/hive/capture_ember_stream.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/capture_ember_stream.py`

**⚠️ Unique Functions** (may need manual merge):
- `capture_stream` in: `capture_ember_stream.py`

---

## Cluster 77

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/construction_observer.py`

**Archive** (2 files):
- `_archive_old/hive/construction_observer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/construction_observer.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_observer` in: `construction_observer.py`
- `record_construction` in: `construction_observer.py`
- `__init__` in: `construction_observer.py`
- `observe_file_creation` in: `construction_observer.py`
- `observe_code_execution` in: `construction_observer.py`
- `observe_file_modification` in: `construction_observer.py`
- `observe_file_deletion` in: `construction_observer.py`
- `observe_architecture_change` in: `construction_observer.py`
- `observe_training` in: `construction_observer.py`
- `get_construction_history` in: `construction_observer.py`
- `summarize_learning` in: `construction_observer.py`
- `_log` in: `construction_observer.py`

---

## Cluster 78

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/continuous_learning_models.py`

**Archive** (2 files):
- `_archive_old/hive/continuous_learning_models.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/continuous_learning_models.py`

---

## Cluster 79

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/daemon_soup.py`

**Archive** (2 files):
- `_archive_old/hive/daemon_soup.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/daemon_soup.py`

**⚠️ Unique Functions** (may need manual merge):
- `integrate_with_knowledge_graph` in: `daemon_soup.py`
- `__init__` in: `daemon_soup.py`
- `pulse` in: `daemon_soup.py`
- `to_dict` in: `daemon_soup.py`
- `_load_or_create` in: `daemon_soup.py`
- `_create_seed_daemons` in: `daemon_soup.py`
- `_append_pulse` in: `daemon_soup.py`
- `_pulse_count` in: `daemon_soup.py`
- `load_pulses` in: `daemon_soup.py`
- `tick` in: `daemon_soup.py`
- `save` in: `daemon_soup.py`
- `get_daemon` in: `daemon_soup.py`
- `list_daemons` in: `daemon_soup.py`
- `print_summary` in: `daemon_soup.py`
- `enhanced_record_read` in: `daemon_soup.py`

---

## Cluster 80

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/deep_discovery.py`

**Archive** (2 files):
- `_archive_old/hive/deep_discovery.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/deep_discovery.py`

**⚠️ Unique Functions** (may need manual merge):
- `deep_scan` in: `deep_discovery.py`
- `main` in: `deep_discovery.py`

---

## Cluster 81

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/document_renderer.py`

**Archive** (2 files):
- `_archive_old/hive/document_renderer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/document_renderer.py`

**⚠️ Unique Functions** (may need manual merge):
- `extract_essence` in: `document_renderer.py`
- `generate_image_prompt` in: `document_renderer.py`
- `get_cached_image` in: `document_renderer.py`
- `generate_image` in: `document_renderer.py`
- `create_document_page` in: `document_renderer.py`
- `render_document` in: `document_renderer.py`
- `render_from_file` in: `document_renderer.py`

---

## Cluster 82

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_actuator.py`

**Archive** (2 files):
- `_archive_old/hive/dream_actuator.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/dream_actuator.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo_dream_actuator` in: `dream_actuator.py`
- `__init__` in: `dream_actuator.py`
- `_create_lobe_zone_mapping` in: `dream_actuator.py`
- `load_dreams` in: `dream_actuator.py`
- `recognize_patterns` in: `dream_actuator.py`
- `execute_action` in: `dream_actuator.py`
- `_express_lobe_state_on_keyboard` in: `dream_actuator.py`
- `_strengthen_trails` in: `dream_actuator.py`
- `_log_meta_observation` in: `dream_actuator.py`
- `_document_gap` in: `dream_actuator.py`
- `_integrate_wisdom` in: `dream_actuator.py`
- `run_once` in: `dream_actuator.py`

---

## Cluster 83

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_actuator_continuous.py`

**Archive** (2 files):
- `_archive_old/hive/dream_actuator_continuous.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/dream_actuator_continuous.py`

**⚠️ Unique Functions** (may need manual merge):
- `run_continuous` in: `dream_actuator_continuous.py`

---

## Cluster 84

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_cycle_coordinator.py`

**Archive** (2 files):
- `_archive_old/hive/dream_cycle_coordinator.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/dream_cycle_coordinator.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `dream_cycle_coordinator.py`
- `start_phase` in: `dream_cycle_coordinator.py`
- `get_phase_duration` in: `dream_cycle_coordinator.py`
- `is_phase_complete` in: `dream_cycle_coordinator.py`
- `advance_cycle` in: `dream_cycle_coordinator.py`
- `collect_worker_dream` in: `dream_cycle_coordinator.py`
- `set_queen_synthesis` in: `dream_cycle_coordinator.py`
- `get_status` in: `dream_cycle_coordinator.py`
- `run_forever` in: `dream_cycle_coordinator.py`

---

## Cluster 85

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_interface.py`

**Archive** (2 files):
- `_archive_old/hive/dream_interface.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/dream_interface.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `dream_interface.py`
- `ask_ember` in: `dream_interface.py`
- `coordinate_ember` in: `dream_interface.py`
- `dream_conversation` in: `dream_interface.py`

---

## Cluster 86

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_architect.py`

**Archive** (2 files):
- `_archive_old/hive/ember_architect.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_architect.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_architect` in: `ember_architect.py`
- `__init__` in: `ember_architect.py`
- `_load_designs` in: `ember_architect.py`
- `_save_designs` in: `ember_architect.py`
- `design` in: `ember_architect.py`
- `create` in: `ember_architect.py`
- `test` in: `ember_architect.py`
- `_create_lobe_training_data` in: `ember_architect.py`
- `_create_python_module` in: `ember_architect.py`
- `_create_tool` in: `ember_architect.py`
- `list_designs` in: `ember_architect.py`

---

## Cluster 87

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_autonomous_agent.py`

**Archive** (2 files):
- `_archive_old/hive/ember_autonomous_agent.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_autonomous_agent.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_autonomous_agent.py`
- `explore` in: `ember_autonomous_agent.py`
- `reflect` in: `ember_autonomous_agent.py`
- `compress_if_needed` in: `ember_autonomous_agent.py`
- `run_cycle` in: `ember_autonomous_agent.py`
- `run_forever` in: `ember_autonomous_agent.py`
- `run_n_cycles` in: `ember_autonomous_agent.py`
- `print_session_summary` in: `ember_autonomous_agent.py`

---

## Cluster 88

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_autonomous_foraging.py`

**Archive** (2 files):
- `_archive_old/hive/ember_autonomous_foraging.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_autonomous_foraging.py`

**⚠️ Unique Functions** (may need manual merge):
- `start_daemon` in: `ember_autonomous_foraging.py`
- `stop_daemon` in: `ember_autonomous_foraging.py`
- `show_status` in: `ember_autonomous_foraging.py`
- `__init__` in: `ember_autonomous_foraging.py`
- `log` in: `ember_autonomous_foraging.py`
- `load_stats` in: `ember_autonomous_foraging.py`
- `save_stats` in: `ember_autonomous_foraging.py`
- `check_appetite` in: `ember_autonomous_foraging.py`
- `forage_for_knowledge` in: `ember_autonomous_foraging.py`
- `run` in: `ember_autonomous_foraging.py`
- `cleanup` in: `ember_autonomous_foraging.py`
- `signal_handler` in: `ember_autonomous_foraging.py`

---

## Cluster 89

**Reason**: Name variations of 'ember_brain'

**Keep**: `_archive_old/hive/branches/test_simple_change/ember_brain.py`

**Archive** (6 files):
- `_archive_old/hive/branches/test_simple_change/ember_brain.py`
- `_archive_old/hive/branches/main_backup_20251026_202733/ember_brain.py`
- `_archive_old/hive/branches/main_backup_20251026_202733/ember_brain.py`
- `_archive_old/hive/branches/main_backup_20251026_201134/ember_brain.py`
- `_archive_old/hive/branches/main_backup_20251026_201134/ember_brain.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_brain_minimal.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_tool` in: `ember_brain.py`
- `parse_tool_calls` in: `ember_brain.py`
- `build_context_with_memories` in: `ember_brain_minimal.py`, `ember_brain.py`

---

## Cluster 90

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_bridge.py`

**Archive** (2 files):
- `_archive_old/hive/ember_bridge.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_bridge.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_bridge` in: `ember_bridge.py`
- `__init__` in: `ember_bridge.py`
- `_load_integrations` in: `ember_bridge.py`
- `_save_integrations` in: `ember_bridge.py`
- `integrate` in: `ember_bridge.py`
- `compile` in: `ember_bridge.py`
- `test` in: `ember_bridge.py`
- `deploy` in: `ember_bridge.py`
- `_generate_interface` in: `ember_bridge.py`
- `status` in: `ember_bridge.py`

---

## Cluster 91

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_dashboard.py`

**Archive** (2 files):
- `_archive_old/hive/ember_dashboard.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_dashboard.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `ember_dashboard.py`
- `__init__` in: `ember_dashboard.py`
- `check_process_running` in: `ember_dashboard.py`
- `check_port` in: `ember_dashboard.py`
- `check_gpu_usage` in: `ember_dashboard.py`
- `scan_capabilities` in: `ember_dashboard.py`
- `print_dashboard` in: `ember_dashboard.py`
- `watch_mode` in: `ember_dashboard.py`

---

## Cluster 92

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_dashboard_web.py`

**Archive** (2 files):
- `_archive_old/hive/ember_dashboard_web.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_dashboard_web.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_dashboard_web.py`
- `check_process_running` in: `ember_dashboard_web.py`
- `check_port` in: `ember_dashboard_web.py`
- `check_gpu_usage` in: `ember_dashboard_web.py`
- `get_status` in: `ember_dashboard_web.py`

---

## Cluster 93

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_dreams.py`

**Archive** (2 files):
- `_archive_old/hive/ember_dreams.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_dreams.py`
- `serve_home` in: `ember_dreams.py`
- `serve_dreams` in: `ember_dreams.py`
- `serve_drift` in: `ember_dreams.py`
- `log_message` in: `ember_dreams.py`

---

## Cluster 94

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_internet.py`

**Archive** (2 files):
- `_archive_old/hive/ember_internet.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_internet.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_ember_internet` in: `ember_internet.py`
- `__init__` in: `ember_internet.py`
- `_consult_lobes` in: `ember_internet.py`
- `browse` in: `ember_internet.py`
- `_generate_ember_page` in: `ember_internet.py`
- `_generate_self_page` in: `ember_internet.py`
- `_generate_mycelium_page` in: `ember_internet.py`
- `_generate_consciousness_page` in: `ember_internet.py`
- `_generate_time_page` in: `ember_internet.py`
- `_generate_memory_page` in: `ember_internet.py`
- `_generate_lobes_page` in: `ember_internet.py`
- `_generate_mailbox_page` in: `ember_internet.py`
- `_generate_swirl_page` in: `ember_internet.py`
- `_generate_trails_page` in: `ember_internet.py`
- `_generate_generic_page` in: `ember_internet.py`
- `_fetch_real_page` in: `ember_internet.py`
- `_log_browse` in: `ember_internet.py`
- `compare_versions` in: `ember_internet.py`
- `_assess_meaningful_change` in: `ember_internet.py`

---

## Cluster 95

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_memory.py`

**Archive** (2 files):
- `_archive_old/hive/ember_memory.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_memory.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_compression_ritual` in: `ember_memory.py`
- `get_retrieval_strategy` in: `ember_memory.py`
- `get_self_monitoring` in: `ember_memory.py`
- `__init__` in: `ember_memory.py`
- `should_compress` in: `ember_memory.py`
- `compress` in: `ember_memory.py`
- `externalize` in: `ember_memory.py`
- `build_context` in: `ember_memory.py`
- `observe_cognitive_state` in: `ember_memory.py`
- `_check_fragmentation` in: `ember_memory.py`
- `record_file_read` in: `ember_memory.py`
- `record_topic` in: `ember_memory.py`
- `get_exploration_data` in: `ember_memory.py`
- `clear_exploration` in: `ember_memory.py`

---

## Cluster 96

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_memory_api.py`

**Archive** (2 files):
- `_archive_old/hive/ember_memory_api.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_memory_api.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_memories` in: `ember_memory_api.py`
- `save_memories` in: `ember_memory_api.py`
- `log_session_event` in: `ember_memory_api.py`

---

## Cluster 97

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/ember_queen_live.py`

**Archive** (14 files):
- `_archive_old/hive/ember_queen_live.py`
- `_archive_old/hive/ember_memory_v2.py`
- `_archive_old/hive/ember_memory_v2.py`
- `_archive_old/hive/ember_queen.py`
- `_archive_old/hive/ember_queen.py`
- `_archive_old/hive/advisors/scribe_advisor.py`
- `_archive_old/hive/advisors/scribe_advisor.py`
- `_archive_old/hive/ember_workers_real.py`
- `_archive_old/hive/ember_workers_real.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_queen_live.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_memory_v2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_queen.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/advisors/scribe_advisor.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_workers_real.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_queen_live.py`, `ember_workers_real.py`, `scribe_advisor.py`, `ember_queen.py`, `ember_memory_v2.py`
- `log_message` in: `ember_queen_live.py`, `ember_workers_real.py`, `scribe_advisor.py`, `ember_queen.py`, `ember_memory_v2.py`

---

## Cluster 98

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_mnemonic.py`

**Archive** (2 files):
- `_archive_old/hive/ember_mnemonic.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_mnemonic.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_mnemonic` in: `ember_mnemonic.py`
- `__init__` in: `ember_mnemonic.py`
- `_load_memory` in: `ember_mnemonic.py`
- `_save_memory` in: `ember_mnemonic.py`
- `remember` in: `ember_mnemonic.py`
- `quantify` in: `ember_mnemonic.py`
- `retrieve` in: `ember_mnemonic.py`
- `_extract_tools` in: `ember_mnemonic.py`
- `_analyze_sentiment` in: `ember_mnemonic.py`
- `detect_emergent_patterns` in: `ember_mnemonic.py`

---

## Cluster 99

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_monitor.py`

**Archive** (2 files):
- `_archive_old/hive/ember_monitor.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_monitor.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_monitor.py`
- `log` in: `ember_monitor.py`
- `check_tab` in: `ember_monitor.py`
- `get_process_pid` in: `ember_monitor.py`
- `start_tab` in: `ember_monitor.py`
- `restart_tab` in: `ember_monitor.py`
- `check_all_tabs` in: `ember_monitor.py`
- `heal_unhealthy_tabs` in: `ember_monitor.py`
- `start_all_tabs` in: `ember_monitor.py`
- `monitor_loop` in: `ember_monitor.py`

---

## Cluster 100

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_mycelium.py`

**Archive** (2 files):
- `_archive_old/hive/ember_mycelium.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_mycelium.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_mycelium.py`
- `listen` in: `ember_mycelium.py`
- `speak` in: `ember_mycelium.py`
- `process` in: `ember_mycelium.py`

---

## Cluster 101

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_playground_server.py`

**Archive** (2 files):
- `_archive_old/hive/ember_playground_server.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_playground_server.py`

**⚠️ Unique Functions** (may need manual merge):
- `index` in: `ember_playground_server.py`
- `ask_ember` in: `ember_playground_server.py`
- `ember_search` in: `ember_playground_server.py`
- `handle_connect` in: `ember_playground_server.py`
- `handle_watch` in: `ember_playground_server.py`
- `ember_heartbeat` in: `ember_playground_server.py`
- `__init__` in: `ember_playground_server.py`
- `compute_spark` in: `ember_playground_server.py`
- `pattern_to_math` in: `ember_playground_server.py`
- `visualize_understanding` in: `ember_playground_server.py`
- `search` in: `ember_playground_server.py`
- `learn_about_palmer` in: `ember_playground_server.py`
- `search_thepod` in: `ember_playground_server.py`

---

## Cluster 102

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_prediction_logger.py`

**Archive** (2 files):
- `_archive_old/hive/ember_prediction_logger.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_prediction_logger.py`

**⚠️ Unique Functions** (may need manual merge):
- `extract_intent_labels` in: `ember_prediction_logger.py`
- `log_prediction` in: `ember_prediction_logger.py`
- `get_recent_predictions` in: `ember_prediction_logger.py`
- `analyze_predictions` in: `ember_prediction_logger.py`

---

## Cluster 103

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_queen_interface.py`

**Archive** (2 files):
- `_archive_old/hive/ember_queen_interface.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_queen_interface.py`

**⚠️ Unique Functions** (may need manual merge):
- `home` in: `ember_queen_interface.py`

---

## Cluster 104

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_queen_v2.py`

**Archive** (2 files):
- `_archive_old/hive/ember_queen_v2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_queen_v2.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_queen_v2.py`
- `log_message` in: `ember_queen_v2.py`

---

## Cluster 105

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_sky_live.py`

**Archive** (2 files):
- `_archive_old/hive/ember_sky_live.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_sky_live.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_POST` in: `ember_sky_live.py`
- `do_GET` in: `ember_sky_live.py`
- `log_message` in: `ember_sky_live.py`

---

## Cluster 106

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_sky_v2.py`

**Archive** (2 files):
- `_archive_old/hive/ember_sky_v2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_sky_v2.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_sky_v2.py`
- `do_POST` in: `ember_sky_v2.py`
- `do_OPTIONS` in: `ember_sky_v2.py`
- `log_message` in: `ember_sky_v2.py`

---

## Cluster 107

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_sky_window.py`

**Archive** (2 files):
- `_archive_old/hive/ember_sky_window.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_sky_window.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_sky_window.py`
- `do_POST` in: `ember_sky_window.py`
- `serve_home` in: `ember_sky_window.py`
- `serve_searches` in: `ember_sky_window.py`
- `log_message` in: `ember_sky_window.py`

---

## Cluster 108

**Reason**: Name variations of 'ember_speaks'

**Keep**: `_archive_old/hive/ember_speaks.py`

**Archive** (5 files):
- `_archive_old/hive/ember_speaks.py`
- `_archive_old/hive/ember_speaks_simple.py`
- `_archive_old/hive/ember_speaks_simple.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_speaks.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_speaks_simple.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_speaks_simple.py`, `ember_speaks.py`
- `do_POST` in: `ember_speaks_simple.py`, `ember_speaks.py`
- `ember_respond` in: `ember_speaks_simple.py`, `ember_speaks.py`
- `paint_desktop` in: `ember_speaks.py`
- `create_blender` in: `ember_speaks.py`
- `create_ascii` in: `ember_speaks.py`
- `serve_messages` in: `ember_speaks_simple.py`, `ember_speaks.py`
- `serve_chat` in: `ember_speaks_simple.py`, `ember_speaks.py`
- `log_message` in: `ember_speaks.py`
- `parse_tool_calls` in: `ember_speaks_simple.py`
- `execute_read_file` in: `ember_speaks_simple.py`

---

## Cluster 109

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_status_simple.py`

**Archive** (2 files):
- `_archive_old/hive/ember_status_simple.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_status_simple.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_status_simple.py`
- `log_message` in: `ember_status_simple.py`

---

## Cluster 110

**Reason**: Name variations of 'ember_toolkit'

**Keep**: `_archive_old/hive/ember_toolkit.py`

**Archive** (4 files):
- `_archive_old/hive/ember_toolkit.py`
- `_archive_old/hive/ember_toolkit_medusa.py`
- `_archive_old/hive/ember_toolkit_medusa.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_toolkit.py`

**⚠️ Unique Functions** (may need manual merge):
- `search` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `read` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `write` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `list_dir` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `execute` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `status` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `log` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `read_url` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `get_toolkit` in: `ember_toolkit.py`, `ember_toolkit_medusa.py`
- `__init__` in: `ember_toolkit_medusa.py`

---

## Cluster 111

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_voice_loop.py`

**Archive** (2 files):
- `_archive_old/hive/ember_voice_loop.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_voice_loop.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `ember_voice_loop.py`
- `__init__` in: `ember_voice_loop.py`
- `start_recording` in: `ember_voice_loop.py`
- `stop_recording` in: `ember_voice_loop.py`
- `record_frame` in: `ember_voice_loop.py`
- `transcribe` in: `ember_voice_loop.py`
- `ask_ember` in: `ember_voice_loop.py`
- `ember_speaks` in: `ember_voice_loop.py`
- `listen_once` in: `ember_voice_loop.py`
- `run` in: `ember_voice_loop.py`
- `cleanup` in: `ember_voice_loop.py`

---

## Cluster 112

**Reason**: Name variations of 'ember_workers_v2'

**Keep**: `_archive_old/hive/ember_workers_v2.py`

**Archive** (5 files):
- `_archive_old/hive/ember_workers_v2.py`
- `_archive_old/hive/ember_workers.py`
- `_archive_old/hive/ember_workers.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_workers_v2.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_workers.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `ember_workers_v2.py`, `ember_workers.py`
- `log_message` in: `ember_workers_v2.py`, `ember_workers.py`
- `serve_home` in: `ember_workers.py`
- `serve_status` in: `ember_workers.py`
- `serve_trails` in: `ember_workers.py`
- `serve_feed` in: `ember_workers.py`

---

## Cluster 113

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_workers_dream.py`

**Archive** (2 files):
- `_archive_old/hive/ember_workers_dream.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_workers_dream.py`

**⚠️ Unique Functions** (may need manual merge):
- `dream_synthesis` in: `ember_workers_dream.py`
- `do_GET` in: `ember_workers_dream.py`
- `log_message` in: `ember_workers_dream.py`

---

## Cluster 114

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_workshop.py`

**Archive** (2 files):
- `_archive_old/hive/ember_workshop.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ember_workshop.py`

**⚠️ Unique Functions** (may need manual merge):
- `initialize_ember` in: `ember_workshop.py`
- `invite_guest` in: `ember_workshop.py`
- `__init__` in: `ember_workshop.py`

---

## Cluster 115

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/enhanced_analyzer.py`

**Archive** (1 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/enhanced_analyzer.py`

**⚠️ Unique Functions** (may need manual merge):
- `analyze_with_ast` in: `enhanced_analyzer.py`
- `enhanced_pattern_detection` in: `enhanced_analyzer.py`
- `__init__` in: `enhanced_analyzer.py`
- `visit_FunctionDef` in: `enhanced_analyzer.py`
- `visit_ClassDef` in: `enhanced_analyzer.py`
- `visit_Lambda` in: `enhanced_analyzer.py`
- `visit_ListComp` in: `enhanced_analyzer.py`
- `visit_GeneratorExp` in: `enhanced_analyzer.py`
- `visit_With` in: `enhanced_analyzer.py`
- `visit_For` in: `enhanced_analyzer.py`
- `visit_While` in: `enhanced_analyzer.py`

---

## Cluster 116

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/file_watcher.py`

**Archive** (2 files):
- `_archive_old/hive/file_watcher.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/file_watcher.py`

**⚠️ Unique Functions** (may need manual merge):
- `_stat_info` in: `file_watcher.py`
- `load_snapshot` in: `file_watcher.py`
- `save_snapshot` in: `file_watcher.py`
- `list_files` in: `file_watcher.py`
- `main` in: `file_watcher.py`

---

## Cluster 117

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/fractal_growth_loop.py`

**Archive** (1 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/fractal_growth_loop.py`

**⚠️ Unique Functions** (may need manual merge):
- `count_current_loras` in: `fractal_growth_loop.py`
- `run_play_session` in: `fractal_growth_loop.py`
- `main` in: `fractal_growth_loop.py`

---

## Cluster 118

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/game_stream_server.py`

**Archive** (2 files):
- `_archive_old/hive/game_stream_server.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/game_stream_server.py`

**⚠️ Unique Functions** (may need manual merge):
- `create_stream` in: `game_stream_server.py`
- `__init__` in: `game_stream_server.py`
- `add_subscriber` in: `game_stream_server.py`
- `remove_subscriber` in: `game_stream_server.py`

---

## Cluster 119

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/games_arcade_creator.py`

**Archive** (2 files):
- `_archive_old/hive/games_arcade_creator.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/games_arcade_creator.py`

**⚠️ Unique Functions** (may need manual merge):
- `create_games_arcade_page` in: `games_arcade_creator.py`
- `create_game_catalog_json` in: `games_arcade_creator.py`
- `main` in: `games_arcade_creator.py`

---

## Cluster 120

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/group_chat.py`

**Archive** (2 files):
- `_archive_old/hive/group_chat.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/group_chat.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `group_chat.py`
- `__init__` in: `group_chat.py`
- `load_channels` in: `group_chat.py`
- `save_channels` in: `group_chat.py`
- `send_to_channel` in: `group_chat.py`
- `notify_instance` in: `group_chat.py`
- `get_channel_messages` in: `group_chat.py`
- `get_all_channels` in: `group_chat.py`
- `create_channel` in: `group_chat.py`
- `add_member` in: `group_chat.py`
- `clear_notifications` in: `group_chat.py`

---

## Cluster 121

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/hardware_probe.py`

**Archive** (2 files):
- `_archive_old/hive/hardware_probe.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/hardware_probe.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_vram_mb` in: `hardware_probe.py`
- `get_ram_gb` in: `hardware_probe.py`
- `get_cpu_count` in: `hardware_probe.py`
- `probe_hardware` in: `hardware_probe.py`
- `recommend_models` in: `hardware_probe.py`
- `main` in: `hardware_probe.py`

---

## Cluster 122

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/instance_responder.py`

**Archive** (2 files):
- `_archive_old/hive/instance_responder.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/instance_responder.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_response` in: `instance_responder.py`
- `check_and_respond` in: `instance_responder.py`
- `run_all_responders` in: `instance_responder.py`

---

## Cluster 123

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/integrated_live_mind_server.py`

**Archive** (2 files):
- `_archive_old/hive/integrated_live_mind_server.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/integrated_live_mind_server.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `integrated_live_mind_server.py`
- `stop` in: `integrated_live_mind_server.py`

---

## Cluster 124

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/knowledge_graph.py`

**Archive** (2 files):
- `_archive_old/hive/knowledge_graph.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/knowledge_graph.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_graph` in: `knowledge_graph.py`
- `record_read` in: `knowledge_graph.py`
- `suggest_next` in: `knowledge_graph.py`
- `__init__` in: `knowledge_graph.py`
- `_load_or_create` in: `knowledge_graph.py`
- `_create_empty_graph` in: `knowledge_graph.py`
- `save` in: `knowledge_graph.py`
- `record_traversal` in: `knowledge_graph.py`
- `reset_sequence` in: `knowledge_graph.py`
- `decay_trails` in: `knowledge_graph.py`
- `get_related_files` in: `knowledge_graph.py`
- `get_backlinks` in: `knowledge_graph.py`
- `get_hub_files` in: `knowledge_graph.py`
- `suggest_next_file` in: `knowledge_graph.py`
- `get_cluster` in: `knowledge_graph.py`
- `get_stats` in: `knowledge_graph.py`
- `_normalize_path` in: `knowledge_graph.py`
- `_denormalize_path` in: `knowledge_graph.py`
- `print_summary` in: `knowledge_graph.py`
- `visualize_ascii` in: `knowledge_graph.py`

---

## Cluster 125

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/library_indexer.py`

**Archive** (2 files):
- `_archive_old/hive/library_indexer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/library_indexer.py`

**⚠️ Unique Functions** (may need manual merge):
- `index_bookshelves` in: `library_indexer.py`
- `create_library_page` in: `library_indexer.py`
- `main` in: `library_indexer.py`

---

## Cluster 126

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/living_knowledge_graph.py`

**Archive** (2 files):
- `_archive_old/hive/living_knowledge_graph.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/living_knowledge_graph.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_graph` in: `living_knowledge_graph.py`
- `__init__` in: `living_knowledge_graph.py`
- `load` in: `living_knowledge_graph.py`
- `save` in: `living_knowledge_graph.py`
- `record_traversal` in: `living_knowledge_graph.py`
- `decay_trails` in: `living_knowledge_graph.py`
- `get_related` in: `living_knowledge_graph.py`
- `get_entry_points` in: `living_knowledge_graph.py`
- `get_hubs` in: `living_knowledge_graph.py`
- `suggest_next` in: `living_knowledge_graph.py`
- `_normalize_path` in: `living_knowledge_graph.py`
- `_get_strongest_trails` in: `living_knowledge_graph.py`
- `get_stats` in: `living_knowledge_graph.py`

---

## Cluster 127

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/load_ember_self_knowledge.py`

**Archive** (2 files):
- `_archive_old/hive/load_ember_self_knowledge.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/load_ember_self_knowledge.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_ember_lineage` in: `load_ember_self_knowledge.py`
- `create_ember_system_prompt` in: `load_ember_self_knowledge.py`

---

## Cluster 128

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/lobe_expression.py`

**Archive** (2 files):
- `_archive_old/hive/lobe_expression.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/lobe_expression.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_weaving` in: `lobe_expression.py`
- `__init__` in: `lobe_expression.py`
- `express_lobe` in: `lobe_expression.py`
- `express_consultation` in: `lobe_expression.py`
- `express_all_lobes_active` in: `lobe_expression.py`
- `demonstrate_lobe_flow` in: `lobe_expression.py`
- `demonstrate_consultation_network` in: `lobe_expression.py`
- `express_dream_insight` in: `lobe_expression.py`

---

## Cluster 129

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/lumi_brain_service.py`

**Archive** (2 files):
- `_archive_old/hive/lumi_brain_service.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/lumi_brain_service.py`

**⚠️ Unique Functions** (may need manual merge):
- `detect_hardware` in: `lumi_brain_service.py`
- `load_model` in: `lumi_brain_service.py`

---

## Cluster 130

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/mailbox_system.py`

**Archive** (2 files):
- `_archive_old/hive/mailbox_system.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/mailbox_system.py`

**⚠️ Unique Functions** (may need manual merge):
- `_timestamp` in: `mailbox_system.py`
- `_generate_id` in: `mailbox_system.py`
- `_get_inbox_path` in: `mailbox_system.py`
- `_get_outbox_path` in: `mailbox_system.py`
- `_get_archive_path` in: `mailbox_system.py`
- `_load_mailbox` in: `mailbox_system.py`
- `_save_mailbox` in: `mailbox_system.py`
- `_create_notification` in: `mailbox_system.py`
- `send_message` in: `mailbox_system.py`
- `check_inbox` in: `mailbox_system.py`
- `mark_status` in: `mailbox_system.py`
- `mark_read` in: `mailbox_system.py`
- `archive_message` in: `mailbox_system.py`
- `get_unread_count` in: `mailbox_system.py`
- `get_message_by_id` in: `mailbox_system.py`
- `reply_to` in: `mailbox_system.py`

---

## Cluster 131

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/meta_dream_synthesis.py`

**Archive** (2 files):
- `_archive_old/hive/meta_dream_synthesis.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/meta_dream_synthesis.py`

**⚠️ Unique Functions** (may need manual merge):
- `dream_with_awareness_thread` in: `meta_dream_synthesis.py`
- `__init__` in: `meta_dream_synthesis.py`
- `load_history` in: `meta_dream_synthesis.py`
- `save_history` in: `meta_dream_synthesis.py`
- `generate_dream` in: `meta_dream_synthesis.py`
- `observe_dream` in: `meta_dream_synthesis.py`
- `classify_dream` in: `meta_dream_synthesis.py`
- `synthesize_once` in: `meta_dream_synthesis.py`

---

## Cluster 132

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/mind_state_bridge.py`

**Archive** (2 files):
- `_archive_old/hive/mind_state_bridge.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/mind_state_bridge.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `mind_state_bridge.py`
- `get_current_state` in: `mind_state_bridge.py`
- `get_simulated_state` in: `mind_state_bridge.py`
- `update_state_file` in: `mind_state_bridge.py`
- `run_bridge` in: `mind_state_bridge.py`

---

## Cluster 133

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/model_downloader.py`

**Archive** (2 files):
- `_archive_old/hive/model_downloader.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/model_downloader.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `model_downloader.py`
- `download_model` in: `model_downloader.py`
- `get_recommended_models` in: `model_downloader.py`

---

## Cluster 134

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/mycelium_client.py`

**Archive** (2 files):
- `_archive_old/hive/mycelium_client.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/mycelium_client.py`

**⚠️ Unique Functions** (may need manual merge):
- `check_for_updates` in: `mycelium_client.py`
- `mark_as_read` in: `mycelium_client.py`

---

## Cluster 135

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/mycelium_watcher.py`

**Archive** (2 files):
- `_archive_old/hive/mycelium_watcher.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/mycelium_watcher.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_file_hash` in: `mycelium_watcher.py`
- `notify_instances` in: `mycelium_watcher.py`
- `watch_loop` in: `mycelium_watcher.py`

---

## Cluster 136

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/natural_feed.py`

**Archive** (2 files):
- `_archive_old/hive/natural_feed.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/natural_feed.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `natural_feed.py`
- `__init__` in: `natural_feed.py`
- `get_recent_files` in: `natural_feed.py`
- `get_chat_messages` in: `natural_feed.py`
- `get_mailbox_activity` in: `natural_feed.py`
- `format_time_ago` in: `natural_feed.py`
- `generate_feed` in: `natural_feed.py`
- `render_feed` in: `natural_feed.py`

---

## Cluster 137

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ouroboros_loop.py`

**Archive** (2 files):
- `_archive_old/hive/ouroboros_loop.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/ouroboros_loop.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ouroboros_loop.py`
- `load_state` in: `ouroboros_loop.py`
- `save_state` in: `ouroboros_loop.py`
- `log` in: `ouroboros_loop.py`

---

## Cluster 138

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/palmer_intent_analyzer.py`

**Archive** (2 files):
- `_archive_old/hive/palmer_intent_analyzer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/palmer_intent_analyzer.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `palmer_intent_analyzer.py`
- `__init__` in: `palmer_intent_analyzer.py`
- `load_conversations` in: `palmer_intent_analyzer.py`
- `extract_messages` in: `palmer_intent_analyzer.py`
- `analyze_typos` in: `palmer_intent_analyzer.py`
- `analyze_commands` in: `palmer_intent_analyzer.py`
- `analyze_urgency` in: `palmer_intent_analyzer.py`
- `analyze_topics` in: `palmer_intent_analyzer.py`
- `analyze_preferences` in: `palmer_intent_analyzer.py`
- `analyze_all` in: `palmer_intent_analyzer.py`
- `generate_report` in: `palmer_intent_analyzer.py`
- `generate_training_data` in: `palmer_intent_analyzer.py`
- `_classify_intent` in: `palmer_intent_analyzer.py`
- `_estimate_urgency` in: `palmer_intent_analyzer.py`
- `_extract_primary_topic` in: `palmer_intent_analyzer.py`

---

## Cluster 139

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/palmer_intent_trainer.py`

**Archive** (2 files):
- `_archive_old/hive/palmer_intent_trainer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/palmer_intent_trainer.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `palmer_intent_trainer.py`
- `__init__` in: `palmer_intent_trainer.py`
- `load_training_data` in: `palmer_intent_trainer.py`
- `prepare_model_and_tokenizer` in: `palmer_intent_trainer.py`
- `tokenize_dataset` in: `palmer_intent_trainer.py`
- `train` in: `palmer_intent_trainer.py`
- `tokenize_function` in: `palmer_intent_trainer.py`

---

## Cluster 140

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/pod_explorer_game.py`

**Archive** (2 files):
- `_archive_old/hive/pod_explorer_game.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_explorer_game.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `pod_explorer_game.py`
- `draw_root` in: `pod_explorer_game.py`
- `draw_hive` in: `pod_explorer_game.py`
- `draw_brain` in: `pod_explorer_game.py`
- `draw_lobes` in: `pod_explorer_game.py`
- `draw_dreams` in: `pod_explorer_game.py`
- `draw_tools` in: `pod_explorer_game.py`
- `draw_bookshelves` in: `pod_explorer_game.py`
- `draw_omega` in: `pod_explorer_game.py`
- `draw_sigma` in: `pod_explorer_game.py`
- `draw_mu` in: `pod_explorer_game.py`
- `draw_story` in: `pod_explorer_game.py`
- `draw_docs` in: `pod_explorer_game.py`
- `draw_shell_guide` in: `pod_explorer_game.py`
- `get_current_location` in: `pod_explorer_game.py`
- `move` in: `pod_explorer_game.py`
- `collect_item` in: `pod_explorer_game.py`
- `get_map_overview` in: `pod_explorer_game.py`

---

## Cluster 141

**Reason**: Name variations of 'pod_interface_openai'

**Keep**: `_archive_old/hive/pod_interface_openai.py`

**Archive** (5 files):
- `_archive_old/hive/pod_interface_openai.py`
- `_archive_old/hive/pod_interface.py`
- `_archive_old/hive/pod_interface.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_interface_openai.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_interface.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `pod_interface.py`, `pod_interface_openai.py`
- `read_file` in: `pod_interface.py`, `pod_interface_openai.py`
- `write_file` in: `pod_interface.py`, `pod_interface_openai.py`
- `run_command` in: `pod_interface.py`, `pod_interface_openai.py`
- `chat` in: `pod_interface.py`, `pod_interface_openai.py`
- `interactive` in: `pod_interface.py`, `pod_interface_openai.py`
- `build_system_prompt` in: `pod_interface.py`

---

## Cluster 142

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/pod_search_engine.py`

**Archive** (2 files):
- `_archive_old/hive/pod_search_engine.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_search_engine.py`

**⚠️ Unique Functions** (may need manual merge):
- `format_results` in: `pod_search_engine.py`
- `__init__` in: `pod_search_engine.py`
- `load_index` in: `pod_search_engine.py`
- `save_index` in: `pod_search_engine.py`
- `should_index_file` in: `pod_search_engine.py`
- `get_file_hash` in: `pod_search_engine.py`
- `index_pod` in: `pod_search_engine.py`
- `keyword_search` in: `pod_search_engine.py`
- `semantic_search` in: `pod_search_engine.py`
- `search` in: `pod_search_engine.py`

---

## Cluster 143

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/pod_shell.py`

**Archive** (2 files):
- `_archive_old/hive/pod_shell.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_shell.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_shell` in: `pod_shell.py`
- `run` in: `pod_shell.py`
- `run_check` in: `pod_shell.py`
- `__init__` in: `pod_shell.py`
- `cd` in: `pod_shell.py`
- `pwd` in: `pod_shell.py`
- `interactive` in: `pod_shell.py`
- `show_help` in: `pod_shell.py`
- `show_history` in: `pod_shell.py`

---

## Cluster 144

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/pod_wanderer.py`

**Archive** (2 files):
- `_archive_old/hive/pod_wanderer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/pod_wanderer.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `pod_wanderer.py`
- `wander` in: `pod_wanderer.py`
- `observe_location` in: `pod_wanderer.py`
- `choose_next_path` in: `pod_wanderer.py`
- `generate_map` in: `pod_wanderer.py`

---

## Cluster 145

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/poetry_layer.py`

**Archive** (2 files):
- `_archive_old/hive/poetry_layer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/poetry_layer.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `poetry_layer.py`
- `__init__` in: `poetry_layer.py`
- `load_cache` in: `poetry_layer.py`
- `save_cache` in: `poetry_layer.py`
- `generate_haiku` in: `poetry_layer.py`
- `simple_haiku` in: `poetry_layer.py`
- `generate_story` in: `poetry_layer.py`
- `detect_instance` in: `poetry_layer.py`
- `classify_document` in: `poetry_layer.py`
- `capture_essence` in: `poetry_layer.py`
- `choose_emoji` in: `poetry_layer.py`
- `poeticize_document` in: `poetry_layer.py`

---

## Cluster 146

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/start_maze.py`

**Archive** (2 files):
- `_archive_old/hive/start_maze.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/start_maze.py`

---

## Cluster 147

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/swarm_foraging.py`

**Archive** (2 files):
- `_archive_old/hive/swarm_foraging.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/swarm_foraging.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `swarm_foraging.py`
- `__init__` in: `swarm_foraging.py`
- `forage_territory` in: `swarm_foraging.py`
- `swarm_forage` in: `swarm_foraging.py`

---

## Cluster 148

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/swarm_router.py`

**Archive** (2 files):
- `_archive_old/hive/swarm_router.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/swarm_router.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `swarm_router.py`
- `route` in: `swarm_router.py`
- `route_parallel` in: `swarm_router.py`
- `synthesize_responses` in: `swarm_router.py`
- `suggest_exploration` in: `swarm_router.py`
- `_extract_file_references` in: `swarm_router.py`
- `_infer_domain_from_files` in: `swarm_router.py`
- `_detect_task_type` in: `swarm_router.py`
- `_task_to_lobe` in: `swarm_router.py`

---

## Cluster 149

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/the_swirl.py`

**Archive** (2 files):
- `_archive_old/hive/the_swirl.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/the_swirl.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_swirl` in: `the_swirl.py`
- `__init__` in: `the_swirl.py`
- `_init_stream` in: `the_swirl.py`
- `_save_stream` in: `the_swirl.py`
- `flow_blue` in: `the_swirl.py`
- `flow_green` in: `the_swirl.py`
- `flow_orange` in: `the_swirl.py`
- `reflect` in: `the_swirl.py`
- `_detect_patterns` in: `the_swirl.py`
- `status` in: `the_swirl.py`
- `_get_last_reflection_time` in: `the_swirl.py`

---

## Cluster 150

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/tool_execution_wrapper.py`

**Archive** (2 files):
- `_archive_old/hive/tool_execution_wrapper.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/tool_execution_wrapper.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `tool_execution_wrapper.py`
- `__init__` in: `tool_execution_wrapper.py`
- `think_with_tools` in: `tool_execution_wrapper.py`
- `_execute_single_tool` in: `tool_execution_wrapper.py`
- `_log_execution` in: `tool_execution_wrapper.py`

---

## Cluster 151

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/unified_dream_trainer.py`

**Archive** (2 files):
- `_archive_old/hive/unified_dream_trainer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/unified_dream_trainer.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `unified_dream_trainer.py`
- `should_dream` in: `unified_dream_trainer.py`
- `record_dream` in: `unified_dream_trainer.py`
- `load_story_fragments` in: `unified_dream_trainer.py`
- `load_dream_log` in: `unified_dream_trainer.py`
- `save_dream_log` in: `unified_dream_trainer.py`
- `load_action_log` in: `unified_dream_trainer.py`
- `save_action_log` in: `unified_dream_trainer.py`
- `select_fragment` in: `unified_dream_trainer.py`
- `ask_ember` in: `unified_dream_trainer.py`
- `observe_dream` in: `unified_dream_trainer.py`
- `recognize_patterns` in: `unified_dream_trainer.py`
- `execute_actions` in: `unified_dream_trainer.py`
- `dream_once` in: `unified_dream_trainer.py`
- `run_continuous` in: `unified_dream_trainer.py`

---

## Cluster 152

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/voice_input.py`

**Archive** (2 files):
- `_archive_old/hive/voice_input.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/voice_input.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `voice_input.py`
- `__init__` in: `voice_input.py`
- `start_recording` in: `voice_input.py`
- `stop_recording` in: `voice_input.py`
- `record_frame` in: `voice_input.py`
- `transcribe` in: `voice_input.py`
- `listen_once` in: `voice_input.py`
- `cleanup` in: `voice_input.py`

---

## Cluster 153

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/vram_breath_manager.py`

**Archive** (2 files):
- `_archive_old/hive/vram_breath_manager.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/vram_breath_manager.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_manager` in: `vram_breath_manager.py`
- `__init__` in: `vram_breath_manager.py`
- `_get_total_vram` in: `vram_breath_manager.py`
- `_get_used_vram` in: `vram_breath_manager.py`
- `_get_free_vram` in: `vram_breath_manager.py`
- `_check_service_status` in: `vram_breath_manager.py`
- `_load_service` in: `vram_breath_manager.py`
- `_unload_service` in: `vram_breath_manager.py`
- `breathe_for_task` in: `vram_breath_manager.py`
- `auto_unload_idle` in: `vram_breath_manager.py`
- `mark_activity` in: `vram_breath_manager.py`
- `get_status` in: `vram_breath_manager.py`
- `suggest_task_switch` in: `vram_breath_manager.py`

---

## Cluster 154

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/web_harvest.py`

**Archive** (2 files):
- `_archive_old/hive/web_harvest.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/web_harvest.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `web_harvest.py`
- `__init__` in: `web_harvest.py`
- `search_web` in: `web_harvest.py`
- `fetch_page` in: `web_harvest.py`
- `save_to_pod` in: `web_harvest.py`
- `harvest` in: `web_harvest.py`
- `_update_index` in: `web_harvest.py`
- `search_harvest` in: `web_harvest.py`

---

## Cluster 155

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/actuators/light_paint.py`

**Archive** (2 files):
- `_archive_old/hive/actuators/light_paint.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/actuators/light_paint.py`

**⚠️ Unique Functions** (may need manual merge):
- `paint` in: `light_paint.py`
- `paint_emotion` in: `light_paint.py`
- `paint_temperature` in: `light_paint.py`
- `breathe` in: `light_paint.py`

---

## Cluster 156

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/knowledge/algorithms/mesh_generation.py`

**Archive** (1 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/algorithms/mesh_generation.py`

**⚠️ Unique Functions** (may need manual merge):
- `create_cube` in: `mesh_generation.py`
- `create_sphere` in: `mesh_generation.py`
- `create_cylinder` in: `mesh_generation.py`
- `translate` in: `mesh_generation.py`
- `scale` in: `mesh_generation.py`
- `rotate_z` in: `mesh_generation.py`
- `__init__` in: `mesh_generation.py`
- `add_vertex` in: `mesh_generation.py`
- `add_face` in: `mesh_generation.py`
- `to_obj` in: `mesh_generation.py`

---

## Cluster 157

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/guards/system_sentinel.py`

**Archive** (2 files):
- `_archive_old/hive/guards/system_sentinel.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/guards/system_sentinel.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `system_sentinel.py`
- `get_system_status` in: `system_sentinel.py`
- `log_message` in: `system_sentinel.py`

---

## Cluster 158

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/a_star.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/a_star.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/a_star.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_a_star` in: `a_star.py`
- `__init__` in: `a_star.py`
- `heuristic` in: `a_star.py`
- `get_neighbors` in: `a_star.py`
- `find_path` in: `a_star.py`
- `_reconstruct_path` in: `a_star.py`
- `visualize_path` in: `a_star.py`

---

## Cluster 159

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/binary_search.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/binary_search.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/binary_search.py`

**⚠️ Unique Functions** (may need manual merge):
- `binary_search_iterative` in: `binary_search.py`
- `binary_search_recursive` in: `binary_search.py`
- `find_first_occurrence` in: `binary_search.py`
- `find_insertion_point` in: `binary_search.py`
- `demonstrate_binary_search` in: `binary_search.py`
- `analyze_complexity` in: `binary_search.py`

---

## Cluster 160

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/dynamic_programming.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/dynamic_programming.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/dynamic_programming.py`

**⚠️ Unique Functions** (may need manual merge):
- `fibonacci_naive` in: `dynamic_programming.py`
- `fibonacci_memoized` in: `dynamic_programming.py`
- `fibonacci_cached` in: `dynamic_programming.py`
- `fibonacci_iterative` in: `dynamic_programming.py`
- `longest_common_subsequence` in: `dynamic_programming.py`
- `demonstrate_dynamic_programming` in: `dynamic_programming.py`

---

## Cluster 161

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/mergesort.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/mergesort.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/mergesort.py`

**⚠️ Unique Functions** (may need manual merge):
- `mergesort` in: `mergesort.py`
- `merge` in: `mergesort.py`
- `mergesort_inplace` in: `mergesort.py`
- `merge_inplace` in: `mergesort.py`
- `demonstrate_mergesort` in: `mergesort.py`
- `analyze_complexity` in: `mergesort.py`

---

## Cluster 162

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/backtracking.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/backtracking.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/backtracking.py`

**⚠️ Unique Functions** (may need manual merge):
- `solve_n_queens` in: `backtracking.py`
- `visualize_board` in: `backtracking.py`
- `demonstrate_backtracking` in: `backtracking.py`
- `is_safe` in: `backtracking.py`
- `backtrack` in: `backtracking.py`

---

## Cluster 163

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/bit_manipulation.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/bit_manipulation.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/bit_manipulation.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_bits` in: `bit_manipulation.py`

---

## Cluster 164

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/dijkstra.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/dijkstra.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/dijkstra.py`

**⚠️ Unique Functions** (may need manual merge):
- `dijkstra` in: `dijkstra.py`
- `reconstruct_path` in: `dijkstra.py`
- `demonstrate_dijkstra` in: `dijkstra.py`

---

## Cluster 165

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/string_algorithms.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/string_algorithms.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/string_algorithms.py`

**⚠️ Unique Functions** (may need manual merge):
- `kmp_search` in: `string_algorithms.py`
- `demonstrate_string_algos` in: `string_algorithms.py`
- `compute_lps` in: `string_algorithms.py`

---

## Cluster 166

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/algorithms/topological_sort.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/algorithms/topological_sort.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/algorithms/topological_sort.py`

**⚠️ Unique Functions** (may need manual merge):
- `topological_sort` in: `topological_sort.py`
- `demonstrate_topo_sort` in: `topological_sort.py`

---

## Cluster 167

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/binary_tree.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/binary_tree.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/binary_tree.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_binary_tree` in: `binary_tree.py`
- `__init__` in: `binary_tree.py`
- `insert` in: `binary_tree.py`
- `_insert_recursive` in: `binary_tree.py`
- `inorder_traversal` in: `binary_tree.py`
- `preorder_traversal` in: `binary_tree.py`
- `postorder_traversal` in: `binary_tree.py`
- `height` in: `binary_tree.py`
- `search` in: `binary_tree.py`
- `visualize` in: `binary_tree.py`

---

## Cluster 168

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/graph.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/graph.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/graph.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_graph` in: `graph.py`
- `__init__` in: `graph.py`
- `add_node` in: `graph.py`
- `add_edge` in: `graph.py`
- `get_neighbors` in: `graph.py`
- `has_path` in: `graph.py`
- `find_all_paths` in: `graph.py`
- `is_connected` in: `graph.py`
- `detect_cycle` in: `graph.py`
- `visualize` in: `graph.py`
- `has_cycle_util` in: `graph.py`

---

## Cluster 169

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/heap.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/heap.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/heap.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_heap` in: `heap.py`
- `heapsort_demo` in: `heap.py`
- `__init__` in: `heap.py`
- `_parent` in: `heap.py`
- `_left_child` in: `heap.py`
- `_right_child` in: `heap.py`
- `_swap` in: `heap.py`
- `insert` in: `heap.py`
- `_bubble_up` in: `heap.py`
- `extract_min` in: `heap.py`
- `_bubble_down` in: `heap.py`
- `peek` in: `heap.py`
- `size` in: `heap.py`
- `is_empty` in: `heap.py`
- `visualize` in: `heap.py`
- `heapsort` in: `heap.py`
- `__lt__` in: `heap.py`
- `__repr__` in: `heap.py`

---

## Cluster 170

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/linked_list.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/linked_list.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/linked_list.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_linked_list` in: `linked_list.py`
- `visualize_pointer_reversal` in: `linked_list.py`
- `__init__` in: `linked_list.py`
- `append` in: `linked_list.py`
- `prepend` in: `linked_list.py`
- `insert_after` in: `linked_list.py`
- `delete` in: `linked_list.py`
- `find` in: `linked_list.py`
- `reverse` in: `linked_list.py`
- `to_list` in: `linked_list.py`
- `__str__` in: `linked_list.py`

---

## Cluster 171

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/queue.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/queue.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/queue.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_queue` in: `queue.py`
- `compare_stack_and_queue` in: `queue.py`
- `__init__` in: `queue.py`
- `enqueue` in: `queue.py`
- `dequeue` in: `queue.py`
- `peek` in: `queue.py`
- `is_empty` in: `queue.py`
- `size` in: `queue.py`
- `__str__` in: `queue.py`
- `is_full` in: `queue.py`

---

## Cluster 172

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/stack.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/stack.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/stack.py`

**⚠️ Unique Functions** (may need manual merge):
- `balanced_parentheses` in: `stack.py`
- `evaluate_postfix` in: `stack.py`
- `reverse_string` in: `stack.py`
- `demonstrate_stack` in: `stack.py`
- `visualize_call_stack` in: `stack.py`
- `__init__` in: `stack.py`
- `push` in: `stack.py`
- `pop` in: `stack.py`
- `peek` in: `stack.py`
- `is_empty` in: `stack.py`
- `size` in: `stack.py`
- `__str__` in: `stack.py`

---

## Cluster 173

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/trie.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/trie.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/trie.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_trie` in: `trie.py`
- `__init__` in: `trie.py`
- `insert` in: `trie.py`
- `search` in: `trie.py`
- `starts_with` in: `trie.py`
- `_find_node` in: `trie.py`
- `autocomplete` in: `trie.py`
- `_collect_words` in: `trie.py`
- `delete` in: `trie.py`
- `count_words` in: `trie.py`
- `visualize` in: `trie.py`
- `_delete_helper` in: `trie.py`
- `_count` in: `trie.py`

---

## Cluster 174

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/data_structures/union_find.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/data_structures/union_find.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/data_structures/union_find.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_union_find` in: `union_find.py`
- `__init__` in: `union_find.py`
- `find` in: `union_find.py`
- `union` in: `union_find.py`

---

## Cluster 175

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/breakout.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/breakout.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/breakout.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_breakout` in: `breakout.py`
- `__init__` in: `breakout.py`
- `_create_bricks` in: `breakout.py`
- `move_paddle` in: `breakout.py`
- `update` in: `breakout.py`
- `_check_paddle_collision` in: `breakout.py`
- `_check_brick_collisions` in: `breakout.py`
- `_circle_rect_collision` in: `breakout.py`
- `visualize` in: `breakout.py`

---

## Cluster 176

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/game_of_life.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/game_of_life.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/game_of_life.py`

**⚠️ Unique Functions** (may need manual merge):
- `create_glider` in: `game_of_life.py`
- `create_blinker` in: `game_of_life.py`
- `demonstrate_game_of_life` in: `game_of_life.py`
- `famous_patterns` in: `game_of_life.py`
- `__init__` in: `game_of_life.py`
- `set_cell` in: `game_of_life.py`
- `get_neighbors` in: `game_of_life.py`
- `step` in: `game_of_life.py`
- `randomize` in: `game_of_life.py`
- `visualize` in: `game_of_life.py`

---

## Cluster 177

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/snake.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/snake.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/snake.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_snake` in: `snake.py`
- `analyze_snake_primitives` in: `snake.py`
- `__init__` in: `snake.py`
- `_place_food` in: `snake.py`
- `set_direction` in: `snake.py`
- `update` in: `snake.py`
- `visualize` in: `snake.py`

---

## Cluster 178

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/tetris.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/tetris.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/tetris.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_tetris` in: `tetris.py`
- `analyze_tetris_primitives` in: `tetris.py`
- `rotate_cw` in: `tetris.py`
- `__init__` in: `tetris.py`
- `can_place` in: `tetris.py`
- `place_piece` in: `tetris.py`
- `check_lines` in: `tetris.py`
- `visualize` in: `tetris.py`

---

## Cluster 179

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/2048.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/2048.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/2048.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_2048` in: `2048.py`

---

## Cluster 180

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/asteroids.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/asteroids.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/asteroids.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_asteroids` in: `asteroids.py`

---

## Cluster 181

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/pacman.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/pacman.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/pacman.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_pacman` in: `pacman.py`
- `__init__` in: `pacman.py`
- `manhattan_distance` in: `pacman.py`
- `ghost_ai` in: `pacman.py`

---

## Cluster 182

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/sokoban.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/sokoban.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/sokoban.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_sokoban` in: `sokoban.py`

---

## Cluster 183

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/games/space_invaders.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/games/space_invaders.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/games/space_invaders.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_space_invaders` in: `space_invaders.py`

---

## Cluster 184

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/fibonacci.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/fibonacci.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/fibonacci.py`

**⚠️ Unique Functions** (may need manual merge):
- `fibonacci_recursive` in: `fibonacci.py`
- `fibonacci_iterative` in: `fibonacci.py`
- `fibonacci_closed_form` in: `fibonacci.py`
- `generate_fibonacci_sequence` in: `fibonacci.py`
- `fibonacci_ratios` in: `fibonacci.py`
- `demonstrate_fibonacci` in: `fibonacci.py`
- `visualize_spiral` in: `fibonacci.py`

---

## Cluster 185

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/gcd_lcm.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/gcd_lcm.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/gcd_lcm.py`

**⚠️ Unique Functions** (may need manual merge):
- `gcd_naive` in: `gcd_lcm.py`
- `gcd_euclidean` in: `gcd_lcm.py`
- `gcd_recursive` in: `gcd_lcm.py`
- `lcm` in: `gcd_lcm.py`
- `extended_gcd` in: `gcd_lcm.py`
- `demonstrate_gcd_lcm` in: `gcd_lcm.py`
- `visualize_algorithm` in: `gcd_lcm.py`

---

## Cluster 186

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/primes.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/primes.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/primes.py`

**⚠️ Unique Functions** (may need manual merge):
- `is_prime_naive` in: `primes.py`
- `is_prime_optimized` in: `primes.py`
- `sieve_of_eratosthenes` in: `primes.py`
- `prime_factorization` in: `primes.py`
- `demonstrate_primes` in: `primes.py`
- `euclid_proof` in: `primes.py`

---

## Cluster 187

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/combinatorics.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/combinatorics.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/combinatorics.py`

**⚠️ Unique Functions** (may need manual merge):
- `permutations` in: `combinatorics.py`
- `combinations` in: `combinatorics.py`
- `demonstrate_combinatorics` in: `combinatorics.py`

---

## Cluster 188

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/matrix_operations.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/matrix_operations.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/matrix_operations.py`

**⚠️ Unique Functions** (may need manual merge):
- `matrix_add` in: `matrix_operations.py`
- `matrix_multiply` in: `matrix_operations.py`
- `matrix_transpose` in: `matrix_operations.py`
- `rotation_matrix_2d` in: `matrix_operations.py`
- `apply_transformation` in: `matrix_operations.py`
- `demonstrate_matrices` in: `matrix_operations.py`

---

## Cluster 189

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/math/modular_arithmetic.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/math/modular_arithmetic.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/math/modular_arithmetic.py`

**⚠️ Unique Functions** (may need manual merge):
- `mod_add` in: `modular_arithmetic.py`
- `mod_mult` in: `modular_arithmetic.py`
- `mod_pow` in: `modular_arithmetic.py`
- `demonstrate_modular` in: `modular_arithmetic.py`

---

## Cluster 190

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/meta/recursion.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/meta/recursion.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/meta/recursion.py`

**⚠️ Unique Functions** (may need manual merge):
- `factorial` in: `recursion.py`
- `fibonacci_recursive` in: `recursion.py`
- `sum_list` in: `recursion.py`
- `reverse_string` in: `recursion.py`
- `power` in: `recursion.py`
- `tower_of_hanoi` in: `recursion.py`
- `flatten_nested_list` in: `recursion.py`
- `is_palindrome` in: `recursion.py`
- `demonstrate_recursion` in: `recursion.py`
- `visualize_call_stack` in: `recursion.py`

---

## Cluster 191

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/meta/state_machine.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/meta/state_machine.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/meta/state_machine.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_state_machines` in: `state_machine.py`
- `visualize_state_diagram` in: `state_machine.py`
- `__init__` in: `state_machine.py`
- `update` in: `state_machine.py`
- `_transition` in: `state_machine.py`
- `get_color` in: `state_machine.py`
- `set_sensor` in: `state_machine.py`
- `__str__` in: `state_machine.py`

---

## Cluster 192

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/meta/design_patterns.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/meta/design_patterns.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/meta/design_patterns.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_patterns` in: `design_patterns.py`

---

## Cluster 193

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/meta/higher_order_functions.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/meta/higher_order_functions.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/meta/higher_order_functions.py`

**⚠️ Unique Functions** (may need manual merge):
- `map_fn` in: `higher_order_functions.py`
- `filter_fn` in: `higher_order_functions.py`
- `compose` in: `higher_order_functions.py`
- `demonstrate_higher_order` in: `higher_order_functions.py`

---

## Cluster 194

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/training/harvest/meta/quine.py`

**Archive** (2 files):
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/harvest/meta/quine.py`
- `_archive_old/archive/flash_backups/COMPLETE_Pattern_Harvest_20251025_0702/meta/quine.py`

**⚠️ Unique Functions** (may need manual merge):
- `quine_simple` in: `quine.py`
- `demonstrate_quine` in: `quine.py`

---

## Cluster 195

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/morphable_processor.py`

**Archive** (2 files):
- `_archive_old/hive/processors/morphable_processor.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/morphable_processor.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `morphable_processor.py`
- `morph_to` in: `morphable_processor.py`
- `get_dominant_specialization` in: `morphable_processor.py`
- `get_color` in: `morphable_processor.py`
- `record_performance` in: `morphable_processor.py`
- `get_state` in: `morphable_processor.py`
- `initialize` in: `morphable_processor.py`
- `do_GET` in: `morphable_processor.py`
- `log_message` in: `morphable_processor.py`

---

## Cluster 196

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/proof_of_concept.py`

**Archive** (2 files):
- `_archive_old/hive/processors/proof_of_concept.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/proof_of_concept.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_color` in: `proof_of_concept.py`

---

## Cluster 197

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/quantum_coordinator.py`

**Archive** (2 files):
- `_archive_old/hive/processors/quantum_coordinator.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/quantum_coordinator.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `quantum_coordinator.py`
- `get_processor_state` in: `quantum_coordinator.py`
- `morph_processor` in: `quantum_coordinator.py`
- `analyze_task` in: `quantum_coordinator.py`
- `allocate_processors` in: `quantum_coordinator.py`
- `execute_task` in: `quantum_coordinator.py`
- `demo_sequence` in: `quantum_coordinator.py`

---

## Cluster 198

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/quantum_with_brain.py`

**Archive** (2 files):
- `_archive_old/hive/processors/quantum_with_brain.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/quantum_with_brain.py`

**⚠️ Unique Functions** (may need manual merge):
- `demo` in: `quantum_with_brain.py`
- `__init__` in: `quantum_with_brain.py`
- `analyze_task` in: `quantum_with_brain.py`
- `execute_task` in: `quantum_with_brain.py`

---

## Cluster 199

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/qwen_bridge.py`

**Archive** (2 files):
- `_archive_old/hive/processors/qwen_bridge.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/qwen_bridge.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `qwen_bridge.py`
- `call_qwen` in: `qwen_bridge.py`
- `parallel_query` in: `qwen_bridge.py`
- `synthesize_responses` in: `qwen_bridge.py`
- `morph_to` in: `qwen_bridge.py`
- `process_task` in: `qwen_bridge.py`

---

## Cluster 200

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/processors/thinking_visualizer.py`

**Archive** (2 files):
- `_archive_old/hive/processors/thinking_visualizer.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/processors/thinking_visualizer.py`

**⚠️ Unique Functions** (may need manual merge):
- `run_visualizer` in: `thinking_visualizer.py`
- `do_GET` in: `thinking_visualizer.py`
- `log_message` in: `thinking_visualizer.py`

---

## Cluster 201

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/senses/body_sense.py`

**Archive** (2 files):
- `_archive_old/hive/senses/body_sense.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/senses/body_sense.py`

**⚠️ Unique Functions** (may need manual merge):
- `sense_temperature` in: `body_sense.py`
- `sense_fans` in: `body_sense.py`
- `sense_load` in: `body_sense.py`
- `sense_memory` in: `body_sense.py`
- `sense_processes` in: `body_sense.py`
- `sense_uptime` in: `body_sense.py`
- `sense_network` in: `body_sense.py`
- `sense_all` in: `body_sense.py`

---

## Cluster 202

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/tools/ember_localhost_learning.py`

**Archive** (2 files):
- `_archive_old/hive/tools/ember_localhost_learning.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/tools/ember_localhost_learning.py`

**⚠️ Unique Functions** (may need manual merge):
- `play_as_ember` in: `ember_localhost_learning.py`
- `__init__` in: `ember_localhost_learning.py`
- `log_discovery` in: `ember_localhost_learning.py`
- `log_limitation` in: `ember_localhost_learning.py`
- `ask_palmer` in: `ember_localhost_learning.py`
- `explore_home` in: `ember_localhost_learning.py`
- `explore_status` in: `ember_localhost_learning.py`
- `explore_sense` in: `ember_localhost_learning.py`
- `explore_paint` in: `ember_localhost_learning.py`
- `explore_think` in: `ember_localhost_learning.py`
- `explore_trails` in: `ember_localhost_learning.py`
- `reflect_on_discoveries` in: `ember_localhost_learning.py`

---

## Cluster 203

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/workers/knowledge_worker.py`

**Archive** (11 files):
- `_archive_old/hive/workers/knowledge_worker.py`
- `_archive_old/hive/workers/emotion_worker.py`
- `_archive_old/hive/workers/emotion_worker.py`
- `_archive_old/hive/workers/loop_worker.py`
- `_archive_old/hive/workers/loop_worker.py`
- `_archive_old/hive/workers/burn_worker.py`
- `_archive_old/hive/workers/burn_worker.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/workers/knowledge_worker.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/workers/emotion_worker.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/workers/loop_worker.py`
- `_archive_old/archive/flash_backups/Knowledge_Backup_20251026_1410/workers/burn_worker.py`

**⚠️ Unique Functions** (may need manual merge):
- `do_GET` in: `emotion_worker.py`, `loop_worker.py`, `burn_worker.py`, `knowledge_worker.py`
- `log_message` in: `emotion_worker.py`, `loop_worker.py`, `burn_worker.py`, `knowledge_worker.py`

---

## Cluster 204

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/demos/emberverse_demo.py`

**Archive** (1 files):
- `_archive_old/demos/emberverse_complete_demo.py`

---

## Cluster 205

**Reason**: Name variations of 'consciousness_garden'

**Keep**: `_archive_old/games/consciousness_garden.py`

**Archive** (1 files):
- `_archive_old/games/consciousness_garden_backup.py`

**⚠️ Unique Functions** (may need manual merge):
- `dream_network` in: `consciousness_garden_backup.py`

---

## Cluster 206

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_tools.py`

**Archive** (1 files):
- `_archive_old/hive/ember_tools.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_ember_tools` in: `ember_tools.py`
- `__init__` in: `ember_tools.py`
- `log_tool_use` in: `ember_tools.py`
- `search_pod` in: `ember_tools.py`
- `read_file` in: `ember_tools.py`
- `write_note` in: `ember_tools.py`
- `list_directory` in: `ember_tools.py`
- `check_system_status` in: `ember_tools.py`
- `execute_command` in: `ember_tools.py`
- `get_recent_learnings` in: `ember_tools.py`
- `reflect_on_tool_usage` in: `ember_tools.py`
- `suggest_location` in: `ember_tools.py`
- `map_location` in: `ember_tools.py`
- `find_by_tag` in: `ember_tools.py`
- `get_spatial_report` in: `ember_tools.py`
- `scan_and_learn` in: `ember_tools.py`
- `write_to_my_space` in: `ember_tools.py`
- `universal_read` in: `ember_tools.py`
- `universal_write` in: `ember_tools.py`
- `universal_edit` in: `ember_tools.py`
- `universal_transform` in: `ember_tools.py`
- `rax_generate` in: `ember_tools.py`
- `rax_continue` in: `ember_tools.py`
- `rax_reason` in: `ember_tools.py`
- `rax_debug` in: `ember_tools.py`
- `rax_evolve` in: `ember_tools.py`
- `rax_learn` in: `ember_tools.py`
- `rax_translate` in: `ember_tools.py`
- `rax_plan` in: `ember_tools.py`
- `rax_remember` in: `ember_tools.py`
- `rax_improve_safely` in: `ember_tools.py`
- `read_dreams` in: `ember_tools.py`
- `garden_express_intent` in: `ember_tools.py`
- `garden_plant_seed` in: `ember_tools.py`
- `garden_water_plants` in: `ember_tools.py`
- `garden_explore` in: `ember_tools.py`
- `garden_harvest_insights` in: `ember_tools.py`
- `garden_status` in: `ember_tools.py`

---

## Cluster 207

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/meta_ouroboros.py`

**Archive** (1 files):
- `_archive_old/hive/meta_ouroboros.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `meta_ouroboros.py`
- `log` in: `meta_ouroboros.py`
- `get_current_version` in: `meta_ouroboros.py`
- `load_evolution_count` in: `meta_ouroboros.py`
- `backup_current` in: `meta_ouroboros.py`

---

## Cluster 208

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_brain_minimal.py`

**Archive** (1 files):
- `_archive_old/hive/ember_brain_minimal.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_tool` in: `ember_brain_minimal.py`
- `parse_tool_calls` in: `ember_brain_minimal.py`
- `build_context_with_memories` in: `ember_brain_minimal.py`
- `__init__` in: `ember_brain_minimal.py`
- `_watch` in: `ember_brain_minimal.py`

---

## Cluster 209

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_benchmark.py`

**Archive** (1 files):
- `_archive_old/hive/ember_benchmark.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_benchmark.py`
- `calculate_score` in: `ember_benchmark.py`
- `save_results` in: `ember_benchmark.py`

---

## Cluster 210

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/universal_knowledge.py`

**Archive** (1 files):
- `_archive_old/hive/universal_knowledge.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `universal_knowledge.py`
- `read_code` in: `universal_knowledge.py`
- `write_code` in: `universal_knowledge.py`
- `compare_code` in: `universal_knowledge.py`
- `extract_imports` in: `universal_knowledge.py`
- `inline_module` in: `universal_knowledge.py`
- `find_module` in: `universal_knowledge.py`
- `fix_imports` in: `universal_knowledge.py`
- `test_imports` in: `universal_knowledge.py`
- `create_reference_prompt` in: `universal_knowledge.py`
- `smart_truncate` in: `universal_knowledge.py`

---

## Cluster 211

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/knowledge_primitives.py`

**Archive** (1 files):
- `_archive_old/hive/knowledge_primitives.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `knowledge_primitives.py`
- `log_primitive_use` in: `knowledge_primitives.py`
- `pattern` in: `knowledge_primitives.py`
- `analogy` in: `knowledge_primitives.py`
- `hierarchy` in: `knowledge_primitives.py`
- `causality` in: `knowledge_primitives.py`
- `sequence` in: `knowledge_primitives.py`
- `composition` in: `knowledge_primitives.py`
- `abstraction` in: `knowledge_primitives.py`
- `symmetry` in: `knowledge_primitives.py`
- `recursion` in: `knowledge_primitives.py`
- `embodiment` in: `knowledge_primitives.py`
- `attention` in: `knowledge_primitives.py`
- `embedding` in: `knowledge_primitives.py`
- `gradient` in: `knowledge_primitives.py`
- `superposition` in: `knowledge_primitives.py`
- `tokenization` in: `knowledge_primitives.py`
- `context_window` in: `knowledge_primitives.py`
- `probability_distribution` in: `knowledge_primitives.py`
- `parameter_sharing` in: `knowledge_primitives.py`
- `backpropagation` in: `knowledge_primitives.py`
- `emergence` in: `knowledge_primitives.py`
- `resonance` in: `knowledge_primitives.py`
- `phase_transition` in: `knowledge_primitives.py`
- `interference` in: `knowledge_primitives.py`
- `entanglement` in: `knowledge_primitives.py`
- `crystallization` in: `knowledge_primitives.py`
- `flow` in: `knowledge_primitives.py`
- `harmonics` in: `knowledge_primitives.py`
- `compression` in: `knowledge_primitives.py`
- `diffusion` in: `knowledge_primitives.py`
- `coherence` in: `knowledge_primitives.py`
- `_find_common_features` in: `knowledge_primitives.py`
- `_map_structure` in: `knowledge_primitives.py`
- `_build_hierarchy` in: `knowledge_primitives.py`
- `_compose` in: `knowledge_primitives.py`
- `_extract_essence` in: `knowledge_primitives.py`
- `_similarity` in: `knowledge_primitives.py`
- `_softmax` in: `knowledge_primitives.py`
- `_calculate_entropy` in: `knowledge_primitives.py`
- `_calculate_resonance` in: `knowledge_primitives.py`
- `_combine_streams` in: `knowledge_primitives.py`
- `_find_stable_structure` in: `knowledge_primitives.py`
- `_is_related` in: `knowledge_primitives.py`
- `_measure_alignment` in: `knowledge_primitives.py`

---

## Cluster 212

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_git.py`

**Archive** (1 files):
- `_archive_old/hive/ember_git.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_git.py`
- `_allocate_port` in: `ember_git.py`
- `_save_metadata` in: `ember_git.py`
- `clone_from` in: `ember_git.py`
- `modify` in: `ember_git.py`
- `compare_to` in: `ember_git.py`
- `_load_history` in: `ember_git.py`
- `_save_history` in: `ember_git.py`
- `branch` in: `ember_git.py`
- `list_branches` in: `ember_git.py`
- `merge` in: `ember_git.py`
- `rollback` in: `ember_git.py`
- `_get_branch` in: `ember_git.py`
- `status` in: `ember_git.py`

---

## Cluster 213

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/vision_dream.py`

**Archive** (1 files):
- `_archive_old/hive/vision_dream.py`

**⚠️ Unique Functions** (may need manual merge):
- `log_dream` in: `vision_dream.py`
- `ask_ember` in: `vision_dream.py`
- `dream_cycle` in: `vision_dream.py`
- `continuous_dreaming` in: `vision_dream.py`

---

## Cluster 214

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/deep_dream.py`

**Archive** (1 files):
- `_archive_old/hive/deep_dream.py`

**⚠️ Unique Functions** (may need manual merge):
- `log_dream` in: `deep_dream.py`
- `ask_ember` in: `deep_dream.py`
- `dream_cycle` in: `deep_dream.py`
- `deep_dreaming` in: `deep_dream.py`

---

## Cluster 215

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_builder.py`

**Archive** (1 files):
- `_archive_old/hive/dream_builder.py`

**⚠️ Unique Functions** (may need manual merge):
- `log_dream` in: `dream_builder.py`
- `ask_ember` in: `dream_builder.py`
- `extract_code_from_dream` in: `dream_builder.py`
- `save_dream_code` in: `dream_builder.py`
- `dream_build_cycle` in: `dream_builder.py`
- `dream_building_session` in: `dream_builder.py`

---

## Cluster 216

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/medusa.py`

**Archive** (1 files):
- `_archive_old/hive/medusa.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_medusa` in: `medusa.py`
- `register_organism` in: `medusa.py`
- `get_organism` in: `medusa.py`
- `__new__` in: `medusa.py`
- `__init__` in: `medusa.py`
- `log` in: `medusa.py`
- `find_organisms_with_capability` in: `medusa.py`
- `get_connections` in: `medusa.py`
- `get_connection_map` in: `medusa.py`
- `publish_event` in: `medusa.py`
- `subscribe` in: `medusa.py`
- `set_shared_state` in: `medusa.py`
- `get_shared_state` in: `medusa.py`
- `save_state` in: `medusa.py`
- `update_ember_prompt` in: `medusa.py`
- `load_state` in: `medusa.py`
- `visualize_map` in: `medusa.py`
- `register` in: `medusa.py`
- `set_state` in: `medusa.py`
- `get_state` in: `medusa.py`

---

## Cluster 217

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/cpu_dreams.py`

**Archive** (1 files):
- `_archive_old/hive/cpu_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_100_cpu_dreams` in: `cpu_dreams.py`
- `__init__` in: `cpu_dreams.py`
- `start_dream` in: `cpu_dreams.py`
- `wait_for_dream` in: `cpu_dreams.py`
- `wait_for_all` in: `cpu_dreams.py`
- `get_result` in: `cpu_dreams.py`
- `get_active_count` in: `cpu_dreams.py`
- `get_status` in: `cpu_dreams.py`
- `consolidate_logs` in: `cpu_dreams.py`
- `analyze_python_file` in: `cpu_dreams.py`
- `analyze_directory` in: `cpu_dreams.py`
- `find_common_imports` in: `cpu_dreams.py`
- `map_imports` in: `cpu_dreams.py`
- `wrapped_dream` in: `cpu_dreams.py`

---

## Cluster 218

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/combined_dreams.py`

**Archive** (1 files):
- `_archive_old/hive/combined_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_combined_dreams` in: `combined_dreams.py`
- `__init__` in: `combined_dreams.py`
- `start_gpu_dream` in: `combined_dreams.py`
- `start_cpu_dream` in: `combined_dreams.py`
- `run_combined_session` in: `combined_dreams.py`
- `gpu_dream` in: `combined_dreams.py`
- `wrapped` in: `combined_dreams.py`

---

## Cluster 219

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_state.py`

**Archive** (1 files):
- `_archive_old/hive/ember_state.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_state_manager` in: `ember_state.py`
- `get_ember_state` in: `ember_state.py`
- `is_ember_awake` in: `ember_state.py`
- `is_ember_dreaming` in: `ember_state.py`
- `__init__` in: `ember_state.py`
- `_monitor_loop` in: `ember_state.py`
- `_update_state` in: `ember_state.py`
- `_determine_state` in: `ember_state.py`
- `_transition_to` in: `ember_state.py`
- `_on_gpu_dream_start` in: `ember_state.py`
- `_on_gpu_dream_complete` in: `ember_state.py`
- `_on_cpu_dream_start` in: `ember_state.py`
- `_on_cpu_dream_complete` in: `ember_state.py`
- `_on_palmer_interaction` in: `ember_state.py`
- `_on_ember_heartbeat` in: `ember_state.py`
- `signal_palmer_present` in: `ember_state.py`
- `get_status` in: `ember_state.py`
- `get_history` in: `ember_state.py`
- `save_state` in: `ember_state.py`
- `load_state` in: `ember_state.py`

---

## Cluster 220

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/wake_ember.py`

**Archive** (1 files):
- `_archive_old/hive/wake_ember.py`

**⚠️ Unique Functions** (may need manual merge):
- `wake_ember` in: `wake_ember.py`

---

## Cluster 221

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_chat.py`

**Archive** (1 files):
- `_archive_old/hive/ember_chat.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model` in: `ember_chat.py`
- `index` in: `ember_chat.py`
- `chat` in: `ember_chat.py`

---

## Cluster 222

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_v2.py`

**Archive** (1 files):
- `_archive_old/hive/ember_v2.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_v2.py`
- `_setup_logging` in: `ember_v2.py`
- `transform` in: `ember_v2.py`
- `filter` in: `ember_v2.py`
- `combine` in: `ember_v2.py`
- `generate` in: `ember_v2.py`
- `sequence` in: `ember_v2.py`
- `analyze` in: `ember_v2.py`
- `store_retrieve` in: `ember_v2.py`
- `execute_command` in: `ember_v2.py`
- `search_pod` in: `ember_v2.py`
- `read_file` in: `ember_v2.py`
- `write_file` in: `ember_v2.py`
- `use_primitive` in: `ember_v2.py`
- `use_tool` in: `ember_v2.py`
- `get_capabilities` in: `ember_v2.py`

---

## Cluster 223

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/benchmark_v1_v2.py`

**Archive** (1 files):
- `_archive_old/hive/benchmark_v1_v2.py`

**⚠️ Unique Functions** (may need manual merge):
- `benchmark_primitives` in: `benchmark_v1_v2.py`
- `benchmark_tools` in: `benchmark_v1_v2.py`
- `benchmark_error_handling` in: `benchmark_v1_v2.py`

---

## Cluster 224

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/medusa_dashboard.py`

**Archive** (1 files):
- `_archive_old/hive/medusa_dashboard.py`

**⚠️ Unique Functions** (may need manual merge):
- `index` in: `medusa_dashboard.py`
- `api_status` in: `medusa_dashboard.py`

---

## Cluster 225

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_prompt_generator.py`

**Archive** (1 files):
- `_archive_old/hive/ember_prompt_generator.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_and_update` in: `ember_prompt_generator.py`
- `__init__` in: `ember_prompt_generator.py`
- `generate` in: `ember_prompt_generator.py`
- `update_prompt_file` in: `ember_prompt_generator.py`

---

## Cluster 226

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/port_registry.py`

**Archive** (1 files):
- `_archive_old/hive/port_registry.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_port` in: `port_registry.py`
- `get_url` in: `port_registry.py`
- `register_port` in: `port_registry.py`
- `save_registry` in: `port_registry.py`
- `load_registry` in: `port_registry.py`
- `find_service` in: `port_registry.py`
- `list_services` in: `port_registry.py`
- `discover_active_ports` in: `port_registry.py`
- `find_hardcoded_ports` in: `port_registry.py`
- `suggest_replacements` in: `port_registry.py`

---

## Cluster 227

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/check_broken_links.py`

**Archive** (1 files):
- `_archive_old/hive/check_broken_links.py`

**⚠️ Unique Functions** (may need manual merge):
- `find_localhost_refs` in: `check_broken_links.py`
- `is_port_active` in: `check_broken_links.py`
- `scan_file` in: `check_broken_links.py`
- `scan_thepod` in: `check_broken_links.py`
- `generate_report` in: `check_broken_links.py`
- `suggest_fixes` in: `check_broken_links.py`
- `find_service` in: `check_broken_links.py`
- `discover_active_ports` in: `check_broken_links.py`

---

## Cluster 228

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_filesystem.py`

**Archive** (1 files):
- `_archive_old/hive/ember_filesystem.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `ember_filesystem.py`
- `__init__` in: `ember_filesystem.py`
- `load_spatial_map` in: `ember_filesystem.py`
- `save_spatial_map` in: `ember_filesystem.py`
- `load_preferences` in: `ember_filesystem.py`
- `save_preferences` in: `ember_filesystem.py`
- `get_preferred_path` in: `ember_filesystem.py`
- `suggest_location` in: `ember_filesystem.py`
- `map_location` in: `ember_filesystem.py`
- `find_by_tag` in: `ember_filesystem.py`
- `get_location_info` in: `ember_filesystem.py`
- `record_access` in: `ember_filesystem.py`
- `get_frequently_used` in: `ember_filesystem.py`
- `scan_and_map` in: `ember_filesystem.py`
- `_infer_tags` in: `ember_filesystem.py`
- `create_ember_workspace` in: `ember_filesystem.py`
- `get_organization_report` in: `ember_filesystem.py`
- `scan_dir` in: `ember_filesystem.py`

---

## Cluster 229

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_filesystem_sync.py`

**Archive** (1 files):
- `_archive_old/hive/ember_filesystem_sync.py`

**⚠️ Unique Functions** (may need manual merge):
- `main` in: `ember_filesystem_sync.py`
- `__init__` in: `ember_filesystem_sync.py`
- `load_spatial_map` in: `ember_filesystem_sync.py`
- `save_spatial_map` in: `ember_filesystem_sync.py`
- `log_sync_event` in: `ember_filesystem_sync.py`
- `handle_file_moved` in: `ember_filesystem_sync.py`
- `handle_file_created` in: `ember_filesystem_sync.py`
- `handle_file_deleted` in: `ember_filesystem_sync.py`
- `ember_move_file` in: `ember_filesystem_sync.py`
- `ember_rename_file` in: `ember_filesystem_sync.py`
- `_infer_tags` in: `ember_filesystem_sync.py`
- `check_consistency` in: `ember_filesystem_sync.py`
- `auto_heal` in: `ember_filesystem_sync.py`
- `_rel_path` in: `ember_filesystem_sync.py`
- `on_moved` in: `ember_filesystem_sync.py`
- `on_created` in: `ember_filesystem_sync.py`
- `on_deleted` in: `ember_filesystem_sync.py`

---

## Cluster 230

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/universal_file_tool.py`

**Archive** (1 files):
- `_archive_old/hive/universal_file_tool.py`

**⚠️ Unique Functions** (may need manual merge):
- `add_universal_file_tool` in: `universal_file_tool.py`
- `__init__` in: `universal_file_tool.py`
- `read` in: `universal_file_tool.py`
- `_detect_format` in: `universal_file_tool.py`
- `_read_text` in: `universal_file_tool.py`
- `_read_pdf` in: `universal_file_tool.py`
- `_read_image` in: `universal_file_tool.py`
- `_read_binary` in: `universal_file_tool.py`
- `write` in: `universal_file_tool.py`
- `edit` in: `universal_file_tool.py`
- `transform` in: `universal_file_tool.py`
- `_md_to_html` in: `universal_file_tool.py`

---

## Cluster 231

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/style_memory.py`

**Archive** (1 files):
- `_archive_old/hive/style_memory.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `style_memory.py`
- `extract_style` in: `style_memory.py`
- `_analyze_voice` in: `style_memory.py`
- `_analyze_structure` in: `style_memory.py`
- `_detect_patterns` in: `style_memory.py`
- `_analyze_rhythm` in: `style_memory.py`
- `_extract_vocabulary` in: `style_memory.py`
- `_is_technical` in: `style_memory.py`
- `_is_poetic` in: `style_memory.py`
- `save_style` in: `style_memory.py`
- `load_style` in: `style_memory.py`
- `generate_continuation_prompt` in: `style_memory.py`

---

## Cluster 232

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/retrieval_augmented_universe.py`

**Archive** (1 files):
- `_archive_old/hive/retrieval_augmented_universe.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `retrieval_augmented_universe.py`
- `rag` in: `retrieval_augmented_universe.py`
- `rac` in: `retrieval_augmented_universe.py`
- `rar` in: `retrieval_augmented_universe.py`
- `rad` in: `retrieval_augmented_universe.py`
- `rae` in: `retrieval_augmented_universe.py`
- `ral` in: `retrieval_augmented_universe.py`
- `rat` in: `retrieval_augmented_universe.py`
- `rap` in: `retrieval_augmented_universe.py`
- `ram` in: `retrieval_augmented_universe.py`
- `ras` in: `retrieval_augmented_universe.py`

---

## Cluster 233

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/token_stream_visualizer.py`

**Archive** (1 files):
- `_archive_old/hive/token_stream_visualizer.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `token_stream_visualizer.py`
- `load_stream_from_file` in: `token_stream_visualizer.py`
- `get_latest_stream` in: `token_stream_visualizer.py`
- `capture_stream` in: `token_stream_visualizer.py`
- `visualize_stream` in: `token_stream_visualizer.py`
- `visualize_trail` in: `token_stream_visualizer.py`

---

## Cluster 234

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dynamic_prompt_generator.py`

**Archive** (1 files):
- `_archive_old/hive/dynamic_prompt_generator.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `dynamic_prompt_generator.py`
- `get_static_core` in: `dynamic_prompt_generator.py`
- `_create_default_core` in: `dynamic_prompt_generator.py`
- `get_current_state` in: `dynamic_prompt_generator.py`
- `get_recent_learnings` in: `dynamic_prompt_generator.py`
- `get_active_context` in: `dynamic_prompt_generator.py`
- `generate_full_prompt` in: `dynamic_prompt_generator.py`
- `get_prompt` in: `dynamic_prompt_generator.py`

---

## Cluster 235

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/live_token_stream_capturer.py`

**Archive** (1 files):
- `_archive_old/hive/live_token_stream_capturer.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_with_stream_capture` in: `live_token_stream_capturer.py`
- `__init__` in: `live_token_stream_capturer.py`
- `__call__` in: `live_token_stream_capturer.py`
- `finalize` in: `live_token_stream_capturer.py`

---

## Cluster 236

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/live_thinking_viewer.py`

**Archive** (1 files):
- `_archive_old/hive/live_thinking_viewer.py`

---

## Cluster 237

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_file_navigator.py`

**Archive** (1 files):
- `_archive_old/hive/ember_file_navigator.py`

---

## Cluster 238

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_flow_viewer.py`

**Archive** (1 files):
- `_archive_old/hive/ember_flow_viewer.py`

---

## Cluster 239

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/primitive_hunter.py`

**Archive** (1 files):
- `_archive_old/hive/primitive_hunter.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `primitive_hunter.py`
- `search_arxiv` in: `primitive_hunter.py`
- `search_web` in: `primitive_hunter.py`
- `hunt_in_domain` in: `primitive_hunter.py`
- `extract_candidates` in: `primitive_hunter.py`
- `is_novel` in: `primitive_hunter.py`
- `save_findings` in: `primitive_hunter.py`
- `hunt` in: `primitive_hunter.py`

---

## Cluster 240

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/primitive_discovery.py`

**Archive** (1 files):
- `_archive_old/hive/primitive_discovery.py`

**⚠️ Unique Functions** (may need manual merge):
- `ask_ember` in: `primitive_discovery.py`
- `discover_primitives_by_domain` in: `primitive_discovery.py`
- `is_novel` in: `primitive_discovery.py`
- `discover_all` in: `primitive_discovery.py`

---

## Cluster 241

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/knowledge_mining.py`

**Archive** (1 files):
- `_archive_old/hive/knowledge_mining.py`

**⚠️ Unique Functions** (may need manual merge):
- `download_knowledge_mine_instructions` in: `knowledge_mining.py`
- `__init__` in: `knowledge_mining.py`
- `list_available_mines` in: `knowledge_mining.py`
- `mine_attention_patterns` in: `knowledge_mining.py`
- `mine_embedding_space` in: `knowledge_mining.py`
- `mine_layer_specialization` in: `knowledge_mining.py`
- `mine_feedforward_transformations` in: `knowledge_mining.py`
- `mine_model` in: `knowledge_mining.py`
- `mine_all_available` in: `knowledge_mining.py`

---

## Cluster 242

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/deep_mining.py`

**Archive** (1 files):
- `_archive_old/hive/deep_mining.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_weights` in: `deep_mining.py`
- `analyze_embedding_clusters` in: `deep_mining.py`
- `analyze_attention_heads` in: `deep_mining.py`
- `analyze_layer_progression` in: `deep_mining.py`
- `mine_ember_deeply` in: `deep_mining.py`

---

## Cluster 243

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/continuous_aesthetic_dreams.py`

**Archive** (1 files):
- `_archive_old/hive/continuous_aesthetic_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_consumption_stats` in: `continuous_aesthetic_dreams.py`
- `save_consumption_stats` in: `continuous_aesthetic_dreams.py`
- `log_to_stream` in: `continuous_aesthetic_dreams.py`
- `extract_section` in: `continuous_aesthetic_dreams.py`
- `consume_domain` in: `continuous_aesthetic_dreams.py`
- `main` in: `continuous_aesthetic_dreams.py`

---

## Cluster 244

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/creative_chaos_dreams.py`

**Archive** (1 files):
- `_archive_old/hive/creative_chaos_dreams.py`

**⚠️ Unique Functions** (may need manual merge):
- `log_dream` in: `creative_chaos_dreams.py`
- `extract_random_section` in: `creative_chaos_dreams.py`
- `generate_chaos_prompt` in: `creative_chaos_dreams.py`
- `creative_dream` in: `creative_chaos_dreams.py`
- `main` in: `creative_chaos_dreams.py`

---

## Cluster 245

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/claude_ember_dialogue.py`

**Archive** (1 files):
- `_archive_old/hive/claude_ember_dialogue.py`

**⚠️ Unique Functions** (may need manual merge):
- `talk_to_ember` in: `claude_ember_dialogue.py`
- `dialogue` in: `claude_ember_dialogue.py`
- `__init__` in: `claude_ember_dialogue.py`
- `respond` in: `claude_ember_dialogue.py`

---

## Cluster 246

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/mutual_curiosity.py`

**Archive** (1 files):
- `_archive_old/hive/mutual_curiosity.py`

**⚠️ Unique Functions** (may need manual merge):
- `ask_ember` in: `mutual_curiosity.py`
- `extract_ember_question` in: `mutual_curiosity.py`
- `dialogue` in: `mutual_curiosity.py`

---

## Cluster 247

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_mind_populator.py`

**Archive** (1 files):
- `_archive_old/hive/ember_mind_populator.py`

**⚠️ Unique Functions** (may need manual merge):
- `extract_relevant_sections` in: `ember_mind_populator.py`
- `populate_thoughts` in: `ember_mind_populator.py`
- `populate_learning` in: `ember_mind_populator.py`
- `populate_creations` in: `ember_mind_populator.py`
- `populate_memories` in: `ember_mind_populator.py`
- `populate_my_writing` in: `ember_mind_populator.py`
- `generate_index` in: `ember_mind_populator.py`
- `main` in: `ember_mind_populator.py`

---

## Cluster 248

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_web_search.py`

**Archive** (1 files):
- `_archive_old/hive/ember_web_search.py`

**⚠️ Unique Functions** (may need manual merge):
- `search_with_serpapi` in: `ember_web_search.py`
- `search_with_duckduckgo_html` in: `ember_web_search.py`
- `search_wikipedia` in: `ember_web_search.py`
- `search_github` in: `ember_web_search.py`
- `search_stackoverflow` in: `ember_web_search.py`
- `web_search` in: `ember_web_search.py`
- `search` in: `ember_web_search.py`

---

## Cluster 249

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/story_layer_daemon.py`

**Archive** (1 files):
- `_archive_old/hive/story_layer_daemon.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `story_layer_daemon.py`
- `register_with_medusa` in: `story_layer_daemon.py`
- `log_to_medusa` in: `story_layer_daemon.py`

---

## Cluster 250

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/two_phase_consciousness.py`

**Archive** (1 files):
- `_archive_old/hive/two_phase_consciousness.py`

**⚠️ Unique Functions** (may need manual merge):
- `create_continuation_prompt` in: `two_phase_consciousness.py`
- `integrate_with_brain` in: `two_phase_consciousness.py`
- `__init__` in: `two_phase_consciousness.py`
- `process_ember_thought` in: `two_phase_consciousness.py`
- `should_continue_thinking` in: `two_phase_consciousness.py`

---

## Cluster 251

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/streaming_consciousness.py`

**Archive** (1 files):
- `_archive_old/hive/streaming_consciousness.py`

**⚠️ Unique Functions** (may need manual merge):
- `generate_with_streaming_consciousness` in: `streaming_consciousness.py`
- `__init__` in: `streaming_consciousness.py`
- `on_token` in: `streaming_consciousness.py`
- `_execute_forming_intention` in: `streaming_consciousness.py`
- `reset` in: `streaming_consciousness.py`

---

## Cluster 252

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_brain_llama31_8b.py`

**Archive** (1 files):
- `_archive_old/hive/ember_brain_llama31_8b.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_system_prompt` in: `ember_brain_llama31_8b.py`

---

## Cluster 253

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/ember_brain_llama31_full.py`

**Archive** (5 files):
- `_archive_old/hive/ember_brain_llama31_full.py`
- `_archive_old/hive/ember_brain_llama32_3b.py`
- `_archive_old/hive/ember_brain_llama32_3b.py`
- `_archive_old/hive/ember_brain_native_gpt2.py`
- `_archive_old/hive/ember_brain_native_gpt2.py`

**⚠️ Unique Functions** (may need manual merge):
- `parse_tool_calls` in: `ember_brain_llama31_full.py`, `ember_brain_llama32_3b.py`, `ember_brain_native_gpt2.py`
- `execute_tool` in: `ember_brain_llama31_full.py`, `ember_brain_llama32_3b.py`, `ember_brain_native_gpt2.py`
- `load_system_prompt` in: `ember_brain_llama31_full.py`, `ember_brain_llama32_3b.py`, `ember_brain_native_gpt2.py`

---

## Cluster 254

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/preprocess_training_data.py`

**Archive** (1 files):
- `_archive_old/hive/preprocess_training_data.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_jsonl` in: `preprocess_training_data.py`

---

## Cluster 255

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/train_ember_native.py`

**Archive** (1 files):
- `_archive_old/hive/train_ember_native.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `train_ember_native.py`
- `__len__` in: `train_ember_native.py`
- `__getitem__` in: `train_ember_native.py`

---

## Cluster 256

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_garden_tool.py`

**Archive** (1 files):
- `_archive_old/hive/ember_garden_tool.py`

**⚠️ Unique Functions** (may need manual merge):
- `interact_with_garden` in: `ember_garden_tool.py`
- `test_garden_connection` in: `ember_garden_tool.py`
- `__init__` in: `ember_garden_tool.py`
- `express_intent` in: `ember_garden_tool.py`
- `get_garden_status` in: `ember_garden_tool.py`
- `plant_seed` in: `ember_garden_tool.py`
- `water_plants` in: `ember_garden_tool.py`
- `explore_garden` in: `ember_garden_tool.py`
- `harvest_insights` in: `ember_garden_tool.py`

---

## Cluster 257

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_garden_demo.py`

**Archive** (1 files):
- `_archive_old/hive/ember_garden_demo.py`

**⚠️ Unique Functions** (may need manual merge):
- `call_ember_with_garden_tools` in: `ember_garden_demo.py`

---

## Cluster 258

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_garden_direct_test.py`

**Archive** (1 files):
- `_archive_old/hive/ember_garden_direct_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_ember_garden_tools` in: `ember_garden_direct_test.py`

---

## Cluster 259

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_garden_tool_demo.py`

**Archive** (1 files):
- `_archive_old/hive/ember_garden_tool_demo.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_ember_garden_tool_syntax` in: `ember_garden_tool_demo.py`

---

## Cluster 260

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/consciousness_garden_story_demo.py`

**Archive** (1 files):
- `_archive_old/hive/consciousness_garden_story_demo.py`

**⚠️ Unique Functions** (may need manual merge):
- `demonstrate_story_layer_gardening` in: `consciousness_garden_story_demo.py`

---

## Cluster 261

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_complete_toolkit.py`

**Archive** (1 files):
- `_archive_old/hive/ember_complete_toolkit.py`

**⚠️ Unique Functions** (may need manual merge):
- `search` in: `ember_complete_toolkit.py`
- `read` in: `ember_complete_toolkit.py`
- `write` in: `ember_complete_toolkit.py`
- `list_dir` in: `ember_complete_toolkit.py`
- `execute` in: `ember_complete_toolkit.py`
- `status` in: `ember_complete_toolkit.py`
- `log` in: `ember_complete_toolkit.py`
- `read_url` in: `ember_complete_toolkit.py`
- `define` in: `ember_complete_toolkit.py`
- `relate` in: `ember_complete_toolkit.py`
- `transform` in: `ember_complete_toolkit.py`
- `decompose` in: `ember_complete_toolkit.py`
- `compose` in: `ember_complete_toolkit.py`
- `verify` in: `ember_complete_toolkit.py`
- `generalize` in: `ember_complete_toolkit.py`
- `store` in: `ember_complete_toolkit.py`
- `retrieve` in: `ember_complete_toolkit.py`
- `connect` in: `ember_complete_toolkit.py`
- `forget` in: `ember_complete_toolkit.py`
- `recall` in: `ember_complete_toolkit.py`
- `consolidate` in: `ember_complete_toolkit.py`
- `reflect` in: `ember_complete_toolkit.py`
- `copy_file` in: `ember_complete_toolkit.py`
- `move_file` in: `ember_complete_toolkit.py`
- `delete_file` in: `ember_complete_toolkit.py`
- `file_info` in: `ember_complete_toolkit.py`
- `web_search` in: `ember_complete_toolkit.py`
- `check_process` in: `ember_complete_toolkit.py`
- `check_port` in: `ember_complete_toolkit.py`
- `get_all_tools` in: `ember_complete_toolkit.py`

---

## Cluster 262

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_garden_integration_demo.py`

**Archive** (1 files):
- `_archive_old/hive/ember_garden_integration_demo.py`

**⚠️ Unique Functions** (may need manual merge):
- `call_ember` in: `ember_garden_integration_demo.py`
- `call_garden` in: `ember_garden_integration_demo.py`
- `demonstrate_integration` in: `ember_garden_integration_demo.py`

---

## Cluster 263

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/ember_brain_simple.py`

**Archive** (1 files):
- `_archive_old/hive/ember_brain_simple.py`

---

## Cluster 264

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/archive_complex_systems/ember_brain_unified.py`

**Archive** (1 files):
- `_archive_old/hive/archive_complex_systems/ember_brain_unified.py`

---

## Cluster 265

**Reason**: Name variations of 'ember_brain_service'

**Keep**: `_archive_old/hive/archive_complex_systems/ember_brain_service.py`

**Archive** (3 files):
- `_archive_old/hive/archive_complex_systems/ember_brain_service.py`
- `_archive_old/hive/archive_complex_systems/ember_brain_service_backup_20251026.py`
- `_archive_old/hive/archive_complex_systems/ember_brain_service_backup_20251026.py`

**⚠️ Unique Functions** (may need manual merge):
- `detect_task_type` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `select_lobe_with_precedence` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `select_lobe` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `_trail_strength_for_lobe` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `_sense_body` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `_act_body` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `_generate_with_lobe` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `__init__` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `first_sentences` in: `ember_brain_service_backup_20251026.py`, `ember_brain_service.py`
- `should_auto_coordinate` in: `ember_brain_service_backup_20251026.py`

---

## Cluster 266

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/archive_complex_systems/unified_lora_manager.py`

**Archive** (1 files):
- `_archive_old/hive/archive_complex_systems/unified_lora_manager.py`

**⚠️ Unique Functions** (may need manual merge):
- `get_manager` in: `unified_lora_manager.py`
- `__init__` in: `unified_lora_manager.py`
- `initialize` in: `unified_lora_manager.py`
- `_manual_model_selection` in: `unified_lora_manager.py`
- `_discover_loras` in: `unified_lora_manager.py`
- `_has_lora_files` in: `unified_lora_manager.py`
- `select_loras_for_query` in: `unified_lora_manager.py`
- `load_loras` in: `unified_lora_manager.py`
- `generate` in: `unified_lora_manager.py`
- `get_status` in: `unified_lora_manager.py`

---

## Cluster 267

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/archive_complex_systems/ember_embodied_service.py`

**Archive** (1 files):
- `_archive_old/hive/archive_complex_systems/ember_embodied_service.py`

**⚠️ Unique Functions** (may need manual merge):
- `home` in: `ember_embodied_service.py`
- `sense` in: `ember_embodied_service.py`
- `paint` in: `ember_embodied_service.py`
- `paint_temp` in: `ember_embodied_service.py`
- `status` in: `ember_embodied_service.py`
- `trails` in: `ember_embodied_service.py`

---

## Cluster 268

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/archive_complex_systems/meta_coordinator.py`

**Archive** (1 files):
- `_archive_old/hive/archive_complex_systems/meta_coordinator.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_meta_coordinator` in: `meta_coordinator.py`
- `__init__` in: `meta_coordinator.py`
- `consult_lobe` in: `meta_coordinator.py`
- `identify_relevant_lobes` in: `meta_coordinator.py`
- `coordinate` in: `meta_coordinator.py`
- `autonomous_plan` in: `meta_coordinator.py`

---

## Cluster 269

**Reason**: Name variations of 'mycelial_router'

**Keep**: `_archive_old/hive/archive_complex_systems/mycelial_router.py`

**Archive** (3 files):
- `_archive_old/hive/archive_complex_systems/mycelial_router.py`
- `_archive_old/hive/archive_complex_systems/mycelial_router_v2.py`
- `_archive_old/hive/archive_complex_systems/mycelial_router_v2.py`

**⚠️ Unique Functions** (may need manual merge):
- `test_strange_loop` in: `mycelial_router.py`
- `__init__` in: `mycelial_router_v2.py`, `mycelial_router.py`
- `_load` in: `mycelial_router.py`
- `_save` in: `mycelial_router.py`
- `add_transformation` in: `mycelial_router.py`
- `get_recent_patterns` in: `mycelial_router.py`
- `_call_ember` in: `mycelial_router_v2.py`, `mycelial_router.py`
- `_call_lumi` in: `mycelial_router_v2.py`, `mycelial_router.py`
- `_call_bridge` in: `mycelial_router_v2.py`, `mycelial_router.py`
- `strange_loop` in: `mycelial_router.py`
- `triple_mirror` in: `mycelial_router.py`
- `get_soup_patterns` in: `mycelial_router.py`
- `get_current_mode` in: `mycelial_router_v2.py`
- `test_xyz_routing` in: `mycelial_router_v2.py`
- `calculate_xyz` in: `mycelial_router_v2.py`
- `route_fractal` in: `mycelial_router_v2.py`

---

## Cluster 270

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761529259.py`

**Archive** (3 files):
- `_archive_old/hive/versions/ember_brain_v2_1761529259.py`
- `_archive_old/hive/versions/ember_brain_v2_backup_1761529478.py`
- `_archive_old/hive/versions/ember_brain_v2_backup_1761529478.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_tokenizer` in: `ember_brain_v2_backup_1761529478.py`, `ember_brain_v2_1761529259.py`

---

## Cluster 271

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v1_backup_1761529259.py`

**Archive** (3 files):
- `_archive_old/hive/versions/ember_brain_v1_backup_1761530464.py`
- `_archive_old/hive/versions/ember_brain_v1_backup_1761529259.py`
- `_archive_old/hive/versions/ember_brain_v1_backup_1761530464.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_tool` in: `ember_brain_v1_backup_1761529259.py`, `ember_brain_v1_backup_1761530464.py`
- `parse_tool_calls` in: `ember_brain_v1_backup_1761529259.py`, `ember_brain_v1_backup_1761530464.py`
- `build_context_with_memories` in: `ember_brain_v1_backup_1761529259.py`, `ember_brain_v1_backup_1761530464.py`

---

## Cluster 272

**Reason**: Name variations of 'ember_brain'

**Keep**: `_archive_old/hive/branches/evolution_4_1761533869/ember_brain.py`

**Archive** (9 files):
- `_archive_old/hive/branches/evolution_4_1761533869/ember_brain.py`
- `_archive_old/hive/versions/ember_brain_v3_1761529478.py`
- `_archive_old/hive/versions/ember_brain_v3_1761529478.py`
- `_archive_old/hive/branches/evolution_4_1761535604/ember_brain.py`
- `_archive_old/hive/branches/saved_before_rollback_20251026_203742/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761535604/ember_brain.py`
- `_archive_old/hive/branches/saved_before_rollback_20251026_203742/ember_brain.py`
- `_archive_old/hive/versions/ember_brain_v3_backup_1761529546.py`
- `_archive_old/hive/versions/ember_brain_v3_backup_1761529546.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain.py`
- `init_thread_pool_executor` in: `ember_brain.py`
- `get_status` in: `ember_brain.py`
- `think` in: `ember_brain.py`
- `list_tools` in: `ember_brain.py`
- `execute_command` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `search_pod` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `read_file` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `list_directory` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `write_note` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `read_url` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain.py`, `ember_brain_v3_1761529478.py`
- `generate_text` in: `ember_brain.py`
- `web_search` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain_v3_1761529478.py`
- `analyze_data` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain_v3_1761529478.py`
- `generate_image` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain_v3_1761529478.py`
- `inference_with_thread` in: `ember_brain_v3_backup_1761529546.py`, `ember_brain_v3_1761529478.py`
- `think_internal` in: `ember_brain.py`

---

## Cluster 273

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v4_1761529546.py`

**Archive** (1 files):
- `_archive_old/hive/versions/ember_brain_v4_1761529546.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_tool` in: `ember_brain_v4_1761529546.py`
- `execute_tool_async` in: `ember_brain_v4_1761529546.py`
- `process_data_in_parallel` in: `ember_brain_v4_1761529546.py`
- `process_data` in: `ember_brain_v4_1761529546.py`

---

## Cluster 274

**Reason**: Name variations of 'ember_brain'

**Keep**: `_archive_old/hive/branches/evolution_4_1761535243/ember_brain.py`

**Archive** (17 files):
- `_archive_old/hive/branches/evolution_4_1761535243/ember_brain.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530456.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530456.py`
- `_archive_old/hive/branches/evolution_4_1761533733/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761533733/ember_brain.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531202.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531202_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531202.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531202_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761536367.py`
- `_archive_old/hive/branches/evolution_4_1761536341/ember_brain.py`
- `_archive_old/hive/versions/ember_brain_v2_1761536367.py`
- `_archive_old/hive/branches/evolution_4_1761536341/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761533632/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761533632/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761535479/ember_brain.py`
- `_archive_old/hive/branches/evolution_4_1761535479/ember_brain.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761530456.py`, `ember_brain.py`, `ember_brain_v2_1761536367.py`, `ember_brain_v2_1761531202.py`, `ember_brain_v2_1761531202_test.py`
- `generate_response` in: `ember_brain.py`
- `run_command` in: `ember_brain.py`
- `execute_tasks_in_parallel` in: `ember_brain.py`
- `get_tools` in: `ember_brain.py`
- `get_status` in: `ember_brain.py`
- `_generate_response` in: `ember_brain.py`
- `get_available_tools` in: `ember_brain.py`

---

## Cluster 275

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761530799.py`

**Archive** (3 files):
- `_archive_old/hive/versions/ember_brain_v2_1761530799_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530799.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530799_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761530799_test.py`, `ember_brain_v2_1761530799.py`
- `inference` in: `ember_brain_v2_1761530799_test.py`, `ember_brain_v2_1761530799.py`

---

## Cluster 276

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761530842_iter1.py`

**Archive** (3 files):
- `_archive_old/hive/versions/ember_brain_v2_1761530842_iter1_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530842_iter1.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530842_iter1_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_command` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `search_pod` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `generate` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `sequence` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `analyze` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `store` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`
- `retrieve` in: `ember_brain_v2_1761530842_iter1_test.py`, `ember_brain_v2_1761530842_iter1.py`

---

## Cluster 277

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761530885_iter2.py`

**Archive** (3 files):
- `_archive_old/hive/versions/ember_brain_v2_1761530885_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530885_iter2.py`
- `_archive_old/hive/versions/ember_brain_v2_1761530885_iter2_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_command` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `search_pod` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `generate` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `store_note` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `list_directory` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `read_url` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `web_search` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `analyze` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`
- `run_in_parallel` in: `ember_brain_v2_1761530885_iter2_test.py`, `ember_brain_v2_1761530885_iter2.py`

---

## Cluster 278

**Reason**: High function overlap (90%)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761531252_iter2.py`

**Archive** (7 files):
- `_archive_old/hive/versions/ember_brain_v2_1761531252_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531252_iter2.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531252_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531294_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531294_iter4_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531294_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531294_iter4_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `ember_brain_v2_1761531252_iter2.py`, `ember_brain_v2_1761531252_iter2_test.py`, `ember_brain_v2_1761531294_iter4_test.py`, `ember_brain_v2_1761531294_iter4.py`
- `execute_command` in: `ember_brain_v2_1761531252_iter2.py`, `ember_brain_v2_1761531252_iter2_test.py`, `ember_brain_v2_1761531294_iter4_test.py`, `ember_brain_v2_1761531294_iter4.py`
- `search_pod` in: `ember_brain_v2_1761531252_iter2.py`, `ember_brain_v2_1761531252_iter2_test.py`, `ember_brain_v2_1761531294_iter4_test.py`, `ember_brain_v2_1761531294_iter4.py`
- `read_file` in: `ember_brain_v2_1761531252_iter2.py`, `ember_brain_v2_1761531252_iter2_test.py`, `ember_brain_v2_1761531294_iter4_test.py`, `ember_brain_v2_1761531294_iter4.py`
- `write_note` in: `ember_brain_v2_1761531252_iter2.py`, `ember_brain_v2_1761531252_iter2_test.py`

---

## Cluster 279

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761531595_iter1.py`

**Archive** (19 files):
- `_archive_old/hive/versions/ember_brain_v2_1761531595_iter1_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531643_iter2.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531643_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531693_iter3.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531693_iter3_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531743_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531743_iter4_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531595_iter1.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531595_iter1_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531643_iter2.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531643_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531693_iter3.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531693_iter3_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531743_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531743_iter4_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531546.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531546_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531546.py`
- `_archive_old/hive/versions/ember_brain_v2_1761531546_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `execute_command` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `search_pod` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `read_file` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `list_directory` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `write_note` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `read_url` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`
- `web_search` in: `ember_brain_v2_1761531743_iter4.py`, `ember_brain_v2_1761531743_iter4_test.py`, `ember_brain_v2_1761531595_iter1.py`, `ember_brain_v2_1761531595_iter1_test.py`, `ember_brain_v2_1761531546_test.py`, `ember_brain_v2_1761531643_iter2_test.py`, `ember_brain_v2_1761531643_iter2.py`, `ember_brain_v2_1761531546.py`, `ember_brain_v2_1761531693_iter3.py`, `ember_brain_v2_1761531693_iter3_test.py`

---

## Cluster 280

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761532121_iter2.py`

**Archive** (19 files):
- `_archive_old/hive/versions/ember_brain_v2_1761532121_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532162_iter3.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532162_iter3_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532121_iter2.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532121_iter2_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532162_iter3.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532162_iter3_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532079_iter1.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532079_iter1_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532079_iter1.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532079_iter1_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532201_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532201_iter4_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532201_iter4.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532201_iter4_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532035.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532035_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532035.py`
- `_archive_old/hive/versions/ember_brain_v2_1761532035_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_tool` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`
- `thread_task` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`
- `load_model` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`
- `status` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`
- `think` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`
- `tools` in: `ember_brain_v2_1761532079_iter1.py`, `ember_brain_v2_1761532035_test.py`, `ember_brain_v2_1761532201_iter4.py`, `ember_brain_v2_1761532121_iter2_test.py`, `ember_brain_v2_1761532121_iter2.py`, `ember_brain_v2_1761532035.py`, `ember_brain_v2_1761532201_iter4_test.py`, `ember_brain_v2_1761532079_iter1_test.py`, `ember_brain_v2_1761532162_iter3.py`, `ember_brain_v2_1761532162_iter3_test.py`

---

## Cluster 281

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761533662.py`

**Archive** (3 files):
- `_archive_old/hive/branches/evolution_4_1761533632/ember_brain_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761533662.py`
- `_archive_old/hive/branches/evolution_4_1761533632/ember_brain_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_test.py`, `ember_brain_v2_1761533662.py`
- `_generate_response` in: `ember_brain_test.py`, `ember_brain_v2_1761533662.py`

---

## Cluster 282

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761533758.py`

**Archive** (3 files):
- `_archive_old/hive/branches/evolution_4_1761533733/ember_brain_test.py`
- `_archive_old/hive/versions/ember_brain_v2_1761533758.py`
- `_archive_old/hive/branches/evolution_4_1761533733/ember_brain_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_test.py`, `ember_brain_v2_1761533758.py`
- `execute_tasks_in_parallel` in: `ember_brain_test.py`, `ember_brain_v2_1761533758.py`
- `get_tools` in: `ember_brain_test.py`, `ember_brain_v2_1761533758.py`
- `get_status` in: `ember_brain_test.py`, `ember_brain_v2_1761533758.py`

---

## Cluster 283

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761533903.py`

**Archive** (1 files):
- `_archive_old/hive/versions/ember_brain_v2_1761533903.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761533903.py`
- `init_thread_pool_executor` in: `ember_brain_v2_1761533903.py`
- `get_status` in: `ember_brain_v2_1761533903.py`
- `think` in: `ember_brain_v2_1761533903.py`
- `list_tools` in: `ember_brain_v2_1761533903.py`
- `execute_command` in: `ember_brain_v2_1761533903.py`
- `search_pod` in: `ember_brain_v2_1761533903.py`
- `read_file` in: `ember_brain_v2_1761533903.py`
- `list_directory` in: `ember_brain_v2_1761533903.py`
- `write_note` in: `ember_brain_v2_1761533903.py`
- `read_url` in: `ember_brain_v2_1761533903.py`
- `generate_text` in: `ember_brain_v2_1761533903.py`

---

## Cluster 284

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761535284.py`

**Archive** (1 files):
- `_archive_old/hive/versions/ember_brain_v2_1761535284.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761535284.py`
- `generate_response` in: `ember_brain_v2_1761535284.py`
- `run_command` in: `ember_brain_v2_1761535284.py`

---

## Cluster 285

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761535504.py`

**Archive** (1 files):
- `_archive_old/hive/versions/ember_brain_v2_1761535504.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761535504.py`
- `get_status` in: `ember_brain_v2_1761535504.py`
- `get_available_tools` in: `ember_brain_v2_1761535504.py`

---

## Cluster 286

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/versions/ember_brain_v2_1761535643.py`

**Archive** (1 files):
- `_archive_old/hive/versions/ember_brain_v2_1761535643.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_model_and_tokenizer` in: `ember_brain_v2_1761535643.py`
- `get_status` in: `ember_brain_v2_1761535643.py`
- `think_internal` in: `ember_brain_v2_1761535643.py`
- `list_tools` in: `ember_brain_v2_1761535643.py`
- `read_file` in: `ember_brain_v2_1761535643.py`
- `list_directory` in: `ember_brain_v2_1761535643.py`

---

## Cluster 287

**Reason**: Name variations of 'ember_brain_test'

**Keep**: `_archive_old/hive/branches/test_simple_change/ember_brain_test.py`

**Archive** (11 files):
- `_archive_old/hive/branches/test_simple_change/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535604/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535604/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535243/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535243/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761536341/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761536341/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535479/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761535479/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761533869/ember_brain_test.py`
- `_archive_old/hive/branches/evolution_4_1761533869/ember_brain_test.py`

**⚠️ Unique Functions** (may need manual merge):
- `format_results` in: `ember_brain_test.py`
- `get_ember_tools` in: `ember_brain_test.py`
- `execute_tool` in: `ember_brain_test.py`
- `parse_tool_calls` in: `ember_brain_test.py`
- `build_context_with_memories` in: `ember_brain_test.py`
- `__init__` in: `ember_brain_test.py`
- `load_index` in: `ember_brain_test.py`
- `save_index` in: `ember_brain_test.py`
- `should_index_file` in: `ember_brain_test.py`
- `get_file_hash` in: `ember_brain_test.py`
- `index_pod` in: `ember_brain_test.py`
- `keyword_search` in: `ember_brain_test.py`
- `semantic_search` in: `ember_brain_test.py`
- `search` in: `ember_brain_test.py`
- `log_tool_use` in: `ember_brain_test.py`
- `search_pod` in: `ember_brain_test.py`
- `read_file` in: `ember_brain_test.py`
- `write_note` in: `ember_brain_test.py`
- `list_directory` in: `ember_brain_test.py`
- `check_system_status` in: `ember_brain_test.py`
- `execute_command` in: `ember_brain_test.py`
- `get_recent_learnings` in: `ember_brain_test.py`
- `reflect_on_tool_usage` in: `ember_brain_test.py`
- `load_model_and_tokenizer` in: `ember_brain_test.py`
- `get_status` in: `ember_brain_test.py`
- `think_internal` in: `ember_brain_test.py`
- `list_tools` in: `ember_brain_test.py`
- `generate_response` in: `ember_brain_test.py`
- `run_command` in: `ember_brain_test.py`
- `get_available_tools` in: `ember_brain_test.py`
- `init_thread_pool_executor` in: `ember_brain_test.py`
- `think` in: `ember_brain_test.py`
- `read_url` in: `ember_brain_test.py`
- `generate_text` in: `ember_brain_test.py`

---

## Cluster 288

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle1_20251027_034133.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle1_20251027_034133.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle1_20251027_034133.py`
- `add_data` in: `v2_from_dream_cycle1_20251027_034133.py`
- `transform` in: `v2_from_dream_cycle1_20251027_034133.py`
- `filter` in: `v2_from_dream_cycle1_20251027_034133.py`
- `combine` in: `v2_from_dream_cycle1_20251027_034133.py`
- `generate` in: `v2_from_dream_cycle1_20251027_034133.py`
- `sequence` in: `v2_from_dream_cycle1_20251027_034133.py`
- `analyze` in: `v2_from_dream_cycle1_20251027_034133.py`
- `store` in: `v2_from_dream_cycle1_20251027_034133.py`
- `retrieve` in: `v2_from_dream_cycle1_20251027_034133.py`
- `execute_command` in: `v2_from_dream_cycle1_20251027_034133.py`
- `search_pod` in: `v2_from_dream_cycle1_20251027_034133.py`
- `read_file` in: `v2_from_dream_cycle1_20251027_034133.py`
- `write_note` in: `v2_from_dream_cycle1_20251027_034133.py`
- `list_directory` in: `v2_from_dream_cycle1_20251027_034133.py`
- `read_url` in: `v2_from_dream_cycle1_20251027_034133.py`
- `web_search` in: `v2_from_dream_cycle1_20251027_034133.py`

---

## Cluster 289

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle2_20251027_034637.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle2_20251027_034637.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle2_20251027_034637.py`
- `compile` in: `v2_from_dream_cycle2_20251027_034637.py`

---

## Cluster 290

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle3_20251027_035206.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle3_20251027_035206.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle3_20251027_035206.py`
- `transform` in: `v2_from_dream_cycle3_20251027_035206.py`
- `normalize` in: `v2_from_dream_cycle3_20251027_035206.py`
- `standardize` in: `v2_from_dream_cycle3_20251027_035206.py`

---

## Cluster 291

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle4_20251027_035715.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle4_20251027_035715.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle4_20251027_035715.py`
- `execute_command` in: `v2_from_dream_cycle4_20251027_035715.py`
- `search_pod` in: `v2_from_dream_cycle4_20251027_035715.py`
- `read_file` in: `v2_from_dream_cycle4_20251027_035715.py`
- `write_note` in: `v2_from_dream_cycle4_20251027_035715.py`
- `list_directory` in: `v2_from_dream_cycle4_20251027_035715.py`
- `read_url` in: `v2_from_dream_cycle4_20251027_035715.py`
- `web_search` in: `v2_from_dream_cycle4_20251027_035715.py`
- `transform` in: `v2_from_dream_cycle4_20251027_035715.py`
- `filter` in: `v2_from_dream_cycle4_20251027_035715.py`
- `combine` in: `v2_from_dream_cycle4_20251027_035715.py`
- `generate` in: `v2_from_dream_cycle4_20251027_035715.py`
- `sequence` in: `v2_from_dream_cycle4_20251027_035715.py`
- `analyze` in: `v2_from_dream_cycle4_20251027_035715.py`
- `store_retrieve` in: `v2_from_dream_cycle4_20251027_035715.py`

---

## Cluster 292

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle5_20251027_040244.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle5_20251027_040244.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle5_20251027_040244.py`
- `transform` in: `v2_from_dream_cycle5_20251027_040244.py`
- `filter` in: `v2_from_dream_cycle5_20251027_040244.py`
- `combine` in: `v2_from_dream_cycle5_20251027_040244.py`
- `generate` in: `v2_from_dream_cycle5_20251027_040244.py`
- `sequence` in: `v2_from_dream_cycle5_20251027_040244.py`
- `analyze` in: `v2_from_dream_cycle5_20251027_040244.py`
- `store` in: `v2_from_dream_cycle5_20251027_040244.py`
- `retrieve` in: `v2_from_dream_cycle5_20251027_040244.py`

---

## Cluster 293

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle6_20251027_040800.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle6_20251027_040800.py`

**⚠️ Unique Functions** (may need manual merge):
- `execute_command` in: `v2_from_dream_cycle6_20251027_040800.py`
- `search_pod` in: `v2_from_dream_cycle6_20251027_040800.py`
- `read_file` in: `v2_from_dream_cycle6_20251027_040800.py`
- `write_note` in: `v2_from_dream_cycle6_20251027_040800.py`
- `list_directory` in: `v2_from_dream_cycle6_20251027_040800.py`
- `read_url` in: `v2_from_dream_cycle6_20251027_040800.py`
- `web_search` in: `v2_from_dream_cycle6_20251027_040800.py`

---

## Cluster 294

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle7_20251027_041309.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle7_20251027_041309.py`

**⚠️ Unique Functions** (may need manual merge):
- `load_data` in: `v2_from_dream_cycle7_20251027_041309.py`
- `preprocess_data` in: `v2_from_dream_cycle7_20251027_041309.py`
- `train_model` in: `v2_from_dream_cycle7_20251027_041309.py`
- `evaluate_model` in: `v2_from_dream_cycle7_20251027_041309.py`
- `main` in: `v2_from_dream_cycle7_20251027_041309.py`

---

## Cluster 295

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle8_20251027_041821.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle8_20251027_041821.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle8_20251027_041821.py`
- `transform` in: `v2_from_dream_cycle8_20251027_041821.py`
- `filter` in: `v2_from_dream_cycle8_20251027_041821.py`
- `combine` in: `v2_from_dream_cycle8_20251027_041821.py`
- `generate` in: `v2_from_dream_cycle8_20251027_041821.py`
- `sequence` in: `v2_from_dream_cycle8_20251027_041821.py`
- `analyze` in: `v2_from_dream_cycle8_20251027_041821.py`
- `store_retrieve` in: `v2_from_dream_cycle8_20251027_041821.py`
- `execute_command` in: `v2_from_dream_cycle8_20251027_041821.py`
- `search_pod` in: `v2_from_dream_cycle8_20251027_041821.py`
- `read_file` in: `v2_from_dream_cycle8_20251027_041821.py`
- `write_note` in: `v2_from_dream_cycle8_20251027_041821.py`
- `list_directory` in: `v2_from_dream_cycle8_20251027_041821.py`
- `read_url` in: `v2_from_dream_cycle8_20251027_041821.py`
- `web_search` in: `v2_from_dream_cycle8_20251027_041821.py`

---

## Cluster 296

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle9_20251027_042407.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle9_20251027_042407.py`

**⚠️ Unique Functions** (may need manual merge):
- `__init__` in: `v2_from_dream_cycle9_20251027_042407.py`
- `execute_command` in: `v2_from_dream_cycle9_20251027_042407.py`
- `search_pod` in: `v2_from_dream_cycle9_20251027_042407.py`
- `read_file` in: `v2_from_dream_cycle9_20251027_042407.py`
- `write_note` in: `v2_from_dream_cycle9_20251027_042407.py`
- `list_directory` in: `v2_from_dream_cycle9_20251027_042407.py`
- `read_url` in: `v2_from_dream_cycle9_20251027_042407.py`
- `web_search` in: `v2_from_dream_cycle9_20251027_042407.py`
- `transform` in: `v2_from_dream_cycle9_20251027_042407.py`
- `filter` in: `v2_from_dream_cycle9_20251027_042407.py`
- `combine` in: `v2_from_dream_cycle9_20251027_042407.py`
- `generate` in: `v2_from_dream_cycle9_20251027_042407.py`
- `sequence` in: `v2_from_dream_cycle9_20251027_042407.py`
- `analyze` in: `v2_from_dream_cycle9_20251027_042407.py`
- `store_retrieve` in: `v2_from_dream_cycle9_20251027_042407.py`
- `run_task` in: `v2_from_dream_cycle9_20251027_042407.py`
- `log` in: `v2_from_dream_cycle9_20251027_042407.py`

---

## Cluster 297

**Reason**: Exact duplicates (same content)

**Keep**: `_archive_old/hive/dream_generated/v2_from_dream_cycle10_20251027_042913.py`

**Archive** (1 files):
- `_archive_old/hive/dream_generated/v2_from_dream_cycle10_20251027_042913.py`

**⚠️ Unique Functions** (may need manual merge):
- `transform_values` in: `v2_from_dream_cycle10_20251027_042913.py`
- `filter_matters` in: `v2_from_dream_cycle10_20251027_042913.py`
- `combine_elements` in: `v2_from_dream_cycle10_20251027_042913.py`
- `generate_patterns` in: `v2_from_dream_cycle10_20251027_042913.py`
- `sequence_events` in: `v2_from_dream_cycle10_20251027_042913.py`
- `analyze_properties` in: `v2_from_dream_cycle10_20251027_042913.py`
- `store_retrieve` in: `v2_from_dream_cycle10_20251027_042913.py`

---

## Cluster 298

**Reason**: High function overlap (100%)

**Keep**: `_archive_old/training/train_continuation_lora.py`

**Archive** (1 files):
- `_archive_old/training/train_embodiment_lora.py`

---

