<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0452.txt",
      "sha256": "d00b489da3f680e663d8fadf4cd7724ee83fddfec2c475c8d4e66fcdb2e6c8ca",
      "bytes": 12830
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fc67b2df15a0070710d9c02d8ac33db37ca2b7bdb6bba98808bdc3176d539359",
      "bytes": 3159
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "112f587be3f6d9c27d9adeace733f5d6e7aee85ab11331c41c2d18d886f7df37",
      "bytes": 148233
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "ddcfe4e1dc23598798c0593581040dc9c9ac780f8d596075926fca74c14b2f33",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "27606af60078539921fb0a37206f6d78afee294b07a798340e35dfe9c77a2339",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ccccd0ab889fd3120139f84f22e2b28c9bfae83d22d8a79f3a60183364743903",
      "bytes": 1108
    },
    {
      "path": "characters/Jang-pal.md",
      "sha256": "e4dfab4b79f6e04b0b60dcb8882c232f42ea4ec1330e43a13bc7c0d5ba922e06",
      "bytes": 515
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "08335da52fde9cf89ed9e0fb5ca9c6f21d5ab4b3392d90939f87243a8d1a6b8e",
      "bytes": 1470
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "eaf2fc568c117c4c58f9fd6361e858e7b75508ec611b9e5e00eba1740b332c20",
      "bytes": 864
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "ea920b237ccb4b53ca5957242da997e060032caa51242d22a822183569f62bcc",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "10262710e0e4185cc1ca2b6219b0ef7421cba1aec79830b1e7daa1f22d38120f",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e461e36fdfca1b36145d5e3c2c1ab27e0d867d36d7f0c4d6478c5994b61b21fa",
      "bytes": 142508
    }
  ],
  "estimated_tokens": 11829
}
-->

# Durable State Update — Chapter 452

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 452. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 452. Profile updates may replace only one
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
  "chapter": 452,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 452,
    "continuity_sources": [452],
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
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Mungyeong believes the Dongting Fisherman is the most likely Dark Heaven suspect, but the culprit's identity and motive remain unconfirmed."
  ],
  "continuity_sources": [
    451,
    450
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left behind?",
    "Is the Dongting Fisherman a member of Dark Heaven, and who are the other Supreme Peak attackers?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 451,
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
| 태원진가   | **Jin Family of Taiyuan**        |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 신법     | **movement technique**                           |                                                       |
| 은인     | **Benefactor**                               |
| 민첩               | **Agility**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 만리추풍신법 | **Myriad-Li Chasing Wind Movement Technique** | Beggars' Sect movement technique known for speed. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 융중산 | **Mount Longzhong** | Mountain associated with Zhuge Kongming's seclusion. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 451
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 451
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 451
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jang-pal.md

# Jang-pal (장팔)

- **Safe through:** Chapter 169
- **Aliases:** None
- **Role:** Woodcutter from Jang Family Village who encounters and helps the unnamed old man.
- **Personality:** Simple, kind, polite, and guileless.
- **Voice:** Plain, respectful, and good-natured.
- **Relationships:** Husband whose wife prepares his rice ball; lives in Jang Family Village and helps the unnamed old man by sharing food and carrying him down the mountain.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 451
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 450
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is a member of the Yangtze River Channel League's moderate faction; Hwang Chung, his senior and Uncle Hwang, was the League elder and Donghu Stronghold Lord who was killed in its destruction.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 451
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 451
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃452화



처음 들어왔을 때와 달리 나가는 길은 생각만큼 힘들지 않았다.

천령폭의 와류가 주로 바깥쪽을 향해 휘몰아치는 까닭도 있었지만, 수룡채 내부에서도 뱃일에 잔뼈가 굵은 고참 수적들이 자신들의 능력을 십분 발휘한 덕분이기도 했다.

“좌현으로 꺾어!”

“우측, 신호가 떨어질 때까지 노를 젓지 마라!”

“더, 더, 더…… 지금!”

“으합!”

콰아아아아, 철썩!

“배가, 배가 기울어진다!”

“진 대혀업!”

“도와주십쇼!”

“……하, 이 새끼들.”

생각해 보면 좀 힘들었던 것 같기도 하다.

하지만 크게 문제 될 것은 없었다. 적천강과 문경이라는 강력한 우군이 없다 해도 나와 청풍이 나서면 어지간한 위기쯤은 헤쳐 나갈 수 있으니까.

‘처음이 어렵지, 두 번이 어렵나.’

천령폭의 거친 와류에 익숙해진 것은 수적들뿐만이 아니다. 일찌감치 대비하고 있던 나는 힘차게 쌍장(雙掌)을 내질렀다.

퍼엉!

기우뚱거리던 쾌조선이 중심을 되찾는다. 이제 속도를 더하여 이 지긋지긋한 와류를 벗어나야 할 때.

나는 이런 상황을 위해 후미에 배치해 둔 한 사람의 이름을 외쳤다.

“청 소협, 지금이야!”

“끼얏호우!”

“아니, 이 미친놈아! 거기 매달려서 놀지 말라고!”

“앗, 죄송해요. 은인. 저도 모르게 그만…….”

“빨리 하기나 해!”

“네!”

퍼퍼펑!

청풍은 정상인과는 상당히 거리가 먼 놈이지만, 실력 하나만큼은 확실했다.

강력한 공력이 실린 수십 개의 장영(掌影)이 허공을 격하고 수면을 후려치자, 강한 추진력이 더해진 쾌조선이 천령폭의 와류를 뛰어넘어 착지했다.

쿵! 촤아아아악!

높이 솟구친 물보라가 쾌조선의 선체를 뒤덮었다. 머리부터 발끝까지 강물을 뒤집어쓴 궁기방과 혁무진이 중얼거렸다.

“빌어먹을. 전에는 담가지더니 이제는 뒤집어쓰는군. 아주 가지가지야.”

“이 자리에서 맹세하는데, 이번 일만 마무리되면 장강에는 두 번 다시 안 올 겁니다. 하루하루가 거지 같아요.”

“……너 지금 나한테 시비 거는 거냐?”

“아니, 솔직히 거지 같긴 하잖아요.”

“그건 그래. 기분이 더러운데 맞는 말이야. 맞는 말인데 기분이 더러워.”

“하, 기분 진짜 거지 같네.”

“……알겠으니까 그만해라.”

저것들은 틈만 나면 저러고 자빠졌네.

찍먹에 이어 부먹까지 경험한 두 탕수육의 투닥거림을 뒤로하고, 무사히 천령폭을 통과한 선체는 쾌속하게 장강을 가로지르며 나아갔다.

그리고 약 세 시진 후, 새벽녘에 출발한 쾌조선이 조양(棗陽)의 나루터에 닿았을 때는 이미 정오가 가까워진 시각이었다.

“제갈세가가 있는 융중산(隆中山)까지 장강의 물길이 닿지 않으니, 지금부터는 육로로 이동하셔야 합니다.”

무송을 대신하여 온 수룡채 부채주가 건넨 말에, 나는 고개를 끄덕였다.

호북성은 수륙교통이 크게 발달한 곳이지만, 그렇다고 해서 장강의 지류가 모두 연결되어 있지는 않았다. 물이 없는 곳에 배가 갈 수는 없는 법이다.

‘얘들이 뭐 바이킹도 아니고.’

대신 넓고 평탄한 관도가 잘 정비되어 있으니 마차나 경신법을 발휘한다면 금방 도착할 수 있다.

조양과 융중산은 비교적 인접한 곳이라 그리 오랜 시간이 걸리진 않을 것이다.

제갈풍의 지시로 우리와 동행하게 된 제갈세가의 가솔 역시 놀고 있지만은 않았다.

“조양 분타에 즉시 연통을 넣어 마차를 준비해 놓겠습니다. 관도 곳곳에 역관이 설치되어 있으니, 마차를 갈아탄다면 본가까지는 금방입니다.”

“오, 맞네.”

제갈세가는 무당파와 함께 호북성을 양분하는 명문 대파.

태원진가도 산서성 곳곳에 지부나 분타를 세워 영역에 대한 지배력을 공고히 하는데, 이들은 그보다 더했으면 더했지 덜하진 않을 것이다.

대형 브랜드가 체인점을 내는 것과 같은 이치라고 해야 하나.

‘그럼 늦어도 반나절이면 도착하겠네.’

머릿속으로 대충 소요 시간을 계산하며 배에서 내린 바로 그 순간이었다.

처처척.

일사불란한 발걸음 소리와 함께 나타나 나루터를 에워싸는 일단의 무리.

나는 눈살을 찌푸리며 불청객들을 응시했다.

‘이건 또 뭐야.’

서른 명에 달하는 무인들이다.

하나같이 척 봐도 상급의 품질로 보이는 청강장검을 허리춤에 차고, 윤기가 좌르르 흐르는 푸른 비단 무복을 걸친 그들의 모습에 혁무진이 눈을 크게 떴다.

“저건…….”

“왜, 혹시 아는 놈들이냐?”

“아뇨. 저 비단 무복 보고 놀란 건데요.”

“뭐?”

“저게 사천에서 나는 촉금(蜀錦)이라는 건데, 천하의 비단 중에서도 최고로 칩니다. 저희 아버지 꿈이 촉금을 창고 한가득 쌓아 두는 거였어요. 그만큼 비싸고 귀한 건데…… 저걸로 무복을 만들어 입다니. 고용주가 누군지는 몰라도 돈 많나 본데요?”

“…….”

이 자식은 정체를 말하라니까 비단 품질 따지고 있네.

어이없는 눈빛으로 바라보자 궁기방이 혀를 쯧쯧 차며 끼어들었다.

“저놈은 무림인인지, 포목상인지 모르겠군. 저 혁가 놈에게 괜한 기대하지 말고 이 어르신에게 물어봐라.”

“어르신은 모르겠고, 병신은 만들어 줄 수 있으니까 주먹 날아가기 전에 빨리 말해라.”

“……청협방(靑俠房)의 무인들이다. 말했으니까 제발 주먹에 힘 좀 풀어라.”

“청협방? 그게 뭐 하는 놈들인데.”

궁기방이 여전히 굳게 쥐어져 있는 내 주먹을 바라보며 대답했다.

“정식 문파는 아니고, 호북성에서 여러모로 상당한 영향력을 행사하는 자들이지.”

“그런 것치고는 다들 허접해 보이는데?”

나는 저 멀리 도열한 무인들을 힐끗 바라보았다.

값비싼 촉금 비단으로 무복을 만들어 입고, 질 좋은 검을 찼지만 그게 전부다.

대부분은 일류에도 못 미치는 이, 삼류 칼잡이들이고, 무공보다는 외관에 신경 썼는지 하나같이 체격이 좋고 용모가 뛰어났다.

‘얼굴에는 화장까지 했네.’

이 정도면 무림인이 아니라 아이돌 아니냐.

한국에서 시작된 K팝 열풍이 세계를 넘어 무림에까지 영향을 끼친 건지 의심될 정도다.

청협방탄무인단. 뭐 그런 이름으로 행사 뛰러 온 건 아닐까.

“쟤들 그룹명이, 아니 단체명이 청협방이라고 했지? 저런 애들이 호북성에서 잘나간다고?”

“방귀깨나 뀌는 편이라고 들었다.”

“막상 실전 들어가면 바로 오줌 지릴 것 같은데…….”

설마 호북성에서는 인기투표로 문파 순위가 매겨지는 건가.

심각하게 고민하고 있던 그때 제갈세가의 가솔이 입을 열었다.

“청협방은 일종의 친목회입니다.”

“친목?”

“예. 이곳 호북성 각지에서 크고 작은 영향력을 지닌 유력자의 자제들이 모여 만든 곳이지요. 항상 몰려다니며 온갖 사고를 치고는 합니다만, 든든한 배경이 있으니 늘 흐지부지되기 일쑤입니다.”

“아, 금수저 모임이구나.”

“뭐라 하셨는지…….”

“별거 아니에요. 그럼 뭐 저희는 갈 길 가면 되겠네.”

뭐 하는 놈들인가 했더니, 겉치장만 요란하게 하고 다니는 빈 수레였다.

어디에나 있는 한심한 족속들. 그것으로 청협방에 대한 관심을 끈 나는 앞장서서 걸음을 옮겼다.

“조양 분타로 가려면 어느 쪽으로 가면 됩니까?”

“이 위치에서는 일각도 안 걸립니다. 우선 저기 보이는 대로변으로…….”

제갈세가의 가솔이 말꼬리를 흐렸다.

막 그가 말했던 대로변으로부터, 지금껏 본 적이 없을 만큼 호화로운 행렬이 다가오고 있었기 때문이었다.

“청협방의 영웅들께서 행차하십니다!”

족제비 수염의 중년인이 얇은 목소리로 외치자, 행렬의 좌우로 걸어가던 악사들이 악기를 연주하고 아름다운 여인들이 꽃잎을 허공에 흩뿌린다.

삽시간에 축제 분위기에 휩싸인 대로변.

길을 오가던 양민들이 불만과 기대가 뒤섞인 표정으로 행렬을 지켜보았다.

그들의 수많은 시선 끝에는 용과 봉황이 아로새겨진 사인교(四人轎)에 올라탄 열 명의 남녀가 있었다.

있는 자만이 가질 수 있는 여유와 웃음을 전신에 두른 그들은, 초라한 행색의 양민들을 내려다보며 손에 든 무언가를 내던졌다.

촤르르르륵!

암기……가 아니라 돈이다. 그것도 철전 백 개의 값어치를 지닌, 번쩍번쩍 빛나는 은전.

나는 그제야 왜 양민들의 표정에 기대감이 서려 있었는지 알 수 있었다.

“와아아아아!”

“은전! 은전이다!”

“장팔, 이 숭악한 새끼가 어딜 감히 남의 은자를 가로채려고. 당장 손 떼지 못하겠느냐!”

“지랄한다. 내 손이 먼저 닿은 거 못 봤어?”

“이런 개호로……!”

쉬지 않고 떨어지는 꽃잎과 은자 위로 사람들의 환호와 욕설이 뒤덮인다.

뜻밖의 횡재에 은자를 깨물어 보는 아낙네, 서로 자신이 주인이라 주장하며 고성을 높이다가 이내 싸움을 벌이는 사내들.

그리고 사인교에 앉아 그 광경을 바라보며 웃음을 터트리는 젊은 남녀들까지.

“아주 개판이 따로 없구만.”

고개가 절레절레 내저어지는 광경이다.

돈을 뿌리면서 서커스 보듯이 사람들의 반응을 즐기는 저 금수저들은 한심해 보였고, 은자 하나를 갖기 위해 아귀다툼을 벌이는 양민들의 모습은 씁쓸하면서도 짠했다.

그래 봤자 나와는 아무런 상관도 없는 일이지만.

“저런 건 그만 신경 쓰고 얼른 가…….”

나는 말을 잇지 못하고 눈을 깜빡였다. 뭔데, 이거.

없다.

방금 전까지만 하더라도 옆에 있던 놈들이 어딜 갔는지 한 놈도 보이지 않고, 제갈세가의 가솔만이 뻘쭘하게 자리를 지키고 있었다.

“아니, 이 자식들 전부 어디 갔어요?”

머뭇거리던 가솔이 손을 들어 한 방향을 가리켰다.

“저기 계십니다.”

“……?”

고개를 돌린 나는 할 말을 잃었다.

쉭, 쉬쉬쉭!

“어엇! 안 돼!”

“내 은자!”

유령 같은 몸놀림으로 사람들 사이를 누비며 허공의 은자를 낚아채는 한 사람. 아니, 거지새끼.

‘만리추풍신법(萬里追風身法)?’

미친놈이 개방의 절기를 저기에 쓰고 자빠졌네.

심지어 지금까지 봤던 어떤 모습보다 빠르고 민첩하다. 오 성까지밖에 못 익혔다고 우는 소리를 그렇게 하더니, 지금 보여 주는 움직임은 최소 칠 성 이상이다.

‘개방 망신은 저 자식이 다 시키는구나.’

아무리 거지라지만 저렇게까지 본분에 충실할 수가 있나.

하지만 남의 문파 망신을 신경쓰기에는 우리 태원진가의 다크호스도 만만치 않았다.

“하압!”

쉬쉭! 타다다닥!

지면을 박차고 솟구친 혁무진이 검을 휘둘렀다. 힘 있고 유려한 궤적에 휘말린 은자가 허공으로 붕 뜨더니 이내 검신 위로 촤르륵 떨어진다.

은자를 확인한 혁무진의 얼굴이 환해졌다.

“와! 은자가 열 개!”

“…….”

저 자식은 무조건 열 대 예약이다.

나는 목구멍까지 차오르는 욕설을 삼키며 마지막 남은 한 사람을 찾았다.

‘청풍, 이 자식은 어디 있어.’

전심전력으로 은자를 쓸어 담는 궁기방, 혁무진과는 달리 청풍의 모습은 보이지 않았다.

하지만 청풍이라는 생물의 습성을 꿰뚫고 있는 나는 얼마 지나지 않아 녀석을 찾을 수 있었다.

“우선 당과 열 개랑요. 어어, 전병도 좀 주세요. 방금 집어 든 그거 말고, 저쪽에 크고 양 많은 걸로요. 와아, 감사합니다! 혹시 만두 가게는 어디 있어요?”

뚝.

머릿속에 있던 무언가가 끊기는 소리와 함께, 눈깔을 허옇게 뒤집어 깐 내가 외쳤다.

“야, 이 개애새끼들아!”
```

## Final English reading copy

```markdown
# Chapter 452

Unlike when we first entered, the trip out was not as difficult as I had expected.

Part of that was because the whirlpools of Tianling Falls mostly spiraled outward. But it was also thanks to the veteran river bandits inside Water Dragon Stronghold, who had spent years working on boats and were making full use of their skills.

“Turn to port!”

“Starboard! Don’t row until the signal!”

“More, more, more… Now!”

“Yaaah!”

Whoooosh! Splash!

“The boat—the boat’s tilting!”

“Great Hero Jin!”

“Help us!”

“…Damn it, you bastards.”

Come to think of it, maybe it had been a little difficult after all.

But it was nothing we couldn’t handle. Even without powerful allies like Jeok Cheongang and Mungyeong, Cheongpung and I could get through most crises if we put our minds to it.

*The first time is hard. Why would the second be?*

The river bandits weren’t the only ones who had grown accustomed to Tianling Falls’ violent whirlpools. I had prepared in advance as well, and thrust both palms forward with all my strength.

Boom!

The tilting fast ship regained its balance. Now was the time to increase our speed and escape this damned whirlpool.

I called out the name of the person I had stationed at the stern specifically for situations like this.

“Young Hero Cheong, now!”

“Yee-haw!”

“You crazy bastard! Stop hanging there and playing around!”

“Oh, sorry, Benefactor. I didn’t mean to, but before I knew it…”

“Just hurry up and do it!”

“Yes!”

Boom, boom, boom!

Cheongpung was about as far from normal as a person could get, but his skills were undeniable.

Dozens of palm shadows infused with powerful internal energy struck through the air and lashed the surface of the water. The resulting thrust sent the fast ship vaulting over the whirlpool of Tianling Falls before landing on the other side.

Boom! Splash!

A towering spray of water fell over the ship’s hull. Gung Gibang and Hyuk Mujin, drenched from head to toe, muttered under their breath.

“Damn it. Last time we got dunked, and now we’re getting drenched. We really get everything.”

“I swear on my life, once this is over, I’m never coming back to the Yangtze. Not ever. Every day feels like living as a goddamn beggar.”

“…Are you picking a fight with me?”

“No. Honestly, doesn’t it feel like we’re living as beggars?”

“That’s true. It feels shitty to hear it, but you’re right. You’re right, but it still feels shitty.”

“Damn, I really do feel like a beggar.”

“…I get it, so shut up.”

Those two acted like this every chance they got.

Leaving behind the bickering of the two sweet-and-sour pork pieces who had now experienced both dipping and pouring sauce, the ship safely passed through Tianling Falls and sped across the Yangtze.

About three shichen later, when the fast ship that had departed at dawn reached the ferry landing at Zaoyang, it was already close to noon.

“The waters of the Yangtze do not reach Mount Longzhong, where the Zhuge Clan is located. From here, you will have to travel by land.”

The deputy Stronghold Lord of Water Dragon Stronghold had come in Mu Song’s place. I nodded at his words.

Hubei Province had highly developed water and land transportation, but that did not mean all the Yangtze’s tributaries were connected. A boat could not travel where there was no water.

*It’s not like these people are Vikings.*

Fortunately, the broad, level highways were well maintained. We could reach our destination quickly by carriage or by using movement techniques.

Zaoyang and Mount Longzhong were relatively close to each other, so it would not take very long.

The Zhuge Clan retainer who had been ordered by Zhuge Feng to accompany us was not standing around idle, either.

“I will immediately send word to the Zaoyang branch and have carriages prepared. Relay stations have been established all along the main roads, so if you change carriages along the way, you will reach our family home in no time.”

“Oh, right.”

The Zhuge Clan was a prestigious major faction that divided control of Hubei Province with Wudang.

The Jin Family of Taiyuan had also established branches and sub-branches throughout Shanxi Province to solidify its control over the region. The Zhuge Clan’s network was probably even more extensive.

*It’s like a major brand opening chain stores.*

*Then we should arrive in half a day at the latest.*

I had just gotten off the boat after roughly calculating the travel time in my head when—

Clack, clack, clack.

A group of people appeared with the sound of perfectly synchronized footsteps and surrounded the ferry landing.

I frowned as I stared at the unwelcome guests.

*What is this now?*

There were nearly thirty martial artists.

Every one of them wore a blue silk martial uniform that gleamed with luster, and each had a fine-steel long sword hanging at his waist. Hyuk Mujin’s eyes widened.

“That’s…”

“What? Do you know them?”

“No. I was just surprised by those silk uniforms.”

“What?”

“That’s Shu brocade, produced in Sichuan. It’s considered one of the finest kinds of silk in the world. My father dreamed of filling an entire warehouse with it. That’s how expensive and precious it is… And they made martial uniforms out of it. I don’t know who their employer is, but they must have a lot of money.”

“…”

I had told the bastard to identify them, and he was evaluating the quality of their silk instead.

When I stared at him in disbelief, Gung Gibang clicked his tongue and cut in.

“I can’t tell whether that bastard is a martial artist or a cloth merchant. Don’t waste your expectations on that Hyuk Family brat. Ask this old man instead.”

“I don’t know about the old man part, but I can make you a cripple. Tell us before my fist gets there.”

“…”

“They’re martial artists from Qingxia Hall. I told you, so please relax your fist a little.”

“Qingxia Hall? What do those bastards do?”

Gung Gibang glanced at my fist, which was still tightly clenched, and answered.

“They aren’t an official sect, but they wield considerable influence in Hubei Province in various ways.”

“They look pretty pathetic for people with that kind of influence.”

I cast a brief glance at the martial artists standing in formation in the distance.

They had made martial uniforms from expensive Shu brocade and carried quality swords, but that was all.

Most were Second or Third Rate swordsmen who fell short of First Rate. Perhaps they cared more about their appearance than their martial arts, because every one of them was well built and handsome.

*They’re even wearing makeup.*

At this point, weren’t they idols rather than martial artists?

The K-pop craze that had begun in Korea must have spread beyond the world and reached the Murim as well.

Qingxia Bulletproof Martial Artist Corps. Maybe they had come to perform at some event under a name like that.

“Those guys’ group name—or, no, their organization name—was Qingxia Hall, right? They’re that popular in Hubei?”

“I heard they’re fairly influential.”

“They look like they’d piss themselves the moment a real fight started…”

Did sect rankings in Hubei get decided by a popularity vote?

I was seriously pondering the question when the Zhuge Clan retainer spoke.

“Qingxia Hall is a sort of social club.”

“A social club?”

“Yes. It was formed by the sons and daughters of influential people with varying degrees of power throughout Hubei Province. They are always running around together and causing all kinds of trouble, but they have such powerful backing that matters usually fizzle out without consequence.”

“Oh. A rich-kid club.”

“I’m sorry, what did you say?”

“Nothing important. In that case, we can just continue on our way.”

So that was what they were. An empty cart making a great deal of noise, dressed up in gaudy finery wherever they went.

Pathetic people like that could be found anywhere. Having lost interest in Qingxia Hall, I took the lead and started walking.

“Which way do we go to reach the Zaoyang branch?”

“It will take less than fifteen minutes from here. First, we should head to the main road over there…”

The Zhuge Clan retainer trailed off.

From the main road he had just mentioned, an extravagantly luxurious procession was approaching—more lavish than anything I had ever seen.

“The heroes of Qingxia Hall are making their procession!”

At the shout of a middle-aged man with weasel whiskers and a thin voice, musicians walking along both sides of the procession began playing their instruments. Beautiful women scattered flower petals through the air.

In an instant, the main road was swept up in a festive atmosphere.

Commoners traveling along the road watched the procession with expressions that mingled expectation and discontent.

At the end of the countless gazes stood ten men and women riding in sedan chairs engraved with dragons and phoenixes.

They carried themselves with the ease and smiles possessed only by those who had money, looking down at the poorly dressed commoners as they tossed something from their hands.

Clatter, clatter, clatter!

Not hidden weapons… money. Shining silver nyang, each worth a hundred iron coins.

Only then did I understand why there had been anticipation in the commoners’ expressions.

“Waaah!”

“Silver nyang! It’s silver!”

“Jang-pal, you filthy bastard! How dare you try to snatch someone else’s silver nyang? Take your hand off it right now!”

“Bullshit. Didn’t you see that my hand got there first?”

“You fucking son of a—!”

The cheers and curses of the people covered the falling flower petals and silver nyang.

Women bit the silver nyang to test it after their unexpected windfall. Men loudly claimed that they were the rightful owners, then soon began fighting over it.

And the young men and women sitting in the sedan chairs laughed as they watched the spectacle.

“What a complete mess.”

It was a sight that made my head shake on its own.

The rich kids scattering money and enjoying the people’s reactions as if they were watching a circus looked pathetic. The sight of the commoners fighting tooth and nail for a single silver nyang left a bitter taste in my mouth and made me feel sorry for them.

But it had nothing to do with me.

“Let’s stop worrying about that and get going…”

I blinked, unable to finish my sentence.

What the hell?

The people who had been beside me moments ago were nowhere to be seen. Only the Zhuge Clan retainer remained, standing awkwardly in place.

“Wait, where did all those bastards go?”

The retainer hesitated, then raised a hand and pointed in one direction.

“They’re over there.”

“…?”

I turned my head and was rendered speechless.

Whoosh, whoosh-whoosh!

“No! You can’t!”

“My silver!”

One person was darting through the crowd with ghostlike movements, snatching silver nyang out of the air.

No. Not one person.

One fucking beggar.

*The Myriad-Li Chasing Wind Movement Technique?*

That lunatic was actually using a Beggars’ Sect secret technique for this?

He was even faster and more agile than he had ever been before. He had complained endlessly that he had only mastered the technique to the fifth stage, yet the movements he was displaying now were at least seventh-stage.

*That bastard is singlehandedly disgracing the Beggars’ Sect.*

Even if he was a beggar, how could he be this devoted to his calling?

But as little as I cared about another sect’s reputation, the Jin Family of Taiyuan’s own dark horse was no less impressive.

“Hah!”

Whoosh! Rat-a-tat-tat!

Hyuk Mujin kicked off the ground and soared into the air before swinging his sword. The silver nyang caught in the powerful, fluid arc flew upward, then came raining down onto the flat of his blade.

Hyuk Mujin’s face lit up when he checked the silver.

“Wow! Ten silver nyang!”

“…”

That bastard had ten hits coming, guaranteed.

I swallowed the curses rising to my throat and searched for the last remaining person.

*Where is that Cheongpung bastard?*

Unlike Gung Gibang and Hyuk Mujin, who were scooping up silver nyang with all their might, Cheongpung was nowhere to be seen.

But I knew Cheongpung’s habits inside and out, so it did not take long to find him.

“First, ten sweets, please. Oh, and some jeonbyeong too. Not the ones you just picked up—the big ones over there, and make it a generous serving. Wow, thank you! By any chance, where’s the dumpling shop?”

Snap.

As something inside my head broke, I rolled my eyes back and shouted.

“You fucking bastards!”
```
