<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0451.txt",
      "sha256": "404e42889bb6a2baa2fe50ae6a2b974bd85a2e645006d46597e108b9f98da4cf",
      "bytes": 13395
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9265992e04fd610ad84bf28ed0fa9091bb6497b5f51a197293c30bc30ed356b4",
      "bytes": 3007
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "dd9d246d44c5b87b3b0125610bfab2057c49bfd06e77d81f018a802f339502c0",
      "bytes": 147828
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ff6e575c3996e6c0416d4a133179301efa555316bdc6b4a76b40ec6fa7371f03",
      "bytes": 944
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "21aa9f40418584d336d005d2c23c7ca8669807ee0c4c0975216d15de2fdb144d",
      "bytes": 472
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "585122bfb318845dd2f2b16310428ef5efdb54602320b281c9f7d29791f4e082",
      "bytes": 609
    },
    {
      "path": "characters/Hwang Chung.md",
      "sha256": "57d5aab200a54a70aad6f54792b10e7b6ffc5ce58c37a58d2c0b556f78770af0",
      "bytes": 663
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "23152da6c5bd7cbcc8563d9f7cf4f19b193e9a8b02f7e8c64abd756470bf694c",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fcb5723f38876693bfec7fa690093d937caf209f9f6d539956fa18fe02834ce1",
      "bytes": 1470
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "feeb56834aa9a7585626ab3542da88226e0749030c9fd182024dfb28e409937d",
      "bytes": 686
    },
    {
      "path": "characters/Qilian Three Fiends.md",
      "sha256": "4d8f6258af666524e77227dd347b46252a22fff723291f34d79f16ac17bd53d3",
      "bytes": 637
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "10157bc6a1e683007d10e21ee07bc3a528b01fdb76aba81cd2ab7584f00d3ed4",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e461e36fdfca1b36145d5e3c2c1ab27e0d867d36d7f0c4d6478c5994b61b21fa",
      "bytes": 142508
    }
  ],
  "estimated_tokens": 11931
}
-->

# Durable State Update — Chapter 451

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 451. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 451. Profile updates may replace only one
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
  "chapter": 451,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 451,
    "continuity_sources": [451],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society was destroyed, the Dongting Fisherman disappeared, and the Yangtze River Channel League's Hubei strongholds have now also been devastated.",
    "Hwang Chung, Hwang Cheol, and Do Ripgun were found dead at Donghu Stronghold, with no survivors or witnesses.",
    "The suspected Moving Formation was not found at Donghu Stronghold despite a search by Zhuge Clan personnel.",
    "Taekyung's party is preparing to travel to the Zhuge Clan for formation and mechanism specialists.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including the massacre of twenty pilgrims on Mount Wudang.",
    "Jin Wikyung and Jeok Cheongang remain at Donghu Stronghold, while Mungyeong has chosen to stay behind as well.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder."
  ],
  "continuity_sources": [
    450,
    449
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "Why does Mungyeong continue to remain with Taekyung's group despite concealing his reasons?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 450,
  "temporary_decisions": [
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon and 일급 낭인 as First Rate wandering martial artist.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged; render 현공진인 as “Perfected Being Hyeongong” and 화왕질리언 as “Fire King Zilean.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 은인     | **Benefactor**                               |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 황충 | **Hwang Chung** | Lord of Donghu Stronghold, the Seafaring King's sworn brother, and the Yangtze One Saber. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 기련삼괴 | **Qilian Three Fiends** | Three identical brothers from the Qilian Mountains. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 내가고수 | **I'm a Master** | System Title granted to Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 광수도귀 | **Mad Water Saber Demon** | Epithet of Hwang Cheol. |
| 파랑호 | **Wave Fox** | Epithet of Do Ripgun. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 450
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 449
- **Aliases:** None
- **Role:** The Dongting Fisherman is a public critic of the Yangtze River Channel League who disappeared after condemning it.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League; his current whereabouts are unknown.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 450
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hwang Chung.md

# Hwang Chung (황충)

- **Safe through:** Chapter 450
- **Aliases:** Yangtze One Saber
- **Role:** Hwang Chung was the Lord of Donghu Stronghold, a moderate-faction elder of the Yangtze River Channel League, and the Seafaring King's sworn brother before he was killed in the stronghold's destruction.
- **Personality:** Calm, clever, and supportive of the orthodox faction during the Great Faction War.
- **Voice:** Not established.
- **Relationships:** Hwang Chung helped the Seafaring King establish the Yangtze River Channel League and is regarded by Mu Song as an uncle and trusted senior.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 450
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 450
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 450
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Qilian Three Fiends.md

# Qilian Three Fiends (기련삼괴)

- **Safe through:** Chapter 370
- **Aliases:** Three Fiends
- **Role:** First Fiend and at least one other brother are dead, the Third Fiend has been captured by Mungyeong, and the Second Fiend's fate remains unknown.
- **Personality:** Bloodthirsty and notorious throughout Qinghai, but fearful and submissive before the Western Heaven Demon Lord.
- **Voice:** The brothers speak in near-unison with frightened, deferential phrasing.
- **Relationships:** They serve the Western Heaven Demon Lord and address him as their superior.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 450
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃451화



“은인, 어디 가세요?”

“으, 응?”

문밖으로 슬그머니 걸음을 옮기던 나는 움찔했다. 주섬주섬 짐을 챙긴 청풍이 고개를 갸웃거리며 나를 바라보고 있었다.

“뭐가, 왜.”

“어디 가시는 거 아니에요?”

“그, 잠깐 급한 볼일이 생겨서.”

“빨리 출발해야 한다고 하셨잖아요?”

“이봐, 청 소협. 내가 굳이 이런 말까지는 안 하려고 했는데…….”

나는 짐짓 얼굴을 굳히며 입을 열었다.

“소피보러 가는 거야. 됐지?”

“하지만 측간은 그 방향이 아닌데요.”

“…….”

쓸데없이 예리하네.

부전공은 무공이고, 전공이 먹고 싸는 일이라 그런지 섬 안의 측간은 죄다 알고 있는 것이 틀림없다.

잠시 머뭇거리던 내가 대답했다.

“……노상 방뇨야.”

내가 생각하기에도 궁색한 변명이다.

그제야 이상함을 느낀 궁기방과 혁무진도 행낭을 꾸리다 말고 이쪽으로 고개를 틀었다.

“궁 소협. 조장님께서 오늘따라 혓바닥이 좀 기신 것 같지 않아요?”

“그러게. 왜 저렇게 안절부절못하는 것 같지?”

“그건 너희 둘 중에 누구부터 때릴까 고민돼서 그래.”

평소 같았다면 이 말을 던진 시점에서 꼬리를 내려야 하는데, 이미 내 폭력에 길들여진 두 놈은 제법 성장해 있었다.

“흠. 평소의 조장님이었다면 이미 말보다 손이 먼저 나왔을 겁니다. 그런데 말로 얼버무린다? 확실히 뭔가 있어요.”

“그렇지?”

“확실합니다. 제가 그동안 한두 번 맞아 본 줄 아세요? 이게 다 개연성과 흐름이 있어요.”

혁무진이 게슴츠레한 눈빛으로 나를 바라보던 그때, 눈을 번쩍 뜬 궁기방이 주위를 훑었다.

“잠깐, 그런데 문경이는 어디 갔어?”

“어, 그러게요. 조금 전까지만 해도 같이 있었는데, 이 녀석 도대체 어딜 간 거지?”

어딜 가긴. 이미 밖으로 나가서 날 기다리고 있지.



‘얘기 좀 하지.’



나는 조금 전 문경이 흘리고 간 전음을 떠올리며 한숨을 내쉬었다.

여기서 더 부정했다가는 괜한 의심만 더 받게 생겼다.

“밖에 있어. 나랑 따로 나눌 이야기가 있어서.”

“측간에서요? 그것도 단둘이?”

“……뭔 개소리야, 미친놈아. 그렇게 말하니까 의미심장하게 들리잖아.”

혁무진이 의뭉스러운 표정으로 나를 바라보며 말했다.

“조장님. 전 이미 욕과 폭력에 길들어진 놈이라 괜찮습니다. 하지만 문경이한테는 이상한 물 들게 하지 마십쇼.”

“…….”

미친놈이 뭐라는 거야. 당장 내가 피로 물들게 생겼구만.

하도 어이가 없어서 말도 제대로 못 하는 내게, 궁기방이 한마디를 보탰다.

“혁가놈 말이 맞다. 애가 볼수록 참 생각이 깊고 착하던데, 괜한 트집 잡아서 괴롭히지 말아라.”

“와, 이 새끼들 진짜…… 아니다. 됐다. 너희가 뭘 알겠냐.”

그나마 이제야 상황을 눈치챈 청풍은 꿀 먹은 벙어리처럼 입을 다물고…… 아니, 지금 보니까 진짜 당과 처먹고 있네.

‘저놈의 당과는 도대체 어디서 계속 튀어나오는 거야.’

더 있다가는 정신병 걸리겠다.

고개를 절레절레 흔든 나는 뒤에서 들려오는 목소리를 무시하고 가옥을 나섰다.

밖으로 나오자, 새하얀 백의를 걸친 문경이 마당에서 나를 기다리고 있었다.

“늦으셨군요.”

“그래도 얼마 안 걸렸…….”

“늦으셨군요.”

“미안하…….”

“늦으셨군요.”

“…….”

제발 살려 줘.

반복재생의 압박이 장난 아니다. 누구도 눈치 못 챌 만큼 은밀하게 쏘아지는 기세에 나는 마른침을 꿀꺽 삼켰다.

“느, 늦어서 미안하다. 그런데 무슨 일이야?”

“네?”

“응?”

“그게 무슨 말씀이십니까. 아까 공자님께서 제게 할 말이 있다고 불러내셨으면서.”

칸 영화제가 선정한 올해의 배우인가.

정말 아무것도 모른다는 듯이 눈을 깜빡이는 모습에 순간 나까지 속아 넘어갔을 정도다.

소년 의생의 껍질을 뒤집어쓴 괴물이 맑게 웃으며 말을 이었다.

“아, 잠깐 자리를 옮기자고요? 알겠습니다.”

“아냐. 될 수 있으면 그냥 이 자리에서 얘기하는 게 좋을 것 같…….”

“아, 잠깐 자리를 옮기자고요? 알겠습니다.”

“……그래, 그러자.”

엄마 보고 싶다.

나는 눈물을 머금고 문경을 따라 걷기 시작했다.

드문드문 보이는 제갈세가와 무당파, 수룡채 수적들을 피해 인적이 끊긴 곳으로 접어들자 비로소 문경의 입이 열렸다.

“암천(暗天). 놈들의 소행이냐?”

“어, 아무래도 그런 것 같은데.”

“여기 사람 없다.”

나는 빛의 속도로 말을 정정했다.

“그런 것 같습니다.”

“아직 확실하지는 않은 모양이로군.”

“언제나 일말의 가능성은 있으니까요. 하지만 진법이 발견되지 않았을 뿐, 암천의 소행이 확실하다고 봅니다.”

“암천이라, 암천…….”

낮게 뇌까린 문경이 문득 고개를 들었다.

보름달마저 모습을 감춘 어두운 밤하늘을 말없이 응시하던 그는 잠시 후 불쑥 입을 열었다.

“시신들을 보며 이상한 점을 느끼지 못했느냐?”

“이상한 점이라면……?”

“시신에 남겨진 상흔(傷痕).”

모든 죽음은 흔적을 남긴다. 특히 무림인들 간의 싸움에서 발생한 사망이라면 더더욱 그렇다.

견문이 넓고 여러 무공의 특징에 대해 꿰뚫고 있는 고수라면 시신에 남은 상흔만으로도 어떤 병장기를 사용했는지, 어떤 초식으로 망자를 죽음에 이르게 했는지 단번에 파악할 수도 있다고 들었다.

그리고 지금 내 눈앞에 있는 이 소년 의생은 그럴 만한 안목과 무공을 갖춘, 무림 최고의 검시관 중 하나다.

“처음 보는 상흔이었다. 아주 기본적인 삼재검법(三才劍法)의 무리를 따른 것 같으면서도, 파도처럼 출렁이는. 아주 희한하고 묘한 상흔이야.”

문경이 천천히 손을 들어 허공을 향해 휘저었다. 올올이 흘러나온 공력이 어둠 속에서 희미한 빛을 뿜어낸다.

“유추해 보건대, 흉수가 사용한 것은 흔히 찾아볼 수 있는 병장기가 아니다. 검신이 구불구불한 사검(蛇劍)에 가까운 기병이야.”

“저는 강기(罡氣)로 베었다고 생각했습니다.”

“네 짐작이 맞다. 강기, 혹은 강기 만큼이나 예리한 무언가가 분명해.”

강기만큼이나 예리한 무언가라면 만년한철이 유일하다.

그리고 암천이 아무리 준비를 철저히 했다 하여도 그 많은 병력들이 만년한철로 만든 병장기를 사용할 리는 없었다.

‘황금이 아무리 많아도 구하기 힘든 것이 만년한철이니까.’

이건 자본이 아니라 자원 희소성의 문제다. 잠시 생각에 잠겨 있던 내게 문경이 물었다.

“시신을 모두 살펴보았느냐?”

“전부는 아니고, 눈에 띄는 시신들은 봤습니다. 제가 그리 견문이 넓은 편이 아니라서, 직접 봐도 무슨 무공과 초식인지 잘 모르겠더군요.”

“네가 본 시신 중에는 장강일도 황충의 것도 있었다. 어땠느냐?”

“강기에 의해 단숨에 허리가 끊겼습니다. 다만 부패가 너무 심한 나머지 거기까지밖에는…….”

“하면 광수도귀와 파랑호는?”

“그건…….”

나는 문득 눈살을 찌푸렸다. 갑자기 세 구의 시신이 가진 공통점이 떠올랐기 때문이었다.

‘……상반신만 남아 있었어.’

세 구의 시신 모두, 떨어져 나간 하반신은 어디에서도 찾을 수 없었다.

앞서 그런 시신 여러 구를 본 탓에 당시로서는 이상함을 느끼지 못했는데, 확실히 의문이 드는 부분이다.

“물고기들이 뜯어 먹은 게 아니었습니까?”

“그것도 틀린 말은 아니겠지. 살펴본 바에 의하면 동정채의 몰살은 이미 열흘 전의 일이다. 추위가 사라진 지 오래이니 부패가 심한 것은 당연하며, 물에 잠긴 시신들은 말할 것도 없을 것이다.”

따사로운 햇볕과 축축한 습기는 죽음이 남긴 많은 흔적을 지워 버렸다.

하지만 그것과는 별개로, 또 다른 흔적까지 지우지는 못했다.

“그에 비해 양민들의 시신은 비교적 사지가 온전했다. 이 사실을 알고 있었느냐?”

“예. 무공을 익히지 않은 이들의 경우에는 보통 베인 것이 아니라 으스러졌더군요.”

어린아이와 여인, 노약자들은 다른 수적들의 시신과 달리 몸뚱어리가 절단되지는 않았다. 다만 전신이 으스러지고, 뭉개졌을 뿐이다.

그리고 거기에 한 가지 더.

“가옥과 주위의 지면이 온통 무너져 있더군. 이는 만근의 힘이 가해지지 않고서야 불가능한 일이며, 고강한 공력을 지닌 내가고수가 택할 만한 수법이 아니다.”

“그러니까, 외공(外功)의 고수다?”

“여기 사람 없다니까.”

“……그냥 혼잣말이었습니다.”

거, 되게 예민하게 구네.

황급히 변명한 나는 잠깐 생각에 잠겼다.

무림에서의 무공은 크게 두 분류로 나뉜다. 공력의 효율과 활용을 중시하는 내공. 그리고 공력을 사용하기는 하나, 신체를 극한으로 단련하는 외공.

무공에 입문함과 동시에 두 가지 선택지를 마주한 사람들은 대부분 전자를 택한다.

외공 수련이 매우 고통스럽다는 이유도 있지만, 성과를 이루기 위해서는 기나긴 인고의 시간이 필요하기 때문이었다.

‘그건 즉, 이 정도 파괴력을 낼 수 있는 초절정의 외공 고수가 손에 꼽는다는 뜻이지.’

애초에 천하를 거꾸로 뒤집어 탈탈 털어 봐도 얼마 없는 초절정 고수다.

답을 구하는 눈빛으로 슬쩍 문경을 바라보자, 소년 의생의 매끈한 이마에 작은 주름이 잡혔다.

“그렇게 봐도 소용없다. 나 역시 놈의 정체를 모르니. 아니, 놈이 아니라 놈들이라고 해야겠군.”

“두 명입니까?”

“적어도 둘. 많으면 셋이다.”

“초절정 고수가 셋이나…….”

“짐작하기로는 사천에서 상대했던 기련삼괴 이상이다. 적어도 그중 하나는 특이한 기병을 사용하는 자고.”

아니, 시벌. 별이 다섯 개도 아니고 무슨 초절정 고수가 셋씩이나 있냐.

문경과 적천강이 떡 버티고 있으니 망정이지, 그렇지 않았다면 무슨 일이 생길까 봐 자리도 못 비웠을 거다.

“이 정도 정보면 삼괴(三怪), 그놈이 알 수도 있겠네요. 그래도 한솥밥 먹는 동료들이 누군지는 들어 봤을 테니까요.”

사천에서 생포한 삼괴는 내가 제갈세가로 가는 이유 중 하나다.

불알이 으스러진 이후로 조울증 환자처럼 변했다고 들었는데, 성심성의껏 조진다면 얼마 버티지 못할 것이다.

‘어쩌면 놈을 앞세워서 진법을 찾아낼 수도 있고.’

희망찬 생각에 잠겨 있던 바로 그 순간이었다.

“어쩌면 이미 모두가 알고 있는 사람인지도 모른다.”

“예?”

“기병을 쓰는 그놈 말이다.”

그 말의 뜻을 이해하는 데에는 제법 오랜 시간이 필요했다. 망치로 뒤통수를 한 대 얻어맞은 듯한 충격.

나는 멍하니 문경을 바라보며 물었다.

“진심이십니까?”

“원숙한 초절정의 고수. 그리고 초식을 읽기 힘들 만큼 특이한 초식과 상흔. 그만한 경지에 이와 같은 기병을 쓰는 자는 결코 흔치 않지.”

“그럼 정말…….”

문경의 입술 사이로 건조한 목소리가 흘러나왔다.

“동정어옹(洞庭漁翁). 지금으로서는 그가 가장 유력하겠지.”

“……!”

일평생 동정호 인근을 떠나지 않았다는 기인이사.

특이하게도 흑목으로 만든 낚시대를 독문병기로 사용하며, 친우인 해사방주의 비보에 분노하여 천령폭을 넘은 뒤 자취를 감춘 초절정 고수.

‘모든 게 정확히 맞아떨어져.’

잠시 잊고 있었다. 그의 존재를.

이건 결코 근거 없는 의심이 아니다.

다른 이들과 달리 동정어옹의 시신은 아직까지도 발견되지 않았고, 부러진 흑목조간만이 그가 남긴 유일한 흔적이다.

비록 짐작이지만, 만약 동정어옹이 정말 암천의 일원이라면?

“하지만 제갈 대협에게 들은 동정어옹은 그럴 이유가 전혀 없는…….”

“모든 것에는 이유가 있기 마련이다. 동정어옹 역시 사람. 누구에게도 보이지 않았던 그림자가 있겠지. 제갈풍 역시 지금쯤 그를 의심하고 있을 것이다.”

문경이 서늘한 목소리와 함께 돌아섰다.

“항상 의심하고, 주의해라. 무운을 비마.”
```

## Final English reading copy

```markdown
# Chapter 451

“Benefactor, where are you going?”

“Huh?”

I flinched as I quietly headed for the door. Cheongpung, who had gathered his belongings, tilted his head and looked at me.

“What? Why?”

“Are you going somewhere?”

“I, uh… something urgent came up.”

“You said we had to leave quickly.”

“Listen, Young Hero Cheong. I wasn’t going to say this, but…”

I deliberately hardened my expression.

“I’m going to relieve myself. Happy?”

“But the privy isn’t in that direction.”

“…”

He was annoyingly sharp.

Martial arts were his minor, while eating and shitting were his major. He had to know the location of every privy on the island.

After hesitating for a moment, I answered.

“…I’m going to piss outside.”

Even I had to admit it was a desperate excuse.

Only then did Gung Gibang and Hyuk Mujin realize something was off. They stopped packing their bags and turned to look at me.

“Young Hero Gung, doesn’t the Captain seem unusually long-tongued today?”

“Yeah. Why does he look so restless?”

“That’s because I’m trying to decide which of you two to hit first.”

Normally, they would have backed down the moment I said something like that. But after being thoroughly conditioned by my violence, the two of them had grown considerably.

“Hmm. If this were our usual Captain, his hands would have moved before his words. But he’s trying to talk his way out of it? There’s definitely something going on.”

“Right?”

“Absolutely. Do you think I’ve only been beaten once or twice? There’s a reason and a flow to all this.”

Just as Hyuk Mujin was staring at me with narrowed eyes, Gung Gibang’s eyes suddenly widened, and he looked around.

“Wait. Where did Mungyeong go?”

“Oh, yeah. He was with us a moment ago. Where the hell did he go?”

Where did he go? He had already gone outside to wait for me.

*Let’s talk.*

I sighed as I remembered the Sound Transmission Mungyeong had sent me earlier.

If I denied it any further, I would only attract more suspicion.

“He’s outside. We have something to discuss privately.”

“In the privy? Just the two of you?”

“…What the hell are you talking about, you lunatic? You’re making it sound suggestive.”

Hyuk Mujin looked at me with a suspicious expression.

“Captain. I’ve already been conditioned to insults and violence, so I’ll be fine. But please don’t expose Mungyeong to anything strange.”

“…”

What the hell was this lunatic talking about? I was the one who looked ready to be stained with blood.

I was so dumbfounded that I could barely speak when Gung Gibang added his own remark.

“Hyuk’s right. The more I see that kid, the more thoughtful and kind he seems. Don’t harass him for no reason.”

“Wow. You bastards, seriously…”

I stopped myself.

“Forget it. What would you two know?”

Cheongpung had at least finally noticed what was going on and kept his mouth shut like a mute with honey in it…

No, now that I looked closely, he really was stuffing candy into his mouth.

*Where does that candy of his keep coming from?*

If I stayed here any longer, I was going to lose my mind.

I shook my head and ignored the voices coming from behind me as I left the house.

Outside, Mungyeong was waiting for me in the courtyard, dressed in spotless white robes.

“You’re late.”

“It didn’t take that long…”

“You’re late.”

“Sorry…”

“You’re late.”

“…”

*Please save me.*

The pressure of that endless repetition was no joke. His aura was being directed at me so subtly that no one else could notice it, and I swallowed hard.

“S-sorry I’m late. But what’s going on?”

“Pardon?”

“Huh?”

“What do you mean? You called me out earlier because you had something to say.”

Was he this year’s actor selected by the Cannes Film Festival?

He blinked as if he truly knew nothing. For an instant, even I almost fell for it.

The monster wearing the shell of a young medical apprentice smiled brightly and continued.

“Oh, you want us to move somewhere else for a moment? Understood.”

“No. If possible, I think it would be better to talk right here…”

“Oh, you want us to move somewhere else for a moment? Understood.”

“…Fine. Let’s go.”

I miss my mother.

Holding back tears, I began walking after Mungyeong.

We avoided the occasional disciples of the Zhuge Clan and Wudang, along with the river bandits of Water Dragon Stronghold, and entered a deserted area. Only then did Mungyeong finally speak.

“Dark Heaven. Did they do this?”

“Yeah. It seems that way.”

“There’s no one here.”

I corrected myself at the speed of light.

“It seems that way, sir.”

“So it is not certain yet.”

“There is always a possibility. But even though no formation was found, I believe this was definitely Dark Heaven’s doing.”

“Dark Heaven. Dark Heaven…”

Mungyeong muttered the words under his breath, then suddenly raised his head.

He silently stared at the dark night sky, where even the full moon had hidden itself. After a moment, he spoke without warning.

“Did you notice anything strange when looking at the corpses?”

“Something strange?”

“The marks left on them.”

Every death left traces. This was especially true of deaths caused by fighting between martial artists.

I had heard that a master with broad experience and a deep understanding of various martial arts could identify an opponent’s weapon and even determine which form had killed the deceased simply by examining the wounds left on the corpse.

And the young medical apprentice before me possessed the insight and martial arts to make him one of the finest forensic examiners in Murim.

“I’ve never seen wounds like these before. They seem to follow the principles of the very basic Three Calamities Sword Technique, yet they ripple like waves. They’re extremely strange and unusual.”

Mungyeong slowly raised one hand and waved it through the air. Strands of internal energy flowed from his fingertips, giving off a faint light in the darkness.

“If I had to guess, the culprit was not using an ordinary weapon. It was an unusual weapon with a crooked blade, something resembling a Snake Sword.”

“I thought they were cut with Force.”

“Your guess is correct. It was Force—or something equally sharp.”

The only thing as sharp as Force was Ten-Thousand-Year Cold Iron.

And no matter how thoroughly Dark Heaven had prepared, there was no way all those soldiers could have been equipped with weapons made of Ten-Thousand-Year Cold Iron.

*No matter how much gold you have, Ten-Thousand-Year Cold Iron is difficult to obtain.*

This was not a matter of capital. It was a matter of resource scarcity.

As I stood lost in thought, Mungyeong asked me a question.

“Did you examine all the corpses?”

“Not all of them. I looked at the ones that stood out. I’m not especially knowledgeable, so even after seeing them firsthand, I couldn’t tell what martial arts or forms had been used.”

“Among the corpses you examined was that of Hwang Chung, the Yangtze One Saber. What did you think?”

“His waist was severed in a single blow by Force. But the decay was so severe that I couldn’t determine anything beyond that…”

“What about the Mad Water Saber Demon and the Wave Fox?”

“Those two…”

I suddenly frowned.

A common feature shared by three corpses had just come to mind.

*…Only their upper bodies remained.*

The lower halves of all three corpses were nowhere to be found.

I had seen several corpses like that earlier, so I had not found it strange at the time. But now that I thought about it, it was certainly suspicious.

“Wasn’t it because the fish ate them?”

“That would not be entirely incorrect. According to my examination, the massacre at Donghu Stronghold took place ten days ago. The cold weather ended long ago, so severe decay is only natural. The corpses that were submerged in water would be even worse.”

Warm sunlight and damp air had erased many of the traces left behind by death.

But they had not erased everything.

“Compared to them, the limbs of the commoners’ corpses were relatively intact. Did you notice that?”

“Yes. Those who had not learned martial arts were not cut apart. They had been crushed.”

Unlike the corpses of the river bandits, the bodies of the children, women, and elderly had not been severed. Their entire bodies had simply been crushed and pulverized.

And there was one more thing.

“The houses and the ground around them had all collapsed. That would have been impossible without a force of ten thousand geun, and it is not a method an internal-arts master with powerful internal energy would choose.”

“So, an external-arts master?”

“There’s no one here, remember?”

“…I was just talking to myself.”

He was being awfully sensitive.

After making that hasty excuse, I fell silent for a moment.

Martial arts in Murim could broadly be divided into two categories.

Internal arts emphasized the efficient use and application of internal energy. External arts also used internal energy, but focused on tempering the body to its limits.

Most people were faced with those two choices as soon as they entered the world of martial arts, and most chose the former.

External-arts training was extremely painful. More importantly, it required a long period of endurance to achieve any meaningful results.

*That means there are only a handful of Supreme Peak external-arts masters capable of producing this level of destructive power.*

There were hardly any Supreme Peak masters in the world to begin with, even if you turned the entire world upside down and shook it out.

I glanced at Mungyeong, silently asking for an answer. A small wrinkle appeared on the smooth forehead of the young medical apprentice.

“Looking at me won’t help. I don’t know his identity either. No—I should say their identities, not his.”

“There are two of them?”

“At least two. Three at most.”

“Three Supreme Peak masters…”

“Based on my guess, they are even more formidable than the Qilian Three Fiends we faced in Sichuan. At least one of them uses an unusual weapon.”

*For fuck’s sake. This isn’t some five-star establishment. Why are there three Supreme Peak masters?*

It was only because Mungyeong and Jeok Cheongang were holding the line that I could afford to leave the stronghold at all. If they had not been here, I would have been too worried to go anywhere.

“With this much information, the Third Fiend might know something. He must have heard who his fellow conspirators were.”

The Third Fiend captured in Sichuan was one of the reasons I was going to the Zhuge Clan.

I had heard that he had become like a bipolar patient after his balls were crushed, but if I worked him over with care and dedication, he would not last long.

*Perhaps we can even use him to find the formation.*

That hopeful thought had barely crossed my mind when Mungyeong spoke.

“Perhaps it is someone everyone already knows.”

“What?”

“I mean the one who uses that unusual weapon.”

It took me a long time to understand what he meant.

The shock felt as if someone had struck me in the back of the head with a hammer.

I stared blankly at Mungyeong.

“Are you serious?”

“An experienced Supreme Peak master. Forms and wounds so unusual that it is difficult to read them. There are not many people who have reached that realm and use a weapon like this.”

“Then it really is…”

A dry voice slipped between Mungyeong’s lips.

“The Dongting Fisherman. At present, he is the most likely suspect.”

“…”

The eccentric master who had never left the area around Dongting Lake his entire life.

Unusually, he used a fishing rod made of black wood as his signature weapon. He was a Supreme Peak master who had crossed Tianling Falls and disappeared after becoming enraged by the tragic news concerning his friend, the head of the Sea Serpent Society.

*Everything fits perfectly.*

I had forgotten for a moment.

I had forgotten about his existence.

This was not a baseless suspicion.

Unlike the others, the Dongting Fisherman’s corpse had never been found. The only trace he had left behind was his broken black-wood fishing rod.

It was only a guess, but what if the Dongting Fisherman really was a member of Dark Heaven?

“But the Dongting Fisherman Zhuge Feng told me about had absolutely no reason to do something like this…”

“Everything has a reason. The Dongting Fisherman is a person, too. He must have had a shadow no one else could see. Zhuge Feng is probably suspicious of him by now as well.”

Mungyeong turned away, his voice cold.

“Always be suspicious, and stay alert. May martial fortune be with you.”
```
