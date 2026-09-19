<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0492.txt",
      "sha256": "54039acfa838ab3637c45adfc1eadc065496878c957b6173b650f8baff7cf1eb",
      "bytes": 13734
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "042e80223bb5920c34f0731f8d51a860dfb96d082cc6acbe8081dddadfe2ce8f",
      "bytes": 4282
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fe90233ee885e4f922b19d9c6847dee81d495629bd7496b204b45e6dc41ec713",
      "bytes": 156947
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "f18acee32ef3fef48f11676bfa1ed699a94842b77c02cc80bac2ce19b171f4eb",
      "bytes": 918
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "12670b49e264ec137143dceb65d804cb6ded56fc53396422868ddb81e8d9a46f",
      "bytes": 686
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "20662f875e3d70e5b23b3be0cb86204ac8293ea6cc7f71ffade06d16f2d3bc09",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ced1e79436c73de2fa992f458c39f1b8efcca8cccdce1cdf65b6c210cdb50ae5",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "414a948943e64ddc2d75bfe7d3e923650b5ae0a99e094f50ebd7ff448a67f6f8",
      "bytes": 1239
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "73b5448845126ed0c02b8ef74129980df642f7dda522c69c74d16aecc5d20ee4",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fe79ec991bfb9c67b812bd250adbb4bf0f8e8eb7829d45b2904c242cdfb0917c",
      "bytes": 152268
    }
  ],
  "estimated_tokens": 11614
}
-->

# Durable State Update — Chapter 492

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 492. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 492. Profile updates may replace only one
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
  "chapter": 492,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 492,
    "continuity_sources": [492],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon has absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts without forming a formal Master-Disciple relationship and is testing him through successive poisoned traps; Taekyung has survived the first night's traps and has now been affected by Potent Energy-Dispersing Poison.",
    "Jeok has withdrawn from the Water God Dragon expedition and told the group not to seek him until everything is finished.",
    "The Water God Dragon's spirit has departed, but its enormous silver-scaled corpse remains where it last lay after ruling Dongting Lake and the Yangtze for five hundred years."
  ],
  "continuity_sources": [
    491,
    490
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What further poison tests will Mungyeong impose on Taekyung, and what secret martial arts will he teach him?"
  ],
  "safe_through": 491,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig and 한 식경 as half an hour.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무당파    | **Wudang**                       |
| 제갈세가   | **Zhuge Clan**                   |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 레이드     | **raid**              |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 육체파 | **physical school** | Taekyung’s joking self-description. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 운철 | **meteorite iron** | Material whose strength is used as a comparison for the black-wood fishing rod. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |

## Listed compact profiles

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 482
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, was captured alive, and is now severely injured with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 491
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 491
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 491
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 484
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 491
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃492화



당연하다면 당연한 말이지만, 이 많은 사람이 한자리에 모인 이유는 수신룡의 명복을 빌어 주기 위해서가 아니었다.

그리고 그중에서도 특히 사심이 엿보이는 한 사람이 있었다.

“놀랍군, 놀라워.”

은빛 비늘을 어루만지는 제갈풍의 눈빛이 황홀하게 반짝였다.

“이 엄청난 강도, 아름다움. 믿어지지 않아.”

비록 끝끝내 용이 되지 못한 채 죽음을 맞이했으나, 수신룡은 오백 년의 세월을 품은 신령스러운 이무기.

이미 한차례의 전투를 통해 검증된 바 있는 수신룡의 육신은 그 자체로도 강력한 갑옷인 동시에 무기였다.

“이건…… 가치를 매길 수 없는 무가지보(無價之寶)요.”

제갈풍의 말에는 일말의 과장도 없었다.

강철보다 단단한 비늘은 검기로도 완전히 베어 낼 수 없고, 그 안에 숨어 있는 뼈는 비늘보다 더한 강도를 자랑한다.

마법을 이용한 제련술이 발달한 현대에서도 이 정도의 재료는 부르는 게 값이라고 할 정도니, 무림이라면 더 말해 봤자 입만 아픈 수준이다.

‘비록 만년한철(萬年寒鐵)만큼은 아니지만…… 엄청난 보물인 건 확실하지.’

무려 백여 장에 이르는 수신룡의 몸뚱어리는 그런 보물들로 이루어져 있다.

저 비늘로 갑옷을 만든다면 쇠뇌로도 뚫을 수 없을 것이고, 뼈로 무기를 만든다면 운철(隕鐵) 이상의 강도와 예리함을 지닌 병장기가 탄생할 것이다.

무공 비급과 영약, 뛰어난 병장기는 무림인이라면 누구나 환장해 마지않는 세 가지 요소.

제갈풍을 비롯한 몇몇 사람들의 눈에 탐욕이 어리는 것은 당연한 일이었다.

“저걸로 타구봉(打狗棒)을 만든다면…….”

궁기방의 중얼거림에 혁무진이 반박했다.

“무슨 뼈로 타구봉을 만듭니까. 검을 만들어야 제대로죠. 이무기의 뼈로 만든 골검(骨劍)이라, 상상만 해도 끝내주네.”

“너 지금 개방 무시하냐?”

“아뇨. 궁 소협만 무시한 건데요.”

“개처럼 맞아 볼래?”

“어허, 진정하세요. 어차피 저 정도 양이면 타구봉이든 검이든 백 자루는 족히 만들고도 남아돌 텐데 왜 그러십니까.”

“그건 그래. 그럼 우선 타구봉 하나 내 거.”

“저도 검 하나 예약…….”

빡! 빡!

“억!”

“아악!”

사이좋게 뒤통수를 한 대씩 얻어맞은 궁기방과 혁무진이 나를 돌아보며 버럭 외쳤다.

“왜 때려!”

“이유나 설명해 주고 때리십쇼. 제발!”

이 자식들이 아직도 정신 못 차렸네.

눈살을 찌푸린 나는 큼지막한 주먹을 흔들며 으름장을 놓았다.

“싸울 때는 아무것도 못 한 새끼들이 뭐, 타구봉? 검? 예약?”

“아니, 그건…….”

“무인이라면 어쩔 수 없는…….”

“수신룡 아니었으면 이미 호북성은 작살 났어. 물고기 몇 마리 난폭해진 정도로 안 끝났다고.”

수신룡에 의해 숱한 사람이 유명을 달리한 것은 틀림없는 사실이다.

그러나 그것은 자의에 의한 것이 아니었을뿐더러, 게이트가 완전히 열렸다면 호북성에는 한 폭의 지옥도(地獄道)가 펼쳐졌을 것이다.

“물론 사체는 유용하게 쓰이겠지만, 최소한 너희가 사람 새끼들이면 감사하는 마음을 가져라. 응?”

내 일갈에 움찔한 두 녀석이 개미만 한 목소리로 중얼거렸다.

“지는…….”

“솔직히 조장님도 할 말 없죠. 동정어옹을 그 꼴로 만들었는데.”

빡! 빠박!

다시 한번 울려 퍼지는 두 번의 타격음과 두 번의 비명.

나는 재차 머리를 감싸 쥔 궁기방과 혁무진을 향해 윽박질렀다.

“그거랑 이거랑 같냐? 같아? 어?”

이건 나도 억울한 점이 많다.

물론 동정어옹을 작살 낸 건 미안하게 생각하지만, 나로서는 어쩔 수 없는 일이었다.

타락한 수신룡의 피어에 정면으로 노출된 동정어옹 역시 제정신이 아닌 상태에서 사람들을 해쳤고, 당시의 모든 증거가 그를 범인으로 지목하고 있었으니까.

비록 사지가 부러지긴 했어도 목숨을 건진 게 어딘가. 따지고 보면 내게 곤죽이 되도록 두들겨 맞아서 피어에서도 벗어날 수 있었던 거다.

‘주먹이 피어를 이겼다.’

이것이 바로 인간 승리……는 아니고, 서로의 사정이 있었던 거다.

안 그래도 미안해서 병문안도 다녀왔다. 혼절해 있던 상태라 대화를 나누진 못했지만.

“어쨌든 감사하는 마음을 가지라고. 알겠냐?”

내가 두 녀석을 향해 위협적으로 주먹을 흔들던 바로 그때였다.

“진 도우의 말이 맞네.”

듣는 것만으로도 깊은 현기(賢氣)가 느껴지는 목소리. 앞으로 나선 무당파의 현공진인이 착잡한 표정으로 입을 열었다.

“이번 일에 관한 이야기를 들었을 때는 설마 했는데, 이리 보게 되니 알겠네. 참으로 하늘이 내린 신령스러운 영물이로군.”

현공진인과 마찬가지로, 오늘 처음 수신룡을 목격하게 된 진위경도 진중한 표정으로 고개를 끄덕였다.

“진인의 말씀이 백번 옳습니다. 스스로를 희생하여 더 큰 혈풍(血風)을 막았으니, 이 이무기야말로 신룡이라 부를 만한 존재입니다.”

“참으로 안타까운 일이오. 이토록 큰 은혜를 입었으니, 모두가 함께 그의 명복을 빌어 주도록 하는 게 어떻겠소?”

현공진인은 역시 도교의 성지인 무당파에서 깊은 도력을 쌓은 노 도사다웠다.

궁기방이나 혁무진과 같은, 일말의 고마움도 느끼지 못하는 인간 말종들과는 뿌리부터가 다른 것이다.

나는 원시천존에 대한 무한한 신앙심이 솟구치는 것을 느끼며 재빨리 합장했다.

“아멘.”

도교의 법문을 외고 있던 현공진인이 움찔하며 돌아섰다.

“아멘?”

“착각했습니다. 아미타불.”

“……따라 해 보게. 무량수불.”

“아, 죄송합니다. 무량수불.”

“훌륭하군. 원시천존께서 진 도우를 굽어보실 걸세.”

“아, 예.”

무당파에도 전도사가 있나.

종교 승리를 노리는 문명 유저처럼 흐뭇하게 웃어 보인 현공진인이 짧게 법문을 왼 뒤 하늘을 우러러보았다.

“그대, 신령스러운 이무기여. 부디 그곳에서는 창룡이 되어 하늘을 누비길 기원하겠소.”

“아아…….”

“역시 진인이십니다.”

어른의 사정이 있는 제갈풍과 진위경이 열심히 빨아 주자 현공진인이 인자하게 웃으며 대답했다.

“허허. 마땅한 도리를 했을 뿐이오. 그건 그렇고…….”

“예. 진인.”

저 노 도사의 입에서 무슨 현기 어린 말이 흘러나올까.

나를 포함한 모두가 경건하게 고개를 숙인 채 귀를 기울이던 그때였다.

“이제 뜯읍시다.”

“……?”

“그, 할 건 해야 하지 않겠소.”

“……!”

고개를 든 나는 볼 수 있었다.

현공진인의 눈에 이글거리는 병장기에 대한 탐욕과 열망을. 그리고 그의 눈동자로부터 전해지는, 들리지 않는 외침을.

‘나는 송문고검! 송문고검 한 자루 찜!’

이거 도사가 아니라 도라이였네.

잠시나마 믿었던 현공진인의 모습을 보며, 나는 다시 한번 깨달았다.

역시 무림인이란 종자들은 하나 같이 답 없는 새끼들이란 것을.



* * *



레이드가 끝났다고 해서 모든 전투가 끝난 것은 아니다.

레이드만큼이나, 아니 가끔은 그것보다 더 치열하게 싸워야 할 과정이 남아 있다.

‘부산물 분배, 최종 정산.’

결국 헌터도 밥 벌어먹자고 하는 짓이다.

연봉이 수십, 수백억에 달하는 상위 헌터 정도 되면 모를까. 하급 헌터들로 이루어진 레이드 파티에서는 몇만 원짜리 부산물에 얼굴 붉히고 싸우는 일이 부기지수였다. 그래서 계약서가 필수인 거고.

하물며 수신룡의 사체는 그 자체로 막대한 가치를 지닌 보물.

계약서도 작성하지 않은 채 돌입한 레이드였으니 현대였다면 엄청난 분쟁이 일어났을 것이다.

하지만 이곳은 현대가 아닌 무림이고, 이 자리에 있는 이들은 말로 하는 흥정보다는 몸으로 나누는 대화를 선호하는 육체파들이었다.

그리고 나는 이런 사람들을 가리키는 가장 적절한 단어를 알고 있다.

‘호구.’

고개를 돌려 주위를 쓱 훑어보니 죄다 눈치만 보고 있다.

아니, 이 중에서 두 사람은 예외다.

그중 한 사람, 호북 제일의 거부라 할 수 있는 제갈세가의 가주가 가장 먼저 입을 열었다.

“크흠.”

헛기침으로 운을 뗀 제갈풍이 태연하게 말을 이었다.

“이번 사안에 관해서는 본가가 양보할 수밖에 없겠구려. 제갈세가는 일 할만 가져갈 터이니 나머지는 다른 분들께서…….”

“동작 그만. 밑장 빼깁니까.”

“뭣이!”

제갈풍의 말을 자른 내가 피식 웃었다.

“일 할? 얼마나 큰일을 했다고 일 할씩이나 가져가십니까. 그렇게 날로 드시려고 하면 배탈 나요.”

“자, 자네…….”

“제가 틀린 말 했습니까. 제가 아무리 제갈 대협을 존중한다지만 이건 아니죠.”

한 것도 없는 주제에 일 할이라니, 어딜 감히 은근슬쩍 날강도 짓을 하려고.

내 서슬 퍼런 눈빛에 움찔한 제갈풍이 재차 입을 열었다.

“한 것이 없다? 우리 제갈세가가 제공한 정보가 아니었다면 자네는 눈뜬장님이나 다름없었을 터. 틀림없이 여기까지 오지도 못했겠지.”

“혓바닥이 기시군요.”

“흡!”

“그 정보로 도출한 결론이 동정어옹이 범인이다! 아닙니까? 누워 계신 동정어옹께서 벌떡 일어나서 공중제비를 다섯 번 돈 다음 허공답보로 여기까지 뛰어오실 이야기를 하시네.”

“그, 그건…….”

순간 말문이 막힌 제갈풍을 향해, 다른 이들 중 유일하게 여유를 보이고 있던 또 다른 한 사람이 부드럽게 웃어 보였다.

과연, 태원진가를 현재의 위치까지 끌어올린 수완가다운 미소였다.

“제갈 대협. 제 아우의 무례를 대신 사과드립니다.”

“크, 크흠!”

“전부 아우를 잘못 가르친 제 잘못입니다.”

“사실 말이 좀 심하긴 했소.”

“마음이 상하셨을 것 같습니다. 이것 참, 이래서는 안 되는 거였는데.”

“괜찮소. 그래도 소가주와는 말이 통할 것 같으니 다행…….”

“아닙니다. 아주 혼쭐을 내줘야지요. 태경이, 너 이 녀석! 어서 사죄드리지 못할까!”

진위경이 내뱉은 쩌렁쩌렁한 호통에 나는 냉큼 고개를 숙였다.

“죄송합니다. 말이 과했습니다.”

“아무리 제갈 대협께서 날로 먹으려 드셔도 그렇지, 지켜야 할 선이라는 게 있는 것이다!”

“다시 한번 사죄드립니다.”

“아니, 잠깐. 잠깐만. 진 소가주?”

뭔가 이상한 낌새를 느낀 제갈풍이 입을 열었지만, 진위경의 호통은 계속해서 이어졌다.

“태경이 네가 수신룡을 쓰러트리는 데에 가장 큰 역할을 하고! 제갈 대협의 목숨을 구해 준 것이나 다름없지만! 그래도 명가의 가주이시자 무림의 존장이시란 말이다!”

“후우, 죽을죄를 지었습니다.”

“이, 이보시오. 소가주.”

“아무리 버릇없이 자랐다고는 하나, 너 같은 새파란 녀석이 무림에 위명이 쟁쟁하신 제갈 대협을 그런 철면피 취급하다니! 내 본가로 돌아가는 즉시……!”

“소가주우!”

절박하게 부르짖은 제갈풍이 질린 표정으로 손을 내저었다.

“알겠소. 다 알겠으니 모쪼록 신경 좀 써 주시오.”

“음. 그럼 저희 형제의 사과를 받아 주시는 겁니까?”

“죄송합니다. 제갈 대협!”

“아, 알겠다니까. 이제 두 사람 모두 그만합시다.”

“감사합니다. 일 할까지는 아니어도, 제갈세가에는 섭섭지 않게 챙겨 드리지요.”

“개평은 국룰.”

“……후우.”

게임 끝. 요시 그란도 시즌.

순식간에 몸과 마음이 너덜너덜해진 제갈풍이 힘없이 나가떨어지자, 나와 진위경은 흐뭇한 미소를 주고받았다.

머리가 뛰어난 것으로는 죽었다가 깨나도 제갈풍을 따라잡을 수 없겠지만, 이런 종류의 협상은 책상머리에서 배울 수 없다.

‘이게 다 생활의 지혜지.’

정산 과정에서 고블린 독침 하나 더 받겠다고 지랄 발광을 떨던 나와, 살았는지 죽었는지 모를 아버지의 부재로 몇 년간 짬통에서 업무 신공을 익힌 진위경.

이 자리에 있는 사람들이 호구라면 우리는 타짜다.

‘활약한 비중을 봐도 내가 원톱이지.’

싸우는 자가 쟁취하는 법.

이건 물러설 수 없고, 물러서서도 안 되는 싸움이다.

상대가 그 누구라 할지라도 당당히 맞서 싸울 때, 비로소 진정한 헌터이자 무림인이 될 수 있다.

- 일 할. 내놔라. 아니면 목을 내놓든가.

- 드리겠습니다.

하지만 가끔은 예외도 있는 법이다.

……시벌.
```

## Final English reading copy

```markdown
# Chapter 492

It went without saying that the reason so many people had gathered in one place was not to pray for the Water God Dragon’s soul.

And one person in particular was showing rather obvious ulterior motives.

“Incredible. Simply incredible.”

Zhuge Feng’s eyes shone with rapture as he stroked the silver scales.

“This strength. This beauty. It’s unbelievable.”

Although it had died without ever becoming a true dragon, the Water God Dragon was still a divine imugi that had lived through five hundred years.

Its body had already proven itself in battle. It was armor and a weapon all on its own.

“This is… a priceless treasure.”

There wasn’t the slightest exaggeration in Zhuge Feng’s words.

The scales were harder than steel and could not be completely severed even by Sword Energy. The bones hidden beneath them were even harder than the scales.

Even in the modern age, where Magic-powered forging techniques had advanced to an incredible degree, material of this quality would sell for whatever price the owner demanded. In Murim, there was no point saying anything more about it.

*It may not be as valuable as Ten-Thousand-Year Cold Iron, but… it’s definitely an incredible treasure.*

The Water God Dragon’s body stretched for more than a hundred zhang,[^1] and every inch of it was made up of treasures like those.

Armor made from those scales would not be pierced even by a crossbow. A weapon made from its bones would be harder and sharper than one made from meteorite iron.

Martial arts manuals, elixirs, and exceptional weapons—the three things every martial artist went crazy for.

It was only natural that greed would appear in the eyes of Zhuge Feng and several others.

“If we made a Dog-Beating Staff out of that…”

Hyuk Mujin immediately objected to Gung Gibang’s muttering.

“Why would you make a Dog-Beating Staff out of the bones? We should make a proper sword. A Bone Sword made from an imugi’s bones… Just imagining it is incredible.”

“Are you looking down on the Beggars’ Sect?”

“No. I’m only looking down on you, Young Hero Gung.”

“Want me to beat you like a dog?”

“Now, now, calm down. There’s enough material to make at least a hundred Dog-Beating Staffs or swords, so why are you fighting over it?”

“That’s true. Then I’ll claim one Dog-Beating Staff for myself first.”

“I’ll reserve one sword too…”

Crack! Crack!

“Ugh!”

“Argh!”

After each receiving a smack to the back of the head, Gung Gibang and Hyuk Mujin turned toward me and shouted.

“Why’d you hit me?”

“Please explain the reason before hitting us!”

These bastards still hadn’t come to their senses.

I frowned and shook a large fist at them threateningly.

“You two useless bastards couldn’t do a damn thing when we were fighting, and now you’re talking about Dog-Beating Staffs? Swords? Reservations?”

“Well, that’s…”

“A martial artist can’t help it…”

“If the Water God Dragon hadn’t been there, Hubei Province would have been destroyed. It wouldn’t have ended with a few fish going berserk.”

There was no question that countless people had died because of the Water God Dragon.

But it had not been of its own free will. And if the Gate had opened completely, Hubei Province would have become a hellscape.

“Of course, the corpse will be useful. But if you’re even remotely human, you should at least be grateful. Got it?”

The two of them flinched at my shout and muttered in voices as tiny as ants.

“Like you are…”

“Honestly, Captain, you don’t have much room to talk either. You turned the Dongting Fisherman into that.”

Crack! Crack!

Two more blows rang out, followed by two more screams.

I glared at Gung Gibang and Hyuk Mujin, who were clutching their heads again.

“Are those two things the same? Are they? Huh?”

I had plenty of grievances of my own.

Of course, I felt bad about wrecking the Dongting Fisherman, but there had been nothing else I could do.

The Dongting Fisherman had been directly exposed to the corrupted Water God Dragon’s Fear. He had harmed people while out of his mind, and every piece of evidence at the time had pointed to him as the culprit.

Even if his limbs had been broken, at least he was still alive. If you looked at it another way, being beaten into a bloody pulp by me had allowed him to escape the Fear.

*A fist beat Fear.*

That was the triumph of humanity…

No, not really. We had both had our own circumstances.

I had even gone to check on him because I felt bad. He had been unconscious, though, so we hadn’t been able to talk.

“Anyway, be grateful. Understand?”

That was when I was shaking my fist threateningly at the two of them.

“Young Friend Jin is right.”

The voice alone carried profound wisdom. Perfected Being Hyeongong of the Wudang Sect stepped forward and spoke with a grave expression.

“I had my doubts when I heard what happened, but seeing it with my own eyes, I understand now. It truly is a divine creature blessed by the heavens.”

Like Perfected Being Hyeongong, Jin Wikyung was seeing the Water God Dragon for the first time that day. He nodded solemnly.

“Your words are completely correct, Perfected Being. It sacrificed itself to prevent even greater bloodshed. This imugi is worthy of being called a divine dragon.”

“It is truly a tragedy. Since we have received such an enormous grace, would it not be proper for everyone to pray for its soul together?”

Perfected Being Hyeongong was exactly what one would expect from an old Daoist who had cultivated profound Daoist mastery at Wudang, the sacred ground of Daoism.

He was fundamentally different from human garbage like Gung Gibang and Hyuk Mujin, who could not feel even the slightest gratitude.

Feeling an overwhelming faith in the Primordial Heavenly Venerable rise within me, I quickly clasped my hands together.

“Amen.”

Perfected Being Hyeongong, who had been reciting Daoist prayers, flinched and turned around.

“Amen?”

“I was mistaken. Amitabha.”

“……Repeat after me. Infinite Life Buddha.”

“Ah, my apologies. Infinite Life Buddha.”

“Excellent. The Primordial Heavenly Venerable will watch over you, Young Friend Jin.”

“Ah. Yes.”

*Does Wudang have missionaries too?*

Perfected Being Hyeongong smiled contentedly, like a Civilization player aiming for a religious victory. After reciting a short prayer, he looked up at the sky.

“You, divine imugi. I pray that you become an Azure Dragon there and soar across the heavens.”

“Ah…”

“As expected of Perfected Being Hyeongong.”

Zhuge Feng and Jin Wikyung, each with his own vested interests, eagerly sang his praises. Perfected Being Hyeongong answered with a benevolent smile.

“Ho ho. I merely did what was proper. That aside…”

“Yes, Perfected Being?”

Everyone, myself included, bowed their heads reverently and listened, wondering what profound words would come from the old Daoist’s mouth.

That was when he said,

“Now, let’s start taking it apart.”

“……?”

“We still have to do what needs to be done, do we not?”

“……!”

I raised my head and saw it.

The greed and longing for weapons blazing in Perfected Being Hyeongong’s eyes. And, carried through his gaze, a silent cry.

*I call dibs on one Pine-Pattern Ancient Sword! One Pine-Pattern Ancient Sword for me!*

He wasn’t a Daoist. He was a lunatic.

As I stared at Perfected Being Hyeongong, whom I had trusted for one brief moment, I realized something once again.

*Every last one of these Murim people is a hopeless bastard.*

* * *

The end of the raid did not mean the end of all the battles.

There was still a process that had to be fought through just as fiercely as the raid itself—sometimes even more fiercely.

*Distribution of the spoils. Final settlement.*

In the end, Hunters did this to make a living.

The top Hunters, who earned tens or even hundreds of billions a year, might be different. But in raid parties made up of lower-tier Hunters, people constantly got into arguments over byproducts worth only a few tens of thousands of won. That was why contracts were essential.

And the Water God Dragon’s corpse was a treasure of immense value in its own right.

Since we had entered the raid without even drawing up a contract, this would have caused an enormous dispute in the modern world.

But this was Murim, not the modern world. And the people gathered here belonged to the physical school, preferring to negotiate with their bodies rather than with words.

And I knew the most appropriate word for people like that.

*Suckers.*

I turned my head and swept my gaze around. Everyone was watching everyone else, waiting to see who would speak first.

Well, two of them were exceptions.

One of them—the Family Head of the Zhuge Clan, which could be called the richest family in Hubei—spoke first.

“Ahem.”

Zhuge Feng cleared his throat and continued casually.

“Regarding this matter, our family will have no choice but to make a concession. The Zhuge Clan will take only ten percent, and the rest can go to everyone else…”

“Stop right there. Are you dealing from the bottom?”

“What!”

I cut him off and gave a quiet laugh.

“Ten percent? What did you do that was worth ten percent? If you try to swallow that much for free, you’ll get a stomachache.”

“You…”

“Am I wrong? I may respect you, Sir Zhuge, but this isn’t right.”

*Ten percent, when he didn’t do a damn thing? How dare he try to sneak in and rob us blind?*

Zhuge Feng flinched under my icy stare, then opened his mouth again.

“Didn’t do anything? If not for the information provided by the Zhuge Clan, you would have been blind even with your eyes open. You certainly would not have made it this far.”

“You have quite a long tongue.”

“Ghk!”

“The conclusion you reached from that information was that the Dongting Fisherman was the culprit. Wasn’t it? You’re telling me that the Dongting Fisherman, lying there injured, suddenly got up, did five somersaults, and then used Stepping on Empty Air to hop all the way here?”

“That, that was…”

Zhuge Feng was momentarily rendered speechless. Then the only other person present who looked completely relaxed smiled gently.

It was the smile of a man whose skill had elevated the Jin Family of Taiyuan to its current position.

“Sir Zhuge, allow me to apologize on behalf of my little brother for his rudeness.”

“C-Cough!”

“It is entirely my fault for teaching my little brother so poorly.”

“His words were rather harsh.”

“I imagine they hurt your feelings. This is really unacceptable of him.”

“It’s all right. At least the Lesser Family Head seems reasonable, so that’s a relief…”

“Not at all. I really must give him a proper scolding. Taekyung, you little rascal! Apologize this instant!”

At Jin Wikyung’s booming shout, I immediately bowed my head.

“I apologize. I spoke too harshly.”

“Even if Sir Zhuge was trying to get something for free, there are still certain lines one must not cross!”

“I apologize once again.”

“No, wait. Hold on. Lesser Family Head Jin?”

Zhuge Feng seemed to sense that something was wrong and opened his mouth, but Jin Wikyung continued shouting.

“Taekyung played the greatest role in defeating the Water God Dragon! He practically saved Sir Zhuge’s life! But you are still the Family Head of a great clan and a respected elder of Murim!”

“Whew. I have committed a crime worthy of death.”

“Wait, Lesser Family Head.”

“Even if you were raised without proper manners, how dare a green youngster like you treat Sir Zhuge, whose reputation resounds throughout Murim, like some shameless bastard! As soon as we return to our family, I will…”

“Lesser Family Head Jiiin!”

Zhuge Feng desperately called out to him and waved his hand with a weary expression.

“All right. I understand. I understand everything, so please take care of me in the settlement.”

“Then you accept our brothers’ apology?”

“I’m sorry, Sir Zhuge!”

“Yes, yes, I understand. Now both of you, stop.”

“Thank you. Even if it isn’t ten percent, we’ll make sure the Zhuge Clan receives a fair share.”

“Even the loser gets a cut. That’s the universal rule.”

“……Whew.”

*Game over. Jackpot.*

Zhuge Feng was reduced to a limp wreck in the blink of an eye. Jin Wikyung and I exchanged satisfied smiles.

No matter how many times I died and came back to life, I could never catch up to Zhuge Feng in sheer intelligence. But this sort of negotiation could not be learned at a desk.

*This is the wisdom of everyday life.*

I had once thrown a fit to get one extra goblin poison dart during a settlement. Jin Wikyung, meanwhile, had spent years mastering the divine art of getting work done in the family’s shit-pile because no one knew whether his father was alive or dead.

If everyone here was a sucker, we were cardsharps.

*And judging by our contributions, I was obviously the top performer.*

Those who fight claim the spoils.

This was a battle from which we could not retreat—and should not retreat.

Only by standing proudly against our opponents, whoever they might be, could we become true Hunters and true martial artists.

—Ten percent. Hand it over. Or hand over your neck.

—We’ll hand it over.

But sometimes there were exceptions.

…Fuck.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
```
