<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0621.txt",
      "sha256": "c165a2e2982091131e0d7312b601e31f57a4381153f1e3f0c98a9274c79095fb",
      "bytes": 13811
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "abc167c4472c829d86b53b8d4f797cff9bf62b726424086a9a74438bba102dd5",
      "bytes": 1621
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b01d2bde321f6145223c45c20c2318293d773ed5aed33f68da3356197d6e01a2",
      "bytes": 192548
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "92d575fe53e56ded93f299d2a5549b4d40ed1f041efa23060fd69953fa44bc66",
      "bytes": 1206
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8a3be771ba89def8c7c7f491fa38a323f1dd4cf0a0b000ce61a22a2262d03e03",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "833003613421fb0978339a0817dcaacaafacaeadcd2e2af55b9bd6c0771a520a",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6299251f568eadc39c970d5413374563df53e5e4f06fcd9d521d32e63db1735d",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "7f5a1063a30f398ebe544503acea76e083df0f436eb3cb4aaaefe124e3c752f4",
      "bytes": 809
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "ede8af0436dd4e24e6c43178567c6b3c3c47e13ba5d3b19b4aaae8b2fdf17c1e",
      "bytes": 899
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "25505abb69647c21e2c02f2643c254c5e2254c8e74d4915f98fdf564cfafc17f",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "de59e238d4a4a858c63010f92c0905a742a14ce3f24ad3909f6a0a2c8a97b522",
      "bytes": 195497
    }
  ],
  "estimated_tokens": 12659
}
-->

# Durable State Update — Chapter 621

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 621. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 621. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 621,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 621,
    "continuity_sources": [621],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Fire Dragon Pavilion has completed contact with Namho, a Hidden Shadow Pavilion agent operating under the cover of the Poison Flower Pavilion in Nanman.",
    "Namho spent more than fifty years mapping Nanman’s terrain and tribal locations and has given the Fire Dragon Pavilion his wooden map.",
    "Namho has left his residence and agreed to guide the Fire Dragon Pavilion toward its Nanman destination.",
    "Namho received the Pavilion Master’s warning about the rift through a messenger eagle.",
    "Namho and Jin Taekyung believe Dark Heaven is targeting Nanman and that a major catastrophe is imminent.",
    "The Contact with a Hidden Shadow Pavilion Agent mission and Seeds Planted in Nanman Quest are complete.",
    "A new linked Quest has been generated.",
    "The Fire Dragon Pavilion’s Nanman mission, including its objective at the Nanman Beast Palace, remains active."
  ],
  "continuity_sources": [
    620
  ],
  "open_questions": [
    "What is the objective of the newly generated linked Quest?",
    "Was the woman in the Heavenly Demon Escort Bureau group the Southern Heaven Demon Empress?",
    "Who poisoned and killed the Heavenly Demon Escort Bureau group, and why?",
    "What catastrophe will Dark Heaven cause in Nanman?",
    "What dangers await the Fire Dragon Pavilion at the Nanman Beast Palace?"
  ],
  "safe_through": 620,
  "temporary_decisions": [
    "Render 南琥, Namho’s code name, as Namho rather than translating it literally as southern amber.",
    "Use Elder Chao for the local title 챠오 어르신."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 무당파    | **Wudang**                       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 십만마병 | **hundred thousand demonic soldiers** | Army fielded by the Demonic Cult during the Great Faction War. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 청계천 | **Cheonggyecheon** | Stream invoked in Taekyung's joke about Dark Heaven. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 영인 | **Yeongin** | Remote county seat in Yunnan and the party's immediate destination. |
| 천마표국 | **Heavenly Demon Escort Bureau** | A Sichuan group whose arrival preceded the Yeongin massacre; all members were later found dead from venom. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 620
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 616
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 620
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 620
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 620
- **Aliases:** Elder Chao
- **Role:** Namho is a non-Han Hidden Shadow Pavilion agent who operated for decades under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 620
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 620
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃621화



“가세. 자네들의 목표가 어디든, 내가 앞장서지.”

나는 고령에 접어들었음에도 굳은 의지를 보이는 늙은 은영각 요원, 남호를 감동 어린 시선으로 바라보았다.

“설령 저승길이라 해도 앞장서시겠다니. 남 노인께서 보여 주신 의기(義氣)에 뭐라 말씀을 드려야 할지 모르겠습니다.”

“아니, 저승길까지 따라간다고 하진 않았는데…….”

“요즘 들어 뼈마디도 시큰거리고, 기억도 자주 깜빡하실 텐데 이렇게 나서 주셔서 감사합니다. 저희에게는 큰 도움이 될 겁니다.”

“……참 고맙군. 자네 말을 듣고 있자니 이 늙은이의 전신에서 힘과 의욕이 샘솟는 것 같아.”

“천만에요. 고마워하실 필요 없습니다.”

떫은 표정으로 나를 응시하던 남호가 문득 입을 열었다.

“한데 어디로 갈 셈인가? 내 생각은 다를 수도 있지만, 우선 자네들이 원하는 목적지를 듣고 싶군.”

목적지라. 나는 대답 대신 허공을 힐끗 바라보았다.

허공은 말 그대로 아무것도 없는 텅 빈 공간일 뿐이다.

그러나 지금껏 수도 없이 그랬듯, 내 눈에는 저 허공에서 이 자리의 누구도 볼 수 없는 정보가 읽혔다.



퀘스트



[남만야수궁]



남만야수궁은 새외(塞外)로 분류되는 대표적인 거대 세력 중 하나로, 지극히 폐쇄적인 남만 땅에서도 가장 깊숙하고 은밀한 곳에 자리 잡았습니다.

그러나 중원 무림은 곧 다가올 대전쟁을 위하여 그들의 도움이 필요한 상황. 이제는 오랫동안 잠들어 있던 밀림의 맹수를 깨워야 할 시간입니다.

혹은…… 아직 드러나지 않은 위기에 처한 맹수를 구하거나.



등급 : 초절정

제한 : 진태경 및 화룡각 인원

임무 : 남만야수궁에 도착 (미완료)

보상 : 연계 퀘스트

 ???

실패 : ???





그건 남호를 만난 직후 새롭게 갱신된 연계 퀘스트였고, 내 생각과 일치하는 이정표이기도 했다.

“남만야수궁. 남만야수궁으로 갈 생각입니다.”

뒤늦게 흘러나온 내 대답에, 남호가 깊게 가라앉은 눈빛으로 고개를 끄덕였다.



* * *



남만은 광활하면서도 험준하기 그지없는 땅이었다.

대지 면적으로 치자면 사천(四川)보다 좁지만, 이동하는 것에 있어 들어가는 수고는 중원 땅에 비할 바가 아니었다.

“일전에 각주께서 그런 말씀을 하신 적이 있지. 남만에서의 십 리는, 중원의 백 리와 같다고.”

이런 남호의 말을 이해하지 못하는 이가 있다면, 그 사람은 아직 남만 땅을 밟아 보지 못한 사람일 것이다.

나를 비롯한 화룡각 대원들은 불과 한나절 만에 남만이 얼마나 좆 같은 땅인지 똑똑히 깨달았으니까.

위이잉. 탁!

“무진아, 방금 무슨 소리였냐?”

“별거 아닙니다. 그냥 모기예요. 갑자기 목덜미가 따끔하길래 뭔가 했네요.”

“아, 그래? 그래도 조심해. 혹시 모르니까 남 노인 불러서 물어볼까?”

“에이, 조장님도 참. 제가 무슨 어린앱니까. 열화신룡의 오른편에서 숱한 격전을 치른 역전의 무사 혁무진! 그게 바로 접니다.”

그리고 정확히 한 시진 후, 역전의 무사 혁무진은 구토와 함께 쓰러졌다.

“우웨에에엑!”

“헉, 무진아!”

“이게 무슨 일인가!”

“남 노인! 무진이가 쓰러졌습니다!”

“내가 아무리 늙었어도 쓰러진 건 다 보여. 혹시 모기에 물렸나?”

“쿨럭, 예에. 한 시진 전쯤에 푸른 줄무늬가 있는 놈한테…….”

“푸른 줄무늬? 그것도 한 시진 전? 해독제. 빨리 해독제 가져와!”

다행히 역전의 무사를 일으켜 세우는 것은 그리 어렵지 않았다.

내게는 사천당가의 신물인 만독지환(萬毒指環)과 퀘스트 보상으로 받은 해독제가 오십 개나 있었으니까.

하지만 그렇다고 해서 안심할 상황은 아니었다.

“본래는 수십 마리씩 무리를 지어 몰려다니며 맹수까지 사냥하는 놈들이지. 한 시진만 더 늦었어도 이 세상 사람이 아니었을 걸세.”

남호의 엄중한 경고와 함께 우리는 다시 이동을 시작했다. 한족이라면 눈깔을 뒤집고 달려드는 이민족들의 눈을 피해 더 깊숙하고 은밀한 곳으로.

그리고 그건, 더욱 위험한 곳으로 향하고 있다는 뜻이었다.

“태산이! 태산이 배가 너무 아프다! 찢어질 것 같다!”

“남 노인!”

“또 뭘 처먹었어!”

“태산이. 배가 고파서 나무에 피어 있던 붉은 버섯을 뜯어 먹었다.”

“이런 천하의 개돼지 같은 놈을 보았나! 내 그토록 주의를 줬거늘, 단순히 허기가 졌다고 해서 호랑이도 못 버티는 혈생균(血牲菌)을 처먹어? 이건 해독제도 안 통해!”

극대노를 몸소 시전한 남호였지만 그의 분노는 이내 당혹스러움으로 바뀌었다.

호랑이도 못 버틴다는 혈생균인지 뭔지를 처먹은 태산이 풀숲으로 들어가 거사를 치른 뒤에 씻은 듯이 나았기 때문이었다.

“태산이. 다 싸고 나니까 편안하다. 이제 괜찮다.”

“……저놈. 사람 맞나?”

진심이 담긴 남호의 물음에 잠시 고민하던 사마표가 자신 없는 목소리로 대답했다.

“아마도 그럴 거요.”

“태산이. 속이 비니까 다시 배가 고프다.”

“내 천지신명께 맹세컨대, 두 번 다시 버섯 따위를 처먹었다가는 영영 허기질 일이 없게 될 줄 알아라.”

“오오. 태산이. 솔깃하다.”

“……후회되는군. 만약 무공을 익혔다면 지금쯤 저놈을 일장에 쳐 죽였을 텐데.”

늙은 은영각 요원의 한탄을 뒤로하고 걸음은 계속해서 이어졌다.

발길이 닿는 곳마다 빽빽한 밀림과 습하면서도 무더운 열기가 우리를 기다리고 있었고, 우거진 풀숲과 늪지대 곳곳에 도사린 맹수들의 눈동자는 샛노랗게 빛났다.

‘혹시 남만이 아니라 아마존에 온 건가.’

말 그대로 개똥 땅.

뭔 놈의 동네가 이 모양인지, 호랑이가 대학가 원룸촌 길냥이보다 많이 보이고 악어는 청계천 올챙이처럼 우글거린다.

물론 이마저도 향만 맡아도 훅 간다는 기화독초(奇花毒草)와 제 몸통보다 큰 독침을 달고 다니는 벌에 비교하면 애교 수준이었다.

그나마 맹수들은 덩치가 큰 탓에 눈에 띄기라도 하니까.

영인을 떠난 지 하루 이틀 만에 혁무진이 앓는 소리를 한 것에는 그만한 이유가 있었다.

“남만야수궁이고 나발이고, 내일모레쯤 뒈질 것 같습니다.”

내일모레까진 아니더라도, 나흘 후에는 생명이 위험해 보이긴 했다. 첫날에만 네 번 정도 중독된 녀석은 지난 이틀 사이 피골이 상접 해 있었으니까.

산서성도 중원의 시각으로는 변경(邊境)에 속한 곳이지만, 남만의 수준은 예상했던 범위를 훌쩍 뛰어넘었다.

“이러지 말고 다른 길로 가면 안 됩니까? 좀 후지고 험하긴 해도 이곳에 비하면 완전 꽃길이나 다름없을 텐데.”

남만에도 길이 아예 없는 것은 아니다.

중원에 비하면 심하게 낙후되었지만, 남만에 자리 잡은 수십, 수백여 갈래의 이민족들은 저마다의 구역을 정하고 분쟁이 일어나지 않는 선에서 왕래를 하는 경우도 그리 드물지는 않다고 들었다.

그러나 간절한 혁무진의 청원에도 남호의 대답은 단호했다.

“불가(不可). 그 이유는 자네도 알겠지?”

“저희를 죽이고 싶어서 환장한 이민족 때문이라면, 차라리 시원하게 맞서 싸우고 말겠습니다. 만약 대화로 잘 풀 수 있다면 그걸로 좋은 거고요.”

“대화?”

꿈과 희망이 가득한 혁무진의 대답에 남호가 눈을 깜빡였다.

“진심인가?”

“물론입니다.”

“마을 하나가 사라졌네. 호의로 한족들을 맞이한 이백여 명이 남녀노소 가리지 않고 도륙당했다고. 그런데 대화가 통할 것 같나?”

“……아뇨. 사실 진심은 아니었습니다.”

“이제야 좀 솔직해졌군. 좋아, 그럼 닥치고 가자고.”

“옙.”

혁가 놈. 빛보다 빠른 태세 전환 보소.

하지만 이번만큼은 남호의 말이 구구절절 옳았다.

당장 우리에게 덤벼드는 이민족과 맞서 싸운다는 소리는 남만 전체와 전쟁을 치르겠다는 말과 동의어다.

평소에는 서로를 향해 으르렁거리다가도, 외부의 적이 나타난다면 언제 그랬냐는 듯이 똘똘 뭉치는 것이 남만의 특징 중 하나라고 했다.

‘그러니 정마대전 당시의 마교조차 남만을 완전히 정벌하지 못했겠지.’

한때 천하의 절반을 집어삼켰던 마교의 십만마병(十萬魔兵)도 남만 외곽에 깃발만 꽂고 물러나는 것이 고작이었다.

남만의 지독한 풍토병과 험난한 지형. 그리고 온갖 맹수와 독물이 득실거리는 이 밀림에 그 이상 깊숙이 들어선다면 득보다 실이 클 것을 알았기 때문이다.

‘그렇다고 신상을 까고 돌아다닐 수도 없는 노릇이고.’

한족 혐오 감정이 팽배한 이민족들이 그 정도로 적대감을 누그러트릴지도 의문이지만, 더 중요한 건 바로 남만 어딘가에 도사리고 있을 암천(暗天)의 존재였다.

‘놈들은 반드시 남만을 노린다. 일이 터지는 건 시간문제일 뿐이야.’

이건 확신에 가까운 짐작이었다. 괜히 우리가 무림맹 총단이 위치한 하남에서부터 밤손님처럼 은밀하게 이동한 것이 아니다.

남만까지 오는 과정에서 부득이하게 수룡채의 수적들에게 신분을 노출하긴 했지만, 입단속도 철저히 했다.

지난번 사천행에서 인연을 쌓았던 아미파와 청성파, 그리고 사천당가에 굳이 연통을 넣지 않았던 이유도 그 때문이었다.

하지만 우리가 이민족들에게 신분을 밝힌다면 그동안의 노력이 전부 허사가 된다.

보이지 않던 비수가 코앞까지 다가온 것을 깨달은 암천은 계획에 더욱 박차를 가할 테고, ‘균열’과 함께 재앙의 문이 열릴 테니까.

‘신분을 밝히는 것은 최소한 남만야수궁에 도착한 뒤여야 해.’

남만야수궁의 궁주인 야수묘왕(野獸苗王)은 정마대전에 참전했던 전력이 있을뿐더러, 적천강과 열화문에 호의를 품고 있다고 들었다.

일의 경중이나 남만에서 차지하는 위상으로 따져 보아도, 눈깔이 뒤집힌 여타 이민족들보다는 훨씬 말이 통하는 상대인 것이다.

‘그나저나 천마표국인지 뭔지 하는 놈들 때문에 우리한테까지 똥이 튀네.’

어물전 망신은 꼴뚜기가 다 시킨다더니, 괜히 동족 패키지 상품으로 같이 묶여서 나나 화룡각 대원들 이미지만 개박살이 났다.

심지어 나는 한족 출신도 아닌데.

‘……이게 폰한족인지 뭔지 하는 그거냐.’

더럽게 억울해도 방법이 없다.

남만 이민족들한테 ‘사실 전 한족이 아니라, 한민족입니다. 노스말고 사우스요.’ 이 지랄 떨어 봤자 알아듣지도 못할 게 뻔하니까.

안 그래도 전에 구화산에서 수련했을 때 향수병이 돋아서 태극기를 그렸더니 적천강이 딱 한 마디 하더라.



‘무당파냐?’

‘아닌데요.’

‘딱 봐도 태극인데 무슨 개소리냐. 태극 하면 무당파다.’

‘태극 하면 한국인데요.’

‘한국이 뭔데?’

‘그게……. 아니다. 노야는 모르셔도 됩니다.’

‘철구 이백 근 추가.’

‘……이백 근? 왜요?’

‘몰라도 된다.’



다시 떠올려봐도 눈물샘만 자극하는 기억이다.

이역만리 머나먼 타차원 땅에서 개고생하던 게 엊그제 같은데, 그 개고생이 언제나 현재 진행형이라는 사실이 개탄스럽다.

“후우.”

한숨을 내뱉는 내 모습에 남호가 쌍심지를 켰다.

“왜. 자네도 지금 당장 내려가서 대화로 해결하고 싶나? 아니면 이민족들이랑 대차게 한판 붙든가?”

“……갑자기 급발진 하시네. 그럴 생각은 쥐똥만큼도 없습니다.”

“그거 다행이군.”

대차게 한판 붙을 일은 지금까지도 많았고 앞으로도 많다. 당장 주위를 배회하며 울음소리를 흘리는 맹수들만 해도 몇 마리인가.

빽빽하게 늘어선 밀림과 늪지대를 훑어본 나는 남호에게 물었다.

“얼마나 남았습니까?”

“짧으면 사흘. 길면 엿새.”

“생각보다 너무 많이 남았네요.”

“이목을 피해 이동하는 것을 생각하면 이마저도 짧은 걸세.”

부쩍 늙은 얼굴로 허리를 두드린 남호가 재차 발걸음을 옮겼다.

“지금부터는 단 한 순간도 걸음을 늦추지 말게. 오늘 중으로 애뇌산(哀牢山)을 넘는다면, 늦어도 나흘 뒤에는 남만야수궁에 도착할 수 있을 테니.”

남호의 말은 사실이었다.

정확히 나흘 뒤, 어느 높은 산봉우리를 지나던 우리는 저 멀리 깊은 운무(雲霧)에 휩싸인 거대한 건축물을 확인할 수 있었다.

“남만야수궁…….”

누군가의 입술 사이로 흘러나온 목소리가, 어디선가 불어온 바람을 타고 퍼져 나갔다.
```

## Final English reading copy

```markdown
# Chapter 621

“Let’s go. Wherever your destination is, I’ll lead the way.”

I looked at Namho, the elderly Hidden Shadow Pavilion agent, with admiration. Despite his advanced age, he was showing an iron will.

“You’re saying you’ll lead us even if our destination is the afterlife. I don’t know what to say in response to the sense of honor you’ve shown us, Elder Namho.”

“No, I never said I’d follow you to the afterlife…”

“Your joints must ache these days, and you probably find yourself forgetting things more often, too. Thank you for stepping forward like this. It’ll be a great help to us.”

“……How very kind of you. Listening to you, I feel as if strength and motivation are welling up throughout this old body of mine.”

“You’re welcome. There’s no need to thank me.”

Namho stared at me with a sour expression before suddenly opening his mouth.

“But where are we going? I may have a different idea, but I’d like to hear your desired destination first.”

Destination, huh?

Instead of answering, I glanced up at the empty air.

The space above us was, quite literally, an empty void where there was nothing at all.

But just as it had happened countless times before, I could read information in that empty space—information that no one else here could see.



> **System**
>
> **Quest**
>
> **Nanman Beast Palace**
>
> The Nanman Beast Palace is one of the representative great powers classified as part of the Outer Lands, and it is located in the deepest, most secluded part of Nanman—a land that is already extremely closed off.
>
> However, the Murim of the Central Plains now needs their help for the Great War that is soon to come. The time has come to awaken the beast of the jungle that has slept for so long.
>
> Or perhaps… to save the beast from a crisis that has yet to reveal itself.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Arrive at the Nanman Beast Palace (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** ???



It was the Chain Quest that had been newly updated right after meeting Namho, and it was also a signpost that matched my own thoughts.

“The Nanman Beast Palace. We’re heading to the Nanman Beast Palace.”

At my belated answer, Namho nodded with deeply sunken eyes.

* * *

Nanman was an expansive land, but it was also unbelievably rugged.

In terms of land area, it was smaller than Sichuan, but the effort required to travel through it was incomparable to anything in the Central Plains.

“The Pavilion Master once said this: ten li in Nanman is the same as a hundred li in the Central Plains.”

Anyone who couldn’t understand Namho’s words had never set foot in Nanman.

Because in only half a day, the Fire Dragon Pavilion members and I had learned exactly what a damnable place Nanman was.

Bzzzzzt. Smack!

“Mujin, what was that sound just now?”

“It was nothing. Just a mosquito. My nape suddenly stung, so I wondered what it was.”

“Oh, really? Still, be careful. You never know. Should I call Elder Namho and ask him about it?”

“Come on, Captain. What do you take me for, a child? Hyuk Mujin, a battle-hardened warrior who has fought countless fierce battles at the right hand of the Blazing Flame Divine Dragon! That’s me.”

Exactly one shichen[^1] later, the battle-hardened warrior Hyuk Mujin collapsed while vomiting.

“Bleeaaagh!”

“Gasp, Mujin!”

“What happened?”

“Elder Namho! Mujin has collapsed!”

“Even if I am old, I can clearly see when someone has collapsed. Was he bitten by a mosquito?”

“Cough, yes. About one shichen ago, by one with blue stripes…”

“Blue stripes? And it was one shichen ago? An antidote. Hurry and bring me an antidote!”

Fortunately, getting the battle-hardened warrior back on his feet wasn’t particularly difficult.

I had the Myriad-Poison Ring, a treasured item of the Sichuan Tang Clan, as well as fifty antidotes I had received as Quest rewards.

But that didn’t mean we could let our guard down.

“They normally swarm together in groups of dozens and even hunt predators. If we’d been one shichen later, he wouldn’t be among the living anymore.”

With Namho’s stern warning ringing in our ears, we resumed moving deeper into the secluded land, avoiding the eyes of the non-Han peoples who charged at Han Chinese the moment they saw them.

And that meant we were heading into an even more dangerous place.

“Taishan! Taishan’s stomach hurts too much! It feels like it’s being torn apart!”

“Elder Namho!”

“What did you eat this time?”

“Taishan was hungry, so Taishan picked and ate the red mushrooms growing on a tree.”

“What kind of dog and pig bastard are you? After all the warnings I gave you, you ate blood-feeding fungus that even a tiger couldn’t withstand just because you were hungry? Antidotes won’t work on this!”

Namho personally unleashed a fit of absolute fury, but his anger soon turned into bewilderment.

Taishan had eaten whatever this blood-feeding fungus was—the kind that even a tiger supposedly couldn’t survive—and then gone into the brush to do his business. Afterward, he came back looking perfectly fine.

“Taishan. Feels better after shitting it all out. Taishan is fine now.”

“……Is that thing even human?”

After a moment of thought, Sama Pyo answered in an uncertain voice.

“Probably.”

“Taishan is hungry again now that Taishan’s stomach is empty.”

“I swear by heaven and earth, if you ever eat another mushroom, you’d better be prepared never to feel hunger again.”

“Oh. Taishan. Tempting.”

“……I regret everything. If I had learned martial arts, I would have killed that bastard with a single palm strike by now.”

We continued on our way, leaving the old Hidden Shadow Pavilion agent to lament behind us.

Dense jungle and humid, sweltering heat awaited us at every step, while the eyes of predators lurking throughout the overgrown brush and swamplands glowed a vivid yellow.

*Did we come to Nanman, or did we somehow end up in the Amazon?*

What a goddamn shithole.

What kind of place was this? Tigers were more common than stray cats in a university neighborhood full of studio apartments, and crocodiles teemed like tadpoles in Cheonggyecheon.

Of course, even that was child’s play compared to the strange poisonous flowers and plants that could knock you out from their scent alone, or the bees that flew around with stingers larger than their own bodies.

At least the predators were large enough to be seen.

There was a reason Hyuk Mujin had started groaning only a day or two after leaving Yeongin.

“To hell with the Nanman Beast Palace. I think I’ll be dead by the day after tomorrow.”

Even if it wasn’t by the day after tomorrow, he did look as if his life would be in danger four days from now. He had been poisoned about four times on the first day alone, and over the past two days he had become skin and bones.

Shanxi Province was considered a borderland from the Central Plains’ perspective, but Nanman had gone far beyond anything we had expected.

“Can’t we take another route? It might be a little run-down and rough, but compared to this place, it’d practically be a flower-lined path.”

It wasn’t as if there were no paths in Nanman at all.

Though it was severely underdeveloped compared to the Central Plains, I had heard that the dozens or even hundreds of non-Han peoples who had settled in Nanman each claimed their own territories, and that it wasn’t particularly unusual for them to travel back and forth so long as they didn’t cause disputes.

But despite Hyuk Mujin’s desperate plea, Namho’s answer was firm.

“Impossible. You know the reason, don’t you?”

“If it’s because of the non-Han peoples who are dying to kill us, I’d rather just face them head-on. If we can settle things through conversation, then all the better.”

“Conversation?”

Namho blinked at Hyuk Mujin’s answer, which was full of dreams and hope.

“Are you serious?”

“Of course.”

“An entire village disappeared. More than two hundred people who had welcomed Han Chinese with goodwill were slaughtered, regardless of age or sex. Do you think conversation will work?”

“……No. Actually, I wasn’t serious.”

“You’re finally being honest. Fine, then shut up and keep moving.”

“Yes, sir.”

*Look at Captain Hyuk’s lightning-fast change of attitude.*

But this time, Namho was completely right.

Saying that we would fight the non-Han people who attacked us was the same as declaring war on all of Nanman.

They normally snarled at one another, but one of Nanman’s defining traits was that they would unite as if nothing had happened whenever an external enemy appeared.

*That must be why even the Demonic Cult couldn’t completely conquer Nanman during the Great Faction War.*

The hundred thousand demonic soldiers of the Demonic Cult, who had once swallowed half the world, had only been able to plant their flags around Nanman’s outskirts before withdrawing.

They knew that if they went any deeper into this jungle, with its brutal endemic diseases, treacherous terrain, and countless predators and venomous beasts, the losses would outweigh the gains.

*But it’s not as if we can go around revealing our identities, either.*

It was questionable whether the non-Han peoples, whose hatred of Han Chinese ran so deep, would lower their hostility that easily. But more important was the presence of Dark Heaven, which was surely lurking somewhere in Nanman.

*They’re definitely targeting Nanman. It’s only a matter of time before something happens.*

This was an assumption bordering on certainty. There was a reason we had traveled secretly, like nighttime thieves, all the way from Henan, where the Murim Alliance headquarters was located.

We had been forced to reveal our identities to the bandits of the Water Dragon Stronghold on the way to Nanman, but we had also made certain that they kept their mouths shut.

That was why we hadn’t sent word to the Emei Sect, the Qingcheng Sect, or the Sichuan Tang Clan, despite the ties we had formed during our previous journey to Sichuan.

But if we revealed our identities to the non-Han peoples, all our efforts would be wasted.

Dark Heaven would realize that the unseen dagger was right under its nose and accelerate its plans even further. Then the door to disaster would open along with the rift.

*We can’t reveal our identities until at least after we arrive at the Nanman Beast Palace.*

The Beast Miao King, lord of the Nanman Beast Palace, had participated in the Great Faction War, and I had heard that he held goodwill toward Jeok Cheongang and the Fire Gate Clan.

Considering both the importance of our business and the position he occupied in Nanman, he was far more likely to listen than the other non-Han peoples with their eyes turned red.

*Still, we’re getting shit splattered on us because of those Heavenly Demon Escort Bureau bastards or whatever they are.*

They say the squid is the one that shames the fish market. We had been lumped together with them as part of the same Han Chinese package, and the image of both me and the Fire Dragon Pavilion members had been completely ruined.

I wasn’t even Han Chinese.

*……Is this what they call being a fake Han Chinese?*

It was incredibly unfair, but there was nothing I could do.

Even if I went up to the non-Han peoples of Nanman and pulled some shit like, “Actually, I’m not Han Chinese. I’m Korean. South, not North,” there was no way they’d understand.

Besides, when I had gotten homesick during our training at Mount Jiuhua and drawn the Korean flag, Jeok Cheongang had said only one thing.



*“Wudang?”*

*“No.”*

*“Anyone can see it’s taiji. What kind of bullshit are you spouting? If it’s taiji, it’s Wudang.”*

*“If it’s taiji, it’s Korea.”*

*“What’s Korea?”*

*“That’s… Never mind. You don’t need to know, Old Master.”*

*“An extra two hundred geun of iron balls.”*

*“……Two hundred geun? Why?”*

*“You don’t need to know.”*



Even remembering it brought tears to my eyes.

It felt like only yesterday that I had been suffering in this distant land of another dimension, yet the fact that the suffering was still ongoing was enough to make me despair.

“Whew.”

At the sight of me sighing, Namho glared fiercely.

“What? Do you also want to go down there and settle things through conversation right now? Or would you rather throw down with the non-Han peoples?”

“……Why are you suddenly revving up like that? I have absolutely no desire to do either.”

“That’s a relief.”

There had already been plenty of chances to throw down with someone, and there would be plenty more in the future. Even now, several predators were wandering around us, letting out their cries.

After surveying the densely packed jungle and swamplands, I asked Namho,

“How much farther?”

“Three days if we’re quick. Six days at most.”

“That’s much farther than I expected.”

“Considering that we have to travel while avoiding prying eyes, even that is a short estimate.”

Namho, whose face had aged noticeably, patted his lower back before starting to walk again.

“From now on, don’t slow your pace for even a moment. If we cross Ailao Mountain today, we’ll be able to reach the Nanman Beast Palace in four days at the latest.”

Namho’s words proved true.

Exactly four days later, as we passed over a high mountain peak, we spotted a massive structure in the distance, shrouded in deep clouds and mist.

“The Nanman Beast Palace…”

The voice that slipped from someone’s lips spread on a wind that had blown in from somewhere.

[^1]: A shichen is approximately two hours, while a li is approximately half a kilometer. A geun is a traditional unit of weight roughly equal to 600 grams.
```
