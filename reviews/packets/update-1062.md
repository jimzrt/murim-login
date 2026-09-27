<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1062.txt",
      "sha256": "c4ed6e1c639dfc92ee9e6840fc49d0cea60d990fa0f003f44cba958063828b06",
      "bytes": 13115
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b98a57f70f0b9479bf8d26548036527e299407e3875b10872baed7e1a71501f8",
      "bytes": 1729
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ba8a51e8512e970aa0d87a116444a581b678a3f337dbb5038bccedbde58a2ec",
      "bytes": 241486
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "23d1da2ae112eda60b71c7ca216b34555eb507a442aee458e1eb1c8ab6700943",
      "bytes": 928
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e1435c8221ab5640032c076e6b004db38959845f4b45ec906279a4ce5feea2fc",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b1257a6d556d6760db66456da9cdf2cdeca6baa4f94834cccedcfac4d20735f8",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "887c6336a45d5b9b6b49b3396195afad63cfb3f8d86213e3a3bc697335aee69c",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ff07e0e507688706b705c2683beb2bfdd1cd66284e9949d06538aed4c935e386",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "627d0a0347322bba02e6cbb5483636d223d28ac58b364888742f47ba1f248efe",
      "bytes": 283094
    }
  ],
  "estimated_tokens": 11001
}
-->

# Durable State Update — Chapter 1062

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1062. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1062. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1062,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1062,
    "continuity_sources": [1062],
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
    "Great Sir is a Level 119 master whose name changes; the System most recently displayed Gaettong, but his identity remains unknown.",
    "Hyeoncheon spared Sama Pyo after wounding him shallowly and said the Kongtong Sect would pursue revenge without punishing relatives for their kinship.",
    "Taekyung stopped Taishan from charging Sama Pyo by knocking him unconscious; some Kongtong survivors remain unaccounted for.",
    "The Great Sir sheltered and treated Hyeoncheon and the Kongtong Disciples after their flight from Dunhuang.",
    "The Seven Masters of Baekma Bang returned with thousands of horse-caravan riders, helping the Kongtong group return to Gansu and striking a decisive blow against the faltering enemy.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown.",
    "A mysterious green light remains in the dispersing darkness."
  ],
  "continuity_sources": [
    1060,
    1061
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where are the remaining Kongtong Sect survivors?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?",
    "Who is Great Sir, and why does the name he uses change?"
  ],
  "safe_through": 1061,
  "temporary_decisions": [
    "Render 대인 as “Great Sir” for the mounted bandits’ address.",
    "Render 미친놈 as “Madman” when Great Sir adopts it as a name; render 소똥이 as “Sottong” with the gloss “Cow Poop.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 만리추행 | **Myriad-Mile Pursuit** | Epithet of the Beggars' Sect Leader and master of movement techniques. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 숭산결의 | **Mount Song Resolution** | The event marking the formal gathering of the Murim Alliance at Mount Song. |
| 황하 | **Yellow River** | River along which civilization began. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 개똥이 | **Gaettong** | One of the names the Lord has used for himself, according to the Seven Masters. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 녕하 | **Ningxia** | Place name; origin of the mounted bandits mentioned by Sima Gong. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 점순이 | **Jeomsuni** | One of the names Ma Junggeol recalls Great Sir using. |
| 소똥이 | **Sottong** | One of the names Ma Junggeol recalls; gloss as “Cow Poop.” |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1061
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1061
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1061
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1061
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1062화




제아무리 평탄한 인생을 살다 간다고 한들, 사람이라면 일생을 통틀어 최소 한 번쯤은 특정 부류의 미친놈을 만나기 마련이다.

더군다나 객관적으로 보아도 상당히, 아니 매우 험난하고 굴곡진 인생을 살아온 나로서는 두말할 필요조차 없다.

하지만 장담컨대.

그런 나조차도 대인(大人)이라 불리는 저 괴인만큼 순수한 의미로 미친 사람은 본 적이 없었다.

‘……이쯤 되면 미친놈 도감이라도 만들어야 하나.’

나는 내심 중얼거리며 조금씩 멀어져 가는 대인의 뒤통수를 바라보았다.

개똥이라는 이름으로도 자신의 완전한 정체성을 찾지 못한 그는, 소와 말까지 두루 섭렵하며 기어코 똥 시리즈 삼부작을 완성.

직후 곧장 점순이로 성별 전환까지 시도하다가 적천강의 살해 협박을 받은 끝에 마방(馬房)들의 손에 끌려 격리조치 되고 있었다.

“노부의 모든 것을 걸고 말하는데…….”

나와 어깨를 나란히 한 채, 마찬가지로 대인의 뒷모습을 지켜보던 적천강이 침중한 목소리로 말을 이었다.

“저놈은 둘 중 하나다. 고도의 훈련을 받은 암천의 간자(間者)거나, 혹은 미쳐도 아주 단단히 미친놈이거나.”

자세한 사정을 아는 이들이라면 누구나 무심코 고개를 끄덕일만한 예측이었지만, 나는 별다른 망설임 없이 대답했다.

“글쎄요, 간자는 아닐 겁니다.”

“저놈이 녕하성의 마방들을 이끌고 아군을 도운 것은 사실이나, 완전히 믿는 것은 금물이다. 네 녀석도 익히 알고 있지 않느냐?”

물론이다. 뒤통수라면 이골이 날 정도로 얻어맞았으니까.

태원진가의 대장로를 시작으로 오대세가의 일익을 담당하고 있던 모용세가까지 암천과 손잡았던 마당에, 어디서 굴러먹다 왔는지 모를 정체불명의 초절정 고수를 무작정 신뢰하는 건 멍청한 짓이다.

하지만…….

“못 믿을 것도 없죠. 충분한 근거가 있다면.”

“근거?”

적천강의 반문에, 나는 미세하게 입술을 달싹였다.

- 시스템.

귓가에 닿는 짤막한 전음(傳音)에 일순간 크게 뜨이는 두 눈동자.

이 세상에서는 생소한 시스템이라는 세 글자가 무엇을 뜻하는지, 이미 내게 들은 이야기를 통해 알고 있던 적천강이 낮게 가라앉은 목소리로 입을 열었다.

“그래서, 네 녀석의 그 잘난 능력으로 파악한 바에 의하면 어떠하냐.”

“미친 사람입니다. 그것도 아주 제대로 미친.”

“즉, 간자는 아니다?”

“예. 완전히 단언할 수는 없지만요.”

“굳이 수치로 말한다면?”

“구 할 구 푼 구 리. 물론 저 미친. 아니, 대인이 간자가 아닐 확률을 말하는 겁니다.”

“대인은 무슨, 그냥 정신 나간 놈이지.”

슬쩍 눈살을 찌푸린 적천강이 입맛을 다셨다.

“여하간 어울리지 않게 매사에 의심부터 하고 보는 네 녀석이 그리 말할 정도면 사실상 확신하고 있다는 뜻인데…… 그럼 저놈이 진정 광증(狂症)을 앓고 있다고 보느냐?”

나는 잠시 망설였지만, 이내 고개를 끄덕였다.

사실 대부분의 시스템을 전반적으로 꿰뚫고 있다고 생각했던 나로서도 처음 겪는 일이라 백 퍼센트 확신할 수는 없으나, 그것이 아니고서야 시시각각 뒤바뀌는 대인의 이름을 설명할 길이 없었다.

‘적어도 거짓말은 아니다. 어떤 수를 쓰더라도 시스템을 속이는 건 사실상 불가능해.’

그러니 결국 답은 하나뿐이다.

개똥이건, 소똥이 말똥이 점순이건.

대인은 스스로를 그런 존재라고 굳게 믿었고, 시스템은 이를 고스란히 반영했다.

고로 그는 아주 순수한 의미에서 미친 사람이었다.

“만리추행(萬里追行), 그 왕초 거지 놈도 울고 갈 행색을 하고 있어서 그렇지 아직 노환에 걸릴 나이는 아닌 것 같고…… 도대체 어디서 굴러먹다 온 개뼈다귀인지 감도 안 잡히는군.”

천하의 개방 방주를 왕초 거지로 간단히 격하시켜 버린 적천강은 미간을 찌푸렸지만, 그로서도 당장 대인의 정체를 유추하는 것은 불가능에 가까울 것이다.

이 광활한 구주팔황(九州八荒)과 사해오호(四海五湖)에는 아직도 드러나지 않은 이들이 너무나도 많으니까.

속세와 동떨어진 심산유곡의 기인들, 스스로 잊히기를 택한 비밀 문파의 후인들.

혹은 세상 어디에선가 숨죽인 채 은밀히 살아가고 있을 도망자와 살인자들까지.

당장 눈앞의 적천강 역시 환갑 무렵까지 구화산(九華山)에 틀어박혀 무공 수련에만 매진하고 있었으니, 대인 역시 그와 같은 부류일 가능성 또한 충분했다.

‘실제로 숭산결의(嵩山決意)를 통해 무림맹이 새롭게 창설된 이후부터는 적지 않은 수의 은거 고수들이 입맹하기도 했었고.’

물론 그들은 대인과는 달리 충분한 검증 과정을 거쳤을 것이다. 무림맹이 무슨 대학교 동아리도 아니고, 지금은 온갖 배신과 흉계가 난무하는 전시 상황이니까.

하지만 뭐랄까.

그 순간 불현듯 찾아온 어떠한 확신이, 이내 목소리가 되어 입술 사이를 비집고 흘러나왔다.

“이대로 아군으로 받아들이죠.”

“뭐라?”

“앞서 말씀드렸듯이 대인은 암천의 간자는 아닌 것 같습니다. 아니, 확실히 아니에요.”

평소와 달리 굳건한 확신이 담긴 음성에, 적천강이 의외라는 듯한 눈빛으로 나를 응시했다.

“거참, 희한한 일이로군. 무엇이 너로 하여금 이토록 저 수상쩍은 미친놈을 신뢰하게 만든 것이냐?”

“그건…….”

나는 대답 대신 말꼬리를 흐렸다.

글쎄, 사실 잘 모르겠다.

시스템이 적아(敵我)까지 구분해 주지는 않았으니까.

그러나 대인을 향한 궁금증과 더불어, 이상하리만치 묘한 확신이 들었다.

저 정체불명의 초절정 고수가 결코 적이 아닐 것이라는, 나로서도 도통 근거를 제시할 수 없는 확신이.

‘……피로 때문인가.’

잠시 잊고 있던 사실을 인지한 순간, 나는 문득 흔들리는 시야를 느끼며 주위를 둘러보았다.

한나절에 걸친 전투로 인해 무수한 피와 시체로 뒤덮인 설원.

아주 잠시 찾아왔던 승리의 기쁨도 잊은 채 전장을 수습하는 사람들과 어느샌가 새카맣게 몰려와 허공을 배회하고 있는 날짐승들.

먹구름에 가려진 하늘은 어둡고, 그 아래 펼쳐진 땅은 온통 붉다.

흔들리는 시야에 담긴 그 세상은, 마치 앞으로도 영원히 반복될 미래처럼 느껴졌다.

“우리가…… 정말 이긴 게 맞습니까?”

흐릿하게 흘러나온 목소리에, 적천강이 대답했다.

“그래. 적어도 오늘만큼은.”

하지만 왜일까.

어째서일까.

일일이 셀 수도 없는 적을 쓰러트리고, 수많은 목숨을 구하고, 마침내 대승을 거두어 감숙성을 지켜 냈음에도.

지금 이렇게 살아 숨 쉬고 있음에도.

도무지 이긴 것 같지가 않았다.

조금도, 기쁘지 않았다.

지금 이 순간, 내 귓가에 울려 퍼지는 맑은 종소리를 들으면서도.

띠링, 띠링, 띠링.



- 퀘스트 조건이 충족되었습니다.

- 임무 : 감숙성 일대의 모든 적 섬멸(완료).

- 퀘스트, [피의 길]을 성공적으로 완료하셨습니다.

- 막대한 경험치와 명성을 획득하셨습니다.




새로운 연계 퀘스트가 생성되었습니다.

변경된 정보를 확인하시겠습니까?

Y  /  N



나는 문득 고개를 들었다.

반투명한 홀로그램 창 너머로 보이는 하늘은 여전히 새카만 먹구름에 가려져 있었고, 심호흡과 함께 몸속 깊숙이 스며드는 공기는 피비린내로 가득했다.

과연 나는, 언제쯤 이 광경에서 해방될 수 있을까.

얼마나 더 많은 고난을 겪고, 죽음을 지켜봐야 이 끔찍한 굴레에서 벗어날 수 있을까.

하지만 언제나 그렇듯이, 나는 대답할 수밖에 없었다.

‘수락.’

빌어먹게도 잔인한 하루였다.



* * *



우둑, 까드드득.

잘게 흔들리는 흐릿한 촛불 너머, 섬뜩한 파육음과 함께 몸부림치는 그림자를 말없이 주시하는 두 눈동자가 있었다.

언뜻 보기에는 속내를 짐작할 수 없을 만큼 깊게 가라앉아 있으나, 그럼에도 일말의 경멸과 혐오가 담긴 그 눈빛은 파육음이 그치고 난 후에도 여전했다.

조금씩 잦아드는 경련 속, 마침내 몸을 일으킨 그림자가 대뜸 불쾌감을 표시할 만큼.

“썅년이. 눈깔하고는.”

오랜만에 건네는 첫인사치고는 거칠었지만, 여인은 크게 신경 쓰지 않았다.

그녀는 늘 스스로를 이성적인 사람이라 자부해 왔고, 한낱 짐승에게서 인간으로서의 예의를 기대하는 것이 매우 어려운 일이라는 사실을 알고 있었으니까.

물론, 설령 그렇다고 한들 고운 말이 나갈 수는 없었다.

“몸이나 닦아. 역겨운 냄새 풍기지 말고.”

“뭐? 역겨워?”

여인의 날 선 음성에, 뭐라 대답하려던 그림자가 문득 피식 실소를 흘렸다.

“그래, 분부대로 하지. 가뜩이나 심사가 불편하실 텐데. 안 그런가?”

“……또 무슨 헛소리를.”

“어울리지도 않게 모른 척은. 그러지 마. 괜히 추해 보이니까.”

스륵.

매끄러운 근육과 살결을 스치는 천.

촛불이 미치지 않는 어둠 속에서 전신 곳곳에 묻은 핏물을 닦아 낸 그림자가 한 마디를 툭 내뱉었다.

“열화신룡(烈火神龍) 진태경.”

“……!”

“전해 듣기로는 거의 실패 직전까지 갔다던데…… 어때, 이 빌어먹을 계집아. 지난번에는 그렇게 비웃더니, 막상 직접 겪어 보니 쉽지 않지?”

여인, 대술사는 조용히 입술을 깨물었다.

그도 그럴 것이, 그녀로서도 별다른 반박의 여지가 없는 사실이었으니까.

그리고 쉽사리 끝나지 않는 대술사의 침묵에, 크게 소리 내어 웃은 그림자가 재차 말을 이었다.

“훨씬 더 신중했어야지. 네년이 뒈지는 거야 뭐 상관없지만, 하마터면 대계(大計)에 큰 지장이 갈 뻔했으니까.”

계속되는 비아냥에 미간을 좁힌 대술사가 대꾸했다.

“그건 당신도 마찬가지야.”

“글쎄, 그때와 비교하기에는 너무 부끄럽지 않나? 나는 고작해야 머저리 몇몇으로 중원 한복판에서 피바람을 일으켰는데, 이건 실눈을 뜨고 봐도 경우가 다르지.”

저벅.

놀리듯이 낄낄 웃은 그림자, 아니 혈주(血主)가 흐릿한 불빛 아래로 모습을 드러내며 덧붙였다.

“거기에 더해서, 중요한 물건까지 챙겨야 했고.”

온 천하를 뒤흔들었던 소림혈사(少林血史) 이후, 두 번 다시 모습을 드러내지 않았던 그는 경쾌한 발걸음으로 넓은 공간을 가로질렀다.

그리고 족히 수백 여년은 될 법한 기나긴 세월의 흔적과 알 수 없는 위압감이 느껴지는 태사의에 앉아, 비스듬히 턱을 괸 채 대술사를 바라보았다.

마치, 자신이 일국의 군주라도 된 것처럼.

“흠. 뭐 지난 얘기는 여기까지 하자고. 중요한 건 과거가 아니라 현재고 미래니까. 안 그래?”

이번에는 대술사가 실소를 흘릴 차례였다.

고개를 절레절레 흔든 그녀는 태사의에 앉은 혈주를 응시했다.

“꼭 뭐라도 되는 것처럼 얘기하지 마. 넌 멍청한 짐승, 아니 괴물이나 다름없으니까.”

“괴물이라, 어차피 중원 놈들이 보기에는 피차일반 아닌가?”

“달라. 함께 그분을 모신다는 공통점이 있을 뿐. 우리 중 그 누구도 네놈과 같을 수는 없지.”

그러나 경멸이 담긴 음성에도, 혈주는 아무렇지 않게 어깨를 으쓱해 보였다.

“맞아. 처음으로 옳은 말을 하는군.”

“……뭐?”

예상했던 것과는 전혀 다른 반응에 대술사가 당황하던 그때, 피처럼 진한 미소가 혈주의 입가에 떠올랐다.

“당연히 같을 수는 없지. 네년을 포함한 그 누구도, 나만큼의 전공을 세운 적은 없었을 테니까.”

그는 즐겁게 웃으며 태사의를 쓰다듬었다.

정확히는 태사의의 일부에 용사비등한 필체로 음각된, 곤륜(崑崙)이라는 두 글자를.

휘우우우.

굽이진 산봉우리를 스치며 휘몰아친 눈바람이 두 남녀가 서로를 마주한 그곳, 태청전(太淸殿)으로 스며들고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1062

No matter how smooth a life someone might lead, every person was bound to meet at least one particular kind of madman in their lifetime.

And as someone who’d lived an objectively—no, an extremely—rough and tumultuous life, I didn’t even need to say more.

But I could say this with certainty.

Even I had never met anyone quite so purely insane as that oddball they called Great Sir.

*…At this rate, should I start a whole encyclopedia of madmen?*

I muttered to myself as I watched Great Sir’s back slowly recede into the distance.

Unable to find his true identity even under the name Gaettong, he’d tried Cow Poop and Horse Poop too, completing his trilogy of poop names.

Then he’d immediately tried to change genders and become Jeomsuni, only to receive death threats from Jeok Cheongang and end up dragged away by the horse caravans for containment.

“I swear on everything I have…”

Standing shoulder to shoulder with me, Jeok Cheongang watched Great Sir’s retreating figure, too. His voice was grave as he continued.

“That man is one of two things: either a Dark Heaven spy who’s undergone intense training, or a man who’s completely and utterly insane.”

Anyone who knew the details would have nodded along without thinking. But I answered without the slightest hesitation.

“I doubt he’s a spy.”

“It’s true that he led the horse caravans of Ningxia Province to help our side. But we mustn’t trust him completely. You know that as well as I do, don’t you?”

Of course. I’d been hit in the back enough times to be sick of it.

The Head Elder of the Jin Family of Taiyuan had joined forces with Dark Heaven. Even the Murong Family, one of the Five Great Families, had done the same. It would be stupid to trust some unidentified Supreme Peak master who’d crawled out of who-knows-where.

But…

“There’s no reason we can’t trust him. Not if there’s enough evidence.”

“Evidence?”

At Jeok Cheongang’s question, my lips barely moved.

—System.

A brief Sound Transmission reached his ear. His eyes widened for an instant.

Jeok Cheongang already knew what the unfamiliar word *System* meant in this world, from what I’d told him before. His voice sank low as he spoke.

“So, according to that impressive ability of yours, what did you find?”

“He’s a madman. A complete and utter madman.”

“So he isn’t a spy?”

“Yes. I can’t say that with absolute certainty, though.”

“If you had to put a number on it?”

“Ninety-nine point nine percent. Of course, I mean the odds that that madman—no, Great Sir—isn’t a spy.”

“Don’t call him Great Sir. He’s just a lunatic.”

Jeok Cheongang frowned slightly and clicked his tongue.

“Anyway, you’re not one to trust people easily. If you’re saying this much, then you’re practically certain… So you think he genuinely suffers from madness?”

I hesitated briefly, then nodded.

Even I, who thought I had a pretty good grasp of most of the System, had never encountered anything like this. I couldn’t be a hundred percent sure, but otherwise, there was no explaining why Great Sir’s name kept changing from one moment to the next.

*At least he isn’t lying. No matter what you did, it’d be practically impossible to fool the System.*

So there was only one answer.

Whether he was Gaettong, Sottong, Malttong, or Jeomsuni—

Great Sir firmly believed he was each of those people, and the System reflected that belief without alteration.

Which meant that, in the purest sense of the word, he was insane.

“Great Sir looks so ragged even Myriad-Mile Pursuit, that king of beggars, would weep, but he doesn’t seem old enough to be suffering from infirmities of old age… I can’t even guess where that stray mutt crawled out of.”

Jeok Cheongang had casually demoted the Beggars’ Sect Leader, a man who ruled over the whole world’s Beggars’ Sect, to a mere king of beggars. He frowned, but even he would have found it nearly impossible to work out Great Sir’s identity right then and there.

There were still far too many people hidden away across the vast Nine Provinces and Eight Wastes, the Four Seas and Five Lakes.

Eccentrics living in remote mountain valleys far from the world. Heirs to secret sects who had chosen to let themselves be forgotten.

Or fugitives and killers living quietly, out of sight, somewhere in the world.

Jeok Cheongang himself had shut himself away on Mount Jiuhua until he was nearly sixty, devoting himself solely to martial arts. There was every chance Great Sir belonged to the same sort.

*In fact, ever since the Murim Alliance was newly founded through the Mount Song Resolution, quite a few reclusive masters had joined.*

Of course, unlike Great Sir, they must have gone through proper vetting. The Murim Alliance wasn’t some college club, and this was wartime, with betrayal and intrigue everywhere.

But how should I put it?

A conviction that came to me out of nowhere slipped between my lips as a voice.

“Let’s accept him as one of our own.”

“What?”

“As I said before, Great Sir doesn’t seem to be a spy for Dark Heaven. No—I’m sure he isn’t.”

Jeok Cheongang looked at me with surprise. My voice was firmer than usual.

“Well, now. That’s strange. What makes you trust that suspicious madman so much?”

“That’s…”

Instead of answering, I let the words trail off.

I wasn’t sure, to be honest.

The System didn’t distinguish between friend and foe.

Still, along with my curiosity about Great Sir, I felt a strangely powerful conviction.

The unidentifiable Supreme Peak master wasn’t our enemy. I couldn’t offer a single reason for believing it.

*…Maybe it’s the exhaustion.*

The moment I recognized something I’d briefly forgotten, I suddenly noticed my vision wavering and looked around.

A snowy field covered in countless bodies and blood after half a day of fighting.

People clearing the battlefield, having already forgotten the brief joy of victory. Birds of prey had gathered in a black mass, circling overhead.

The sky, hidden behind dark clouds, was dim. The land beneath it was red all over.

The world caught in my wavering vision felt like a future that would repeat itself forever.

“Did we… really win?”

At my faint, uncertain voice, Jeok Cheongang answered.

“Yes. At least for today.”

But why?

How come?

We’d defeated more enemies than I could count, saved countless lives, and won a great victory that had finally secured Gansu Province.

And yet, even now, with breath still in my lungs—

It didn’t feel like we’d won.

I wasn’t happy at all.

Not even as a clear chime rang in my ears right then.

*Ding, ding, ding.*

> **System**
> Quest conditions have been met.
>
> **Mission:** Eliminate all enemies in the Gansu Province area (**Complete**).
>
> Quest **Path of Blood** successfully completed.
>
> You have acquired a massive amount of EXP and Fame.
>
> A new chain Quest has been created.
>
> Would you like to check the updated information?
>
> Y / N

I suddenly lifted my head.

Beyond the translucent holographic window, the sky remained hidden behind pitch-black clouds. The air that filled my lungs with a deep breath reeked of blood.

When would I finally be free of this sight?

How much more suffering would I have to endure, how many more deaths would I have to witness, before I could escape this horrible cycle?

But as always, I had no choice but to answer.

*Accept.*

It had been a cruel fucking day.

* * *

Crack. Crunch.

Beyond the faintly trembling candlelight, two eyes silently watched a writhing shadow, accompanied by a gruesome sound of flesh tearing.

At first glance, the eyes seemed so deeply sunk that it was impossible to guess what lay behind them. Even so, they held a trace of contempt and disgust—and that look remained even after the tearing sounds stopped.

The shadow’s convulsions slowly subsided. At last, it rose—and immediately showed its displeasure.

“You bitch. What’s with that look?”

It was a rough way to greet someone after such a long time, but the woman paid it little mind.

She had always prided herself on being a rational person, and she knew how difficult it was to expect a mere beast to show the courtesy of a human being.

Of course, that didn’t mean she could speak kindly to it.

“Wipe yourself off. And stop stinking up the place.”

“What? I stink?”

At the woman’s sharp words, the shadow had started to reply—but suddenly let out a quiet laugh.

“Fine. I’ll do as I’m told. You’re in a bad mood as it is. Aren’t you?”

“…What nonsense are you talking about now?”

“Don’t pretend you don’t know when it doesn’t suit you. Don’t. It makes you look pathetic.”

*Swish.*

Cloth slid over smooth muscle and skin.

In the darkness beyond the candlelight, the shadow wiped the blood from its body and tossed out a few words.

“Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

“I heard you nearly failed… So, how was it, you miserable bitch? You mocked me last time, but it wasn’t so easy when you had to face him yourself, was it?”

The Grand Mage silently bit her lip.

She had little room to argue. It was the truth.

When the Grand Mage’s silence showed no sign of ending, the shadow laughed out loud and continued.

“You should’ve been much more careful. I don’t care if you die, but you nearly caused a serious setback to the grand plan.”

The Grand Mage frowned at the continuing taunts and shot back.

“You’re no different.”

“Hardly comparable to what happened then, is it? I caused a bloodbath in the heart of the Central Plains with only a handful of idiots. Even with one eye half-closed, anyone can see this was a different situation.”

*Step.*

The shadow—no, the Blood Lord—chuckled as if to mock her, then stepped into the faint light.

“And on top of that, I had to retrieve an important item.”

After the Shaolin Bloodshed, which had shaken the whole world, he had never appeared again. Now he crossed the spacious room with a jaunty stride.

He sat in the grand chair, which bore the marks of centuries of age and carried an imposing presence of its own. Resting his chin on one hand, he gazed at the Grand Mage.

Like a king on his throne.

“Well. Enough about the past. The important thing is the present and the future. Isn’t that right?”

This time, it was the Grand Mage’s turn to let out a quiet laugh.

She shook her head and stared at the Blood Lord sitting in the grand chair.

“Don’t talk as if you’re somebody. You’re nothing more than a stupid beast—or a monster.”

“A monster, huh? To the people of the Central Plains, aren’t we as bad as each other?”

“No. The only thing we have in common is that we serve that person. None of us can be like you.”

But even at her contemptuous words, the Blood Lord merely shrugged.

“Right. That’s the first thing you’ve said that’s correct.”

“…What?”

The Grand Mage was taken aback by the response, which was nothing like what she’d expected. A smile, deep as blood, spread across the Blood Lord’s lips.

“Of course none of you can be like me. No one, including you, has ever accomplished as much as I have.”

He laughed gleefully and stroked the grand chair.

More precisely, he stroked the two characters carved into part of it in a bold, vigorous hand.

**Kunlun.**

A whirling snowstorm swept past the jagged mountain peaks and crept into the Taiqing Hall, where the two of them faced each other.
```
