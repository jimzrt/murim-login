<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0447.txt",
      "sha256": "d9e69f495609b2ee0d6f8e8120e6c3f1f8575962ca47aaecf662e339809f7918",
      "bytes": 13208
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1047dfec75fa4827381085d82a3467fd50c608d60ac516974b8ec1aea1578e2b",
      "bytes": 3291
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "779d4d750fb11c49f88f88d272fe4858a0bc4f7a40ac3aa547f1ea27e2471fbe",
      "bytes": 146628
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "52f8fb85a65ffb9ca81820e35f9bb02138765fc5c5d524c9a2bfe815859d624b",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "7dd44fd23d89fe2813b61e721b8353b9827947f224c73e3604ebd7506df74e89",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5e20abc1248071d02fe1aeb79596a8ccdf288b4627ced862f40d58327963828a",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c7854bef8776722db43782fdc80b492e6d9dc71f462a80789e1f7ca825d653c5",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "eb4d0509443a3dd9764bf15b6a4d1169bd0b1c1718eaf09ed06cc94a96527dc9",
      "bytes": 1239
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "61e6b36a83287cd9a73d09607bacaafc158e87f61336b7b9f7957dd6c543f3ca",
      "bytes": 870
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "8c293a634141f85c54984c1fe9c3b23797c10b57f369c969eb3e165e4d56b4ba",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "b72c8683ed7e90056f6e3934988ba042c4db97c4f7be69de9ac7425cc0f08d80",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "db999f65266be742033205ed7626a180cb20a03f2d8eb041eede4d8d3226e171",
      "bytes": 141528
    }
  ],
  "estimated_tokens": 12553
}
-->

# Durable State Update — Chapter 447

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 447. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 447. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 447,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 447,
    "continuity_sources": [447],
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
    "Taekyung accepted the Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance, and Taekyung is cooperating with his investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained and may relate to black magic.",
    "The Sea Serpent Society was destroyed at Red Cliffs, the Dongting Fisherman disappeared after condemning the Yangtze River Channel League, and the League is implicated only by circumstantial evidence.",
    "Dangyang Stronghold and Honghu Stronghold vanished after taking control of Sea Serpent Society territory, while Donghu Stronghold remains inaccessible beyond Tianling Falls.",
    "Hwang Chung, the Yangtze One Saber, is the Seafaring King's sworn brother, a moderate-faction elder, and Lord of Donghu Stronghold; his involvement remains unproven.",
    "The Dongting Fisherman's broken Black Bamboo Fishing Rod was found, and Zhuge Feng ordered Mu Song to guide the group to Donghu Stronghold.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group remains within the Zhuge Clan's Inner Hall in Hubei after traveling with Mu Song's Water Dragon Stronghold fleet."
  ],
  "continuity_sources": [
    446,
    445
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Who destroyed the Sea Serpent Society, caused the disappearances of the Yangtze River Channel League strongholds and Dongting Fisherman, and what happened inside Donghu Stronghold?"
  ],
  "safe_through": 446,
  "temporary_decisions": [
    "Render 황충 as Hwang Chung, 장강일도 as Yangtze One Saber, 천령폭 as Tianling Falls, and 흑죽조간 as Black Bamboo Fishing Rod.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 큰형     | **eldest brother**                           |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 유비 | **Liu Bei** | Historical ruler in the Three Visits to the Thatched Cottage allusion. |
| 강풍 | **Kang Pung** | False name Cheongpung uses while disguised as the Invincible Divine Sword. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 달마대사 | **Bodhidharma** | Famous Shaolin figure cited alongside Lü Dongbin and Jang Samfeng. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 445
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 446
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 444
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 446
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 446
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 446
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, is the League elder and Donghu Stronghold Lord whom Mu Song firmly believes is innocent.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 446
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 446
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃447화



촤아아아.

빠르게 물살을 가르며 나아가는 쾌조선에는 침묵만이 감돌았다.

수룡채의 수적들은 입을 꾹 다문 채 기계처럼 노를 저었고, 무송은 딱딱하게 굳은 얼굴로 전방을 주시할 뿐이었다.

‘분위기 한번 끝내주네.’

나는 내심 혀를 차며 주위를 둘러보았다.

현재 동정채로 향하는 쾌조선은 총 네 척.

하지만 선상의 분위기는 호북으로 향하던 때와는 천양지차다.

전에는 찾아볼 수 없었던 새로운 얼굴들이 바로 그 원인이었다.

‘제갈세가. 그리고 무당파.’

호북성을 양분하는 두 명문 대파의 제자들이 네 척의 쾌조선을 가득 채웠다.

혹시 모를 유혈 사태를 대비하여 가려 뽑은 정예라는 걸 한눈에 알 수 있을 만큼, 한 사람 한 사람이 뛰어난 무인들이다.

그리고 그들의 중심에는 두 사람이 있었다.

“오늘따라 유독 바람이 강한 것 같구려, 제갈가주.”

노도사의 말에 제갈풍이 태평한 목소리로 대답했다.

“염려하지 않으셔도 됩니다. 오늘 같은 바람이 분다면 오히려 일이 더욱 수월해질 테니까요.”

“어째서 그렇소? 이보다 약한 바람에도 이미 수십 척의 배가 수몰한 것으로 알고 있소만.”

“수부들의 실력도 실력이지만, 장강수로맹의 상징이라 할 수 있는 쾌조선은 여타의 배와는 질적으로 다릅니다. 강풍에 휩쓸리기보다 힘을 받고 더욱 힘차게 나아갈 수 있지요.”

“빈도 역시 쾌조선에 관한 풍월을 들은 적이 있긴 하오만…… 견문이 좁은 탓에 자세히는 모르겠구려. 일평생 무림에 몸담은 것이 허송세월처럼 느껴질 정도요.”

“진인께서는 무당파 본산에만 머무르셨으니 모르실 만도 하지요. 그런데…… 지난번 말씀하셨던 그 일은 어떻게 되었는지 여쭤봐도 되겠습니까?”

“장문인께서 직접 본 산의 제자들과 함께 힘쓰고 계시는 중이오. 그 대신 빈둥거리며 양곡만 축내는 빈도를 이리 보내신 것이고.”

“양곡만 축내다니요. 이 후배는 현공진인(玄空眞人)께서 오시니 천군만마를 얻은 듯합니다.”

제갈풍의 말은 예의상 하는 것이 아니었다. 사실이 그랬다.

현공진인.

그것이 누덕누덕 기운 도복과 낡은 송문고검(松紋古劍) 한 자루를 허리춤에 찬 노도사의 도호였다.

그리고 그가 무당파 내에서 차지하는 위치나 무림의 배분은 결코 제갈풍에 뒤떨어지지 않았다.

아니, 오히려 어깨를 나란히 하거나 그 이상이라고도 할 수 있었다.

아직 환갑도 되지 않은 제갈풍과 달리, 현공진인은 정마대전 당시에도 혁혁한 전공을 올린 전대의 고수이자 현 무당파 장문인의 사제니까.

‘게다가 무당파가 자랑하는 초절정 고수이기도 하고.’

무당파 최고의 절기, 태극혜검(太極慧劍)의 극의에 다다랐다고 알려진 검객이 바로 현공진인이었다.

제갈세가의 가주인 제갈풍이 다른 이들 앞에서도 말을 높이는 것 역시 그에 대한 존중의 표시였다.

아, 물론 한 사람은 이 모든 것에서 예외다.

“많이 컸네, 저놈.”

무림의 달마대사 고인물, 적천강의 말에 어이가 없어진 내가 중얼거렸다.

“그러게요. 얼마나 많이 컸는지 수염이 허옇네.”

“마지막으로 봤을 때 저놈 나이가 이립이었던가. 허, 참. 시간 한번 빠르다. 솜털 보송보송하던 어린 녀석들이 죄다 일파의 장문인이고 장로라니.”

“……솜털 보송보송이요? 이립이면 고추 털 수북 아닙니까?”

적천강이 쌍심지 켠 눈으로 나를 바라보았다.

“계속 말꼬리를 잡는 걸 보아하니, 아래 털이 죄다 뽑히고 싶은 모양이로구나.”

“아니, 무슨 그런 말씀을 하세요.”

쾌조선 갑판 위에서 화왕질리언 왁싱을 당할 마음은 눈곱만큼도 없다.

빛의 속도로 손을 내저은 내가 슬쩍 적천강을 곁눈질하며 물었다.

“이렇게 된 김에 여쭤보는 건데, 춘추가 정확히 얼마나 되시는 겁니까?”

“춘추?”

평소에도 늙었다는 소리를 죽여 달라는 것과 동의어로 받아들이는 적천강이다. 나는 떨떠름하게 단어를 고쳤다.

“……그럼, 연세?”

“연세?”

아니, 백 세가 넘었으면서 도대체 여기서 뭘 더 원하는 거야.

나는 어이없음을 한껏 담아 물었다.

“천강이, 몇 살?”

빡!

그래, 이럴 줄 알았다.

번개처럼 내 뒤통수를 후려친 적천강이 심드렁한 어조로 대답했다.

“일백을 넘긴 후로 안 세 봤다.”

“그러니까 마지막으로 나이를 셌던 게 몇 년 전인데요?”

“오천 년 전. 됐느냐?”

근처 뱃머리에 대롱대롱 매달려 있던 청풍이 입을 딱 벌렸다.

“와아, 오천 살!”

“……저놈은 의심이란 걸 할 줄 모르냐?”

“……원래 그런 놈입니다. 그나저나 상상을 초월할 정도로 동안이셨네요.”

적천강이 나를 지그시 노려보았다.

“더 자세히 알고 싶으냐?”

“당연히, 아니죠.”

솔직히 알고 싶긴 한데, 표정을 보니 알아서는 안 될 것 같다.

평소 나이에 민감한 건 둘째 치고, 어느 때보다 거친 물살과 바람을 타고 빠르게 나아가는 쾌조선에 타고 있다는 현실이 그에게 엄청난 스트레스로 다가온 모양이었다.

“도대체 이 염병할 나무 쪼가리는 언제쯤 멈추는 게냐?”

바로 그때.

적천강의 투덜거림을 듣기라도 한 것처럼 염병할 나무 쪼가리가 더욱 속력을 높였다.

콰아아아!

물줄기가 높이 솟구치며 안정적이던 선체가 좌우로 흔들렸다.

갑작스러운 거친 움직임에 청풍이 어린이날 놀이공원에 온 아이처럼 환호를 질렀다.

아직까지도 장강 찍먹 사건의 후유증을 벗어나지 못한 혁무진과 궁기방은 찢어지는 비명을 내질렀고, 평온하게 홀로 중심을 잡고 있던 문경은 사람들의 시선을 의식하여 눈치껏 난간을 붙잡았다.

그리고 적천강은…….

“으허, 으허어어어어!”

화왕(火王)이라는 별호가 무색할 만한 소리를 내며 혼비백산하는 중이다.

세상에, 눈 부릅뜬 거 봐. 강남 성형외과 쌍꺼풀 수술 성공 사례로 지하철 전면 광고 실어도 되겠다.

나는 얼굴로 쏟아지는 물을 피하며 무송을 향해 외쳤다.

“선배! 속도를 좀 늦춰 주…….”

“그건 곤란할 것 같군.”

무송이 내 말을 칼같이 잘라 냈다.

장강에서 나고 자란 사람답게, 마치 평지에서처럼 우뚝 서 있는 그가 손을 들어 전방을 가리켰다.

“보이나?”

보이냐니. 뭘 말하는 거지?

눈을 가늘게 뜬 나는 그의 손가락이 향하는 곳을 응시했다.

공력을 끌어 올려 눈에 집중하자, 비약적으로 상승한 안력(眼力)이 출렁이는 강물에 자욱하게 깔린 안개 너머를 꿰뚫어 본다.

‘저건…….’

보인다.

선박 중에서도 가장 날렵한 축에 들어가는 쾌조선조차 겨우 두 척이 간신히 지나갈 법한 좁은 폭.

그리고 그 앞에서 칼날처럼 회오리치는 거센 와류(渦流)가.

콰아아아, 콰득!

어디서 떠내려온 것인지, 반경만 백여 장에 달하는 와류에 휘말린 커다란 통나무 하나가 수압을 이기지 못하고 부서진다.

그렇게 튕겨 나간 통나무의 파편 일부는, 수문장처럼 와류 뒤에 우뚝 선 거대한 바위와 부딪쳐 산산이 조각났다.

‘바다도 아니고 강에 저런 소용돌이라니.’

신비로우면서도, 한편으로는 등골이 서늘해지는 광경.

그리고 지금 쾌조선에 탄 이 자리의 모든 사람은 저 엄청난 와류의 정체를 알고 있었다.

“천령폭(天靈瀑)!”

누군가가 비명처럼 외친 한마디.

맞다. 저것이 바로 천령폭이다.

장강수로맹의 동정채를 천혜의 요새로 만들어 준 자연의 산물이자, 오랜 세월 동안 숱한 목숨과 선박을 집어삼킨 괴물.

적천강이 당장이라도 질식할 것 같은 얼굴로 선언했다.

“배 돌려. 저걸 건널 바에야 정마대전을 한 번 더 치르겠다.”

이어 궁기방과 혁무진이 이미 질식한 것 같은 얼굴로 말했다.

“무송 선배. 제발 살려 주십시오. 차라리 거지 소굴에서 구걸을 하겠습니다.”

“조장님. 그동안 감사했습니다. 저 이제 무림인 그만할게요. 고향 내려가서 비단 팔고 싶어요.”

“……비단보다 네 영혼이 먼저 팔린 것 같은데.”

이렇게 말하는 나도 겁이 나지 않는 것은 아니다.

빠르게 가까워지는 거대한 와류를 보고 있자니, 나 스스로가 개미지옥에 빠진 한 마리 개미가 된 기분이었다.

‘시벌, 우선 바위에 맞아서 개박살이 난 다음에 화장실 변기 물 내리는 것처럼 쏙 빨려 들어갈 것 같은데.’

대자연이 주는 공포 앞에서는 시스템도, 초절정의 무공도 별 소용없는 것처럼 느껴졌다.

만일 누군가 나를 장강 한가운데에 빠트린다면 어떻게든 헤엄쳐 나올 자신이 있지만, 저런 엄청난 소용돌이에 휩쓸린다면…… 그때는 정말이지 끝장이다.

“후우, 후.”

심호흡하는 내 어깨 위에 두꺼운 손 하나가 올라왔다.

“막내야.”

제법 장신인 나조차도 고개를 들어 올려다봐야 하는 거한, 진위경이 담담한 표정으로 입을 열었다.

“아무것도 걱정하지 말거라.”

형님 소리가 절로 나올 수밖에 없는 침착성이다.

물을 병적으로 싫어하는 적천강은 둘째 치고 초절정의 경지에 오른 나조차도 간담이 서늘해질 정도인데, 무공으로는 한참 아랫줄인 진위경은 한 치의 흔들림도 없었다. 이래서 큰형이고, 소가주인 거구나.

“큰형님…….”

“그래.”

진위경이 희미하게 웃으며 고개를 끄덕였다.

“귀신이 되어서도 우리 형제의 우애는 영원할 것이다.”

“예?”

“돌아가신 부모님이 눈앞에 어른거리는구나. 천령폭에서 우리를 향해 손짓하고 계시는 듯해.”

“……아버지는 아직 살아 계시지 않아요?”

“다시 소식이 끊긴 지 오래됐다. 그냥 죽은 셈 치자꾸나.”

큰형님은 얼어 죽을. 그냥 큰 새끼다.

그 와중에 가문 짬 때리고 도망쳤다고 멀쩡히 살아 있는 아버지까지 죽여 버리는 클라스.

‘시펄…….’

주위를 둘러보니 이미 대부분 반쯤 정신이 나간 상태로 대자연이 주는 비트에 몸을 맡기는 중이다.

나는 마지막 희망을 담아 무송을 바라보았다.

“저기, 무송 선배.”

“미안하지만, 멈추기에는 늦었네.”

콰아아아아! 콰드득!

“어, 시발 진짜네.”

무송이 굳은 얼굴로 고개를 끄덕였다.

“꽉 잡게. 나와 수하들 역시 최선을 다할 테니.”

“예? 애쓰다니, 무슨 말이에요 그게.”

“천령폭이 성마다 하나씩 있는 흔한 것인 줄 아나? 나 역시 황 숙부를 뵙기 위해 호북에 왔을 당시 서너 번 지나갔던 것이 전부야. 본 맹의 쾌조선과 지금껏 갈고닦은 솜씨를 믿는 수밖에.”

“자, 잠깐, 그러니까…… 천령폭 뉴비라 이겁니까?”

“갑자기 왜 유비가 나오는지는 모르겠지만, 나야 애당초 총단을 떠나 채주가 된 이후로는 사천에만 있었으니 익숙하지 않을 수밖에 없지 않겠나.”

맞는 말이다. 존나 처맞는 말.

넋이 반쯤 나가 있던 나는 간신히 목소리를 쥐어짜 냈다.

“아니 미친. 그런 중요한 얘기를 왜 이제야 해요?”

“제갈 대협이 다른 사람에게는 말하지 말라고 했으니까.”

뭐?

전광석화 같은 속도로 고개를 돌리자, 긴장으로 잔뜩 몸이 굳어 있는 양 문파의 제자들과 그 중심에 있는 한 사람이 눈에 들어온다.

나와 시선이 마주친 제갈풍이 솟구치는 물보라를 맞으며 껄껄 웃었다.

“지자(智者)는 아군을 이끌고, 모사(謀士)는 아군마저 속이는 법. 다 함께 호랑이 등에 올라탔으니 어디 한번 끝장을 보세!”

“……!”

“……!”

이거 실화냐.

나를 비롯한 모두는 할 말을 잃었고, 적천강은 이성을 잃었다.

“저 개쌍노무 새끼가……!”

지금까지 봐 왔던 것 중에서도 첫손가락에 꼽히는 역대급 극대노.

하지만 눈을 허옇게 까뒤집은 적천강이 달려들려던 바로 그 순간.

“모두 꽉 붙잡아!”

무송의 다급한 외침과 함께, 아가리를 쩍 벌린 천령폭의 와류가 쾌조선을 후려쳤다.

콰아아아아아앙!
```

## Final English reading copy

```markdown
# Chapter 447

Whoosh.

Silence hung over the fast ship as it cut rapidly through the current.

The river bandits of Water Dragon Stronghold rowed like machines with their mouths pressed tightly shut, while Mu Song did nothing but stare ahead with a stiff, frozen expression.

*What a wonderful atmosphere.*

I clicked my tongue inwardly and looked around.

There were four fast ships heading toward Donghu Stronghold.

But the atmosphere aboard them was worlds apart from when we had been heading toward Hubei.

The reason was the unfamiliar faces that had not been there before.

*The Zhuge Clan. And Wudang.*

Disciples from the two prestigious great factions that divided Hubei Province filled the four fast ships.

It was obvious at a glance that they were elites carefully selected in preparation for any unforeseen bloodshed. Every one of them was an outstanding martial artist.

And at the center of them stood two people.

“The wind seems unusually strong today, Family Head Zhuge.”

At the old Daoist’s words, Zhuge Feng answered in an untroubled voice.

“You need not worry. If the wind is blowing like this, things will actually be easier for us.”

“Why is that? I understand that dozens of ships have already sunk in winds weaker than this.”

“The boatmen’s skill is one thing, but the fast ships that serve as the symbol of the Yangtze River Channel League are qualitatively different from ordinary vessels. Rather than being swept away by strong winds, they can catch the force and move forward with even greater vigor.”

“I have heard some talk about fast ships as well… but I do not know the details, as my experience is limited. I have spent my entire life in Murim, yet it feels as though I have wasted it.”

“Since you have remained at Wudang’s headquarters all this time, it is understandable that you would not know. But… may I ask what became of the matter you mentioned last time?”

“Our Sect Leader is personally working on it together with the disciples of our main sect. As for me, I was sent here instead, since all I was doing was sitting around and consuming the sect’s grain.”

“Consuming grain? With Perfected Being Hyeongong joining us, this junior feels as though he has gained a thousand troops and ten thousand horses.”

Zhuge Feng’s words were not mere courtesy. They were true.

Perfected Being Hyeongong.

That was the Daoist title of the old man wearing a patched Daoist robe and carrying a single Pine-Pattern Ancient Sword at his waist.

His position within Wudang and his generational seniority in Murim were in no way inferior to Zhuge Feng’s.

No, one could even say that he stood shoulder to shoulder with Zhuge Feng—or above him.

Unlike Zhuge Feng, who had not yet reached sixty, Perfected Being Hyeongong was a master of the previous generation who had distinguished himself during the Great Faction War. He was also the current Wudang Sect Leader’s Junior Brother.

*On top of that, he’s one of Wudang’s famed Supreme Peak masters.*

Perfected Being Hyeongong was the swordsman said to have reached the ultimate stage of Wudang’s greatest technique, the Taiji Wisdom Sword.

The fact that Zhuge Feng, Family Head of the Zhuge Clan, spoke so respectfully even in front of others was itself a sign of his respect for Hyeongong.

Ah, of course, there was one exception to all of this.

“That guy’s grown a lot.”

At the words of Jeok Cheongang—Murim’s own Bodhidharma and the ultimate old-timer—I muttered in disbelief.

“Sure has. He’s grown so much that his beard has turned white.”

“How old was that fellow the last time I saw him? Thirty?”

“……”

“Ha. Time really flies. Those young pups with soft fuzz on their faces are all Sect Leaders and Elders now.”

“Soft fuzz? If he was thirty, wouldn’t he have had a full bush down there?”

Jeok Cheongang glared at me with blazing eyes.

“Judging by the way you keep nitpicking my words, it seems you want every hair below your waist plucked out.”

“No, why would you say something like that?”

I had not the slightest desire to undergo Fire King Zilean waxing on the deck of a fast ship.

I waved my hands at lightning speed, then glanced sidelong at Jeok Cheongang.

“Since we’re on the subject, may I ask your venerable age?”

“My venerable age?”

Even under ordinary circumstances, Jeok Cheongang treated being called old as synonymous with asking him to kill you. I awkwardly tried another term.

“…Then, how many years have you lived, sir?”

“How many years?”

No, seriously. He was over a hundred years old. What more did he want from me?

I asked, thoroughly exasperated.

“Cheongang, how old are you?”

Whack!

Right. I knew this would happen.

After striking the back of my head like a bolt of lightning, Jeok Cheongang answered in a bored tone.

“I stopped counting after I passed one hundred.”

“So when was the last time you counted?”

“Five thousand years ago. Satisfied?”

Cheongpung, who had been dangling from the nearby bow, opened his mouth wide.

“Wow, five thousand years old!”

“…Does that fellow not know what suspicion is?”

“…He’s always been like that. Anyway, you look incredibly young for your age.”

Jeok Cheongang stared at me.

“Do you want to know more?”

“Of course not.”

I honestly did want to know, but judging by his expression, I probably shouldn’t.

He was sensitive about his age under ordinary circumstances. On top of that, the reality of riding a fast ship that was racing forward over rougher waves and stronger winds than ever before seemed to be placing an enormous amount of stress on him.

“When the hell is this goddamned piece of wood going to stop?”

Right then.

As if it had heard Jeok Cheongang’s complaint, the goddamned piece of wood picked up even more speed.

Whoooosh!

A column of water surged high into the air, and the previously stable hull rocked from side to side.

At the sudden rough movement, Cheongpung let out a cheer like a child visiting an amusement park on Children’s Day.

Hyuk Mujin and Gung Gibang, who still had not recovered from the aftereffects of the Yangtze taste-test incident, released ear-splitting screams. Mungyeong, who had been calmly keeping his balance by himself, tactfully grabbed the railing after noticing everyone’s eyes on him.

And Jeok Cheongang…

“Uhh! Uhhhhh!”

He was panicking, making a noise so undignified that it rendered the title Fire King meaningless.

Good heavens, look at those bulging eyes. He could be used in a Gangnam plastic surgeon’s subway advertisement as a successful double-eyelid surgery case.

I dodged the water splashing into my face and shouted toward Mu Song.

“Senior! Could you slow down a little—”

“That will be difficult.”

Mu Song cut me off with a voice as sharp as a blade.

Like a man born and raised on the Yangtze, he stood perfectly upright as if he were on level ground. He raised one hand and pointed ahead.

“Can you see it?”

See what?

I narrowed my eyes and stared in the direction of his finger.

I drew up my internal energy and concentrated it in my eyes. My eyesight, enhanced by leaps and bounds, pierced through the thick fog covering the rippling river.

*That’s…*

I could see it.

A narrow passage barely wide enough for two fast ships—the most streamlined kind of vessel—to pass through.

And directly in front of it, a violent whirlpool twisting like a blade.

Whoooosh! Crack!

A massive log, swept in from who knew where and caught in the whirlpool, which measured more than a hundred zhang in radius, broke apart after failing to withstand the pressure of the water.

Some of the splintered pieces were flung away and smashed into a huge rock standing behind the whirlpool like a gatekeeper, shattering into fragments.

*A whirlpool like that in a river, not the sea?*

It was a mysterious sight, but one that sent a chill down my spine.

And every single person aboard the fast ships knew the identity of that terrifying whirlpool.

“Tianling Falls!”

Someone shouted the words like a scream.

That was right. This was Tianling Falls.

A work of nature that had transformed Donghu Stronghold of the Yangtze River Channel League into a natural fortress—and a monster that had swallowed countless lives and ships over the centuries.

Jeok Cheongang declared with a face that looked as though he might suffocate at any moment.

“Turn the ship around. I would rather fight the Great Faction War one more time than cross that.”

Gung Gibang and Hyuk Mujin spoke next, their faces already looking as if they had suffocated.

“Senior Mu Song. Please save us. I would rather beg in a beggars’ den.”

“Captain. Thank you for everything. I’m quitting Murim now. I want to go home and sell silk.”

“…It looks like your soul will be sold before the silk.”

I was afraid, too.

As I watched the enormous whirlpool rushing closer, I felt as though I had become an ant trapped in an antlion’s pit.

*Fuck. First we’ll get smashed to bits against that rock, then we’ll be sucked in like a toilet flushing.*

In the face of the terror offered by Mother Nature, even the System and Supreme Peak martial arts felt utterly useless.

If someone dropped me in the middle of the Yangtze, I was confident I could somehow swim to shore. But if I were swept into a monstrous whirlpool like that…

That would truly be the end.

“Whew. Whew.”

A thick hand settled on my shoulder as I took deep breaths.

“My youngest.”

Even I, who was fairly tall, had to lift my head to look up at the giant. Jin Wikyung opened his mouth with a calm expression.

“Do not worry about a thing.”

His composure was enough to make me call him Big Brother without thinking.

Putting aside Jeok Cheongang, who had a pathological hatred of water, even I had reached the Supreme Peak realm and was still feeling my blood run cold. Yet Jin Wikyung, whose martial arts were far below ours, did not waver in the slightest.

*So this is why he’s the eldest brother and the Lesser Family Head.*

“Big Brother…”

“Yes.”

Jin Wikyung smiled faintly and nodded.

“Even in death, the bond between our brothers will last forever.”

“What?”

“I can see our deceased parents hovering before my eyes. It is as though they are beckoning to us from Tianling Falls.”

“…Isn’t Father still alive?”

“We lost contact with him again a long time ago. Let us consider him dead.”

*Big brother, my ass. He’s just a big bastard.*

And while he was at it, he had declared our perfectly alive father dead just because the man had dumped the family responsibilities on him and run away.

*Shit…*

I looked around. Most of the people were already half out of their minds, letting their bodies move to the beat of Mother Nature.

I looked at Mu Song with the last of my hope.

“Senior Mu Song.”

“I’m sorry, but it’s too late to stop.”

Whoooosh! Crack!

“Oh, fuck. He’s right.”

Mu Song nodded with a hardened expression.

“Hold on tight. My men and I will do our best as well.”

“What? What do you mean, do your best?”

“Do you think Tianling Falls is some common feature that can be found in every province? I have only crossed it three or four times, when I came to Hubei to see Uncle Hwang. We have no choice but to trust the League’s fast ships and the skills we have honed over the years.”

“W-wait. So you’re saying… you’re a Tianling Falls newbie?”

“I do not know why Liu Bei suddenly came up, but naturally I would be unfamiliar with it. I spent all my time in Sichuan after leaving headquarters and becoming Stronghold Lord.”

He had a point.

A fucking punchable one.

Half out of my mind, I barely squeezed out my voice.

“You’ve got to be kidding me. Why are you only telling us something this important now?”

“Great Hero Zhuge told me not to tell anyone else.”

What?

I turned my head at lightning speed and saw the disciples of both sects, their bodies rigid with tension, and the man standing at their center.

Zhuge Feng met my gaze and laughed heartily as he was pelted by the rising spray.

“A wise man leads his allies, while a strategist deceives even his allies. Since we have all climbed onto the tiger’s back, let us see this through to the bitter end!”

“……!”

“……!”

Was this for real?

Everyone, myself included, was left speechless, while Jeok Cheongang lost his reason.

“That fucking son of a bitch…!”

It was one of the greatest fits of rage I had ever witnessed.

But just as Jeok Cheongang rolled his eyes back until only the whites showed and prepared to charge—

“Everyone, hold on tight!”

With Mu Song’s urgent shout, the whirlpool of Tianling Falls opened its maw wide and slammed into the fast ship.

KRA-KOOOOM!
```
