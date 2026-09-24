<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0978.txt",
      "sha256": "ec34ec0441baed6e6a2f8c5663253cc847f9de89191cc6fa268da1e19e3982c5",
      "bytes": 12469
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1f0b464cf6901914cdee909dcf570e4191a66722750997efe6a06009547afd6b",
      "bytes": 1291
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d1fe4cfd1987a3a20bd18a3c812c2ef5974aff3847aa6c3869c67d59aa5b3e86",
      "bytes": 235771
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1f06527f8623b3b1d63f4de80e5c10170ac41a8717eb2dd40f3c3e877885ba52",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "7bd4cc2ed2caa4eebd009d0115bf9fdcd61beeca3173eb7499f8f6a22e8e6d44",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e2456283c9a3d0f01f7481cf2961c12727da9d0a60dd311409c67d200d5f10d7",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2a39b870eb03017bf0762d386146f1e3bcf6e4d8fc76f16e53b2444fa42b6e2e",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "27cfab8e31f057bc15a0df8a7e883ae5bb1fa6a4f0eab93cf97c520eb6818b3c",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e2c6eaf3736fc8349ec2d4fa9128c680894e94f97fa8aeaf00f748771092eca3",
      "bytes": 271349
    }
  ],
  "estimated_tokens": 10428
}
-->

# Durable State Update — Chapter 978

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
1 and safe_through 978. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 978. Profile updates may replace only one
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
  "chapter": 978,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 978,
    "continuity_sources": [978],
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
    "Murong Baek, the North Heaven Demon Lord, burns his innate qi in the fight against Taekyung, Jeok Cheongang, and the Bow Saint, knowing it will lead to his death.",
    "Murong Baek says the Lord of Heaven has awakened, the war has begun, and at most half a year remains.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Hebei Peng Family’s fate against the pill-enhanced Keshiks remains unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    976,
    977
  ],
  "open_questions": [
    "What happens to Murong Baek in the confrontation after he burns his innate qi?",
    "What does the Lord of Heaven intend, and how will the war unfold?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 977,
  "temporary_decisions": [
    "Render Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 모용백 | 자무카 | commander_to_subordinate | you | plain and authoritative | Murong Baek gives Jamukha direct orders and rebukes him without honorific speech. |
| 자무카 | 모용백 | subordinate_to_commander_and_savior | you | deferential and honorific | Jamukha thanks Murong and addresses him with honorific speech. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |
| 북천마군 | 적천강 | former battlefield adversaries | Fire King | calm and familiar | Addresses Jeok Cheongang as 화왕 while asking him not to rush. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 977
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 977
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 977
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 977
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 977
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃978화



어느 날부터인가 가끔, 변해 버린 나를 발견하고는 한다.

매 순간 목숨을 걸어야만 하는 이 지긋지긋한 사투 속에서, 이해할 수 없는 한 줄기 환희를 느끼며 나아가는 내 모습을.

“진태경-!”

사자후(師子吼)와도 같은 일갈이 귓가를 후려친다.

거칠게 휘몰아치는 바람 너머, 북천마군의 손끝에서 터져 나온 혈광을 향해 백염을 내리그었다.

서걱!

창날의 궤적을 따라 두 줄기로 갈라지는 거대한 장력(掌力).

목표를 벗어나 좌우에 늘어선 암벽을 뒤흔드는 엄청난 충격과 폭발음을 뒤로한 채, 다시 한번 지면을 밟았다.

팟.

응당 터져 나와야 할 염화일로(炎火一路)의 불꽃은 없다.

살성의 가르침이 녹아든 발끝은 그 어느 때보다 가벼웠고, 쾌속하게 내쏘아지는 신형은 섬광과도 같았다.

마치, 저 멀리 맞은편에서 불현듯 들이닥친 빛줄기처럼.

슈확!

압축된 공기가 찢겨 나간다. 소리마저 앞질러 다가온 빛의 화살을 향해, 북천마군은 분노와 공력이 들끓는 일권(一拳)을 휘둘렀다.

꽈아아앙!

접촉. 그리고 폭발.

부풀어 오르는 아득한 섬광 속, 나는 궁성이 쏘아 보낸 빛줄기가 검붉은 혈광에 스러지는 광경을 똑똑히 볼 수 있었다.

그 빈틈을 놓치지 않고 어느새 코앞까지 다가온 내 모습을 비치고 있는 북천마군의 두 눈동자도.

‘보인다.’

순간 세상이 느려졌다.

주위를 둘러싼 모든 것이 또렷하고 생생했다.

무어라 말하려는 듯, 느릿하게 달싹이는 입술도.

이제는 흰자위를 찾아볼 수 없을 만큼 붉어진 눈동자도.

그리고 내가 전력을 다해 내뻗은 창날을 가로막는, 한껏 응축된 수강(手罡)도.

콰드드득!

서로 다른 두 갈래의 강기가 부딪친다. 허공에서 맞닿은 청백색의 화염과 검붉은 어둠이 뒤섞여 거센 힘의 파동을 뿜어냈다.

“고작. 이 정도로.”

토막토막 끊어지는 음성.

한 손으로 창날을 움켜쥔 채 나를 노려보는 북천마군의 눈동자에서 시뻘건 화염이 줄기줄기 쏟아지는 듯했다.

“나를, 이 모용백을 쓰러트릴 수 있으리라 생각했더냐!”

치지지지직!

들불처럼 일어난 미증유의 기운이 창날에 실린 화염을 억누른다. 북천마군이 생명마저 불태워 가며 얻은 그 힘은, 이미 예정된 죽음에 대한 대가는 높고도 거대했다.

자무카를 처치하며 모든 피로와 부상이 완전히 회복된 상황에서도 승리를 떠올릴 수 없을 만큼.

하지만…….

‘그래, 이 정도는 해 줘야지.’

나는 웃었다.

지금 북천마군에게서 느껴지는 힘의 크기는, 내가 충분히 예상했던 범주 안에 있었으니까.

그리고 섬광과도 같은 속도로 등 뒤에서 짓 쳐드는 누군가의 기운은, 북천마군이 지닌 그것과 비견될 만큼 거대했으니까.

‘지금.’

그 어떤 경고의 외침이나, 전음도 없었다.

그러나 안다. 그도, 나도.

비록 시야에 보이지 않더라도, 우리는 서로를 너무나도 잘 알고 있었다.

그렇기에 일말의 두려움이나 망설임 없이, 뇌리에 떠오른 그대로 움직일 수 있었다.

스륵.

창대를 놓으며 신형을 반쯤 돌려세운 그 순간.

거한(巨漢)이라 불리기에 조금도 손색이 없는 내 체구에 가려져 보이지 않았던, 한 줄기의 화염이 내 빈자리를 채우며 터져 나왔다.

고오옹.

전설 속 화룡(火龍)이 뿜어내는 숨결처럼, 새하얀 백색의 겁화가 어둠을 아득하게 밝혔다.

새벽 공기에 스며 있던 이슬을 살라 먹고, 증발시키며 북천마군을 향해 들이닥쳤다.

화. 왕.

자그맣게 달싹이는 입술이 소리 없는 외침을 토해 낸다. 뜨거운 열기로 달아오른 놈의 눈동자가 방향을 잃은 채 흔들렸다.

숨길 수 없는 혼동과 두려움.

그리고 북천마군이 본능적으로 내비친 그 감정은, 나나 적천강이 아닌 또 다른 누군가의 등장을 의미했다.

슈확!

북천마군의 등 뒤, 부드럽게 휘어진 두 자루의 곡도가 아름다운 궤적을 그렸다.

거칠 것 없이 정면에서 들이닥친 폭급한 화염과는 정반대의, 그러나 그에 못지않게 치명적인 기운이 실린 일격.

“……!”

느려진 세상 속, 북천마군의 눈동자가 부릅떠졌다.

정면에는 적천강의 멸염신권(滅炎神拳)이, 후방에는 형태를 뒤바꾼 궁성의 쌍도(雙刀)가 내리그어지는 상황.

회피할 시간도, 회피할 수도 없는 두 초절정 고수의 가공할 합공(合攻)이 펼쳐진 순간. 놈에게 더 이상의 선택권은 주어지지 않았다.

쾅! 콰아아아아!

일순간, 협곡에 드리웠던 모든 어둠이 걷혔다.

시뻘건 혈광(血光)이 북천마군의 전신을 휘감은 채 터져 나왔다.

드드드득!

세상이 뒤흔들린다. 거칠 것 없는 힘의 파도가 사방을 휩쓸었고 세 사람의 발끝에서 지면이 붕괴했다.

콰득! 쩌저적!

엄청난 압력을 이기지 못하고 거미줄처럼 갈라지는 지면.

마지막 순간 내가 그러했듯, 신형을 비틀어 방향을 뒤바꾼 북천마군의 전신이 태풍을 만난 나무처럼 거세게 떨렸다.

한 손으로 적천강의 일권을, 다른 손으로는 궁성이 펼쳐 낸 두 자루의 곡도를 움켜쥔 놈의 얼굴은 악귀처럼 일그러져 있었다.

‘아니, 이미 악귀였지. 오래전부터.’

제아무리 긴 세월 동안 인두겁을 뒤집어쓰고 있었다고 한들, 괴물의 본질마저 사라지지는 않는 법.

북천마군은, 모용백은 돌아올 수 없는 강을 건넜다.

저마다의 사정과 이유로 마(魔)를 좇아 어딘가로 향했던, 수많은 괴물처럼.

콰득, 푸화악!

조금씩 베이고, 바스라지는 살과 뼈마디 사이로 핏물이 솟구친다.

북천마군은 상상한 적 없던 고통을 느끼고 경련하고 있었다.

화왕과 궁성. 두 초절정 고수를 막아서고 있는 놈의 양손은 지금 이 순간에도 서서히 제 형태를 잃어 가고 있었다.

그럼에도 단 하나, 마지막까지 변함없을 것은 원독(怨毒)으로 가득한 저 눈동자뿐일 것이다.

“어째서, 어째서……!”

피가 흐를 만큼 악문 잇새로 씹어 내뱉는 듯한 북천마군의 목소리에 실린 고통과 증오를 나는 온전히 느낄 수 있었다.

서서히 다가오는 내 모습에 미처 숨기지 못한, 한 줄기의 두려움까지도.

“나는, 죽지, 않는다.”

헐떡이는 숨결을 따라 끊어져 나온 북천마군의 음성에, 적천강이 담담한 얼굴로 대꾸했다.

“누구나 죽기 마련이지. 사람도, 괴물도.”

온 세상을 집어삼킬 것 같던 혈광(血光)도, 사방을 짓누르던 기파도 이제는 찾아볼 수 없다.

비록 아직은 남아 있다 해도, 바람 앞의 등불처럼 사그라지고 있을 뿐이다.

그그극.

한 손으로는 결코 감당할 수 없는 압력.

적천강이 나직한 대답과 함께 전력을 다해 끌어낸 백색 겁화 앞에서, 북천마군은 마침내 한쪽 무릎을 꿇었다.

쿠웅!

지면이 깊게 파였다. 터질 듯이 눈을 부릅뜬 북천마군의 귓가로 궁성의 음성이 전해졌다.

“한 사람의 인간으로 태어나, 스스로의 판단으로 내린 선택에 정답은 없다. 다만…… 이것이 네 선택에 대한 결과일 뿐.”

정답이 있는 삶이 어디 있겠나.

인생은 객관식도 아니다. 주관식이나 서술형으로 점수가 매겨지는 시험 따위도 아니다.

어떤 삶을 살아왔더라도, 돌이켜보면 단 한 점의 후회라도 남는 것이 바로 인간의 삶이다.

그러나 판단도 결과도 자신의 몫이며, 단지 그뿐이다.

“이룡신창(螭龍神槍) 모용백. 아니, 북천마군. 이제 네 선택의 결과를 받아들일 때다.”

무림인의 별호에는 그만한 이유와 시간이 있다.

그렇기에 궁성의 입술 사이로 흘러나온 낯선 별호를 들었을 때, 나는 모용백이 살아온 삶을 어렴풋이 알 것 같다는 생각이 들었다.

이룡(螭龍).

용이 되지 못한 이무기.

그와 동시에 누구보다 용이 되고 싶었던 이무기.

아마도 그래서였을 것이다.

놈이 여의주를 얻기 위해 그토록 몸부림쳤던 것은.

창천을 훨훨 누비는 한 마리의 용으로 거듭나고자, 합리화를 위한 온갖 변명과 이유를 찾아 암천(暗天)의 그늘 아래에 머무른 것은.

하지만 아는 것과 이해하는 것은 다르다.

그리고 설령 놈이 직접 말한 모든 이야기가 사실이라 해도 나는 모용백을, 북천마군을 평생 이해하지 못할 것이다.

아니, 이해하지 않을 것이다.

놈을 이해하는 그 날, 나 역시 저 깊고 어두컴컴한 강 건너에 존재하는 괴물이 되어 버릴 테니까.

“마지막으로, 이것만 알고 가라.”

나는 나직한 음성과 함께 손을 뻗었다.

북천마군이 적천강과 궁성에 맞서기 위해 놓을 수밖에 없었던, 새하얀 창 자루가 빨려 들어가듯 손아귀에 붙잡혔다.

“세상 모든 사람이, 다 너와 같은 선택을 하는 건 아니라는 거.”

약자는 도태되고 강자는 살아남는다.

이 세상은 늘, 언제나, 항상 그래 왔다.

약육강식의 법칙은 비단 무림뿐만이 아니라 현대에도 존재했고, 앞으로도 그럴 터였다.

비단 창칼이 아니라 다른 어떤 수단으로도.

그러나 그들 모두가 도태되는 것이 두려워 북천마군과 같은 선택을 한다면, 세상은 이미 지옥도(地獄道)가 되었을 것이다.

최소한의 도리와 인의도 없는.

오직 서로를 잡아먹고 잡아먹히는 목적에 의해, 끝없는 연장선을 이어 가는 끔찍한 세상.

하지만 모든 이가 북천마군과 같지 않기에, 나는 이 세상이 아직 살 만하다고 생각한다.

동시에 믿는다.

밤하늘에 흩뿌려진 별처럼 수많은 이들 중, 어느 별 볼 일 없는 F급 헌터에게 이토록 불가사의한 힘을 내려 준 누군가 역시 그런 마음일 것이라고.

“이제, 가라.”

나는 대답을 기다리지 않았다.

그저 묵묵히, 단호하게 청백색의 화염에 휩싸인 창날을 찔러넣었다.

마지막 순간에조차 포기하지 않고, 체내에 남아 있는 모든 생명력을 불태우며 몸부림치고 있는 북천마군을 향해.

단순히 자신의 소중한 것을 지키기 위해서가 아니라, 남의 것을 빼앗아 부풀리기 위해 살아왔던 괴물의 가슴을 향해.

푸욱.

이글거리는 화염이, 살과 뼈를 관통했다.



* * *



마치 누군가 촛불을 켠 듯, 어둠 속의 존재는 불현듯 눈을 떴다.

얼마나 잠들어 있던 것일까.

모든 것이 혼잡하게 뒤섞인 그 심연 같은 꿈속에서, 얼마나 오랜 시간이 흐른 것일까.

알 수 없었다.

익숙한 의문인 동시에, 매번 같은 결론이었다.

어둠 속의 존재에게는 늘 그랬다.

그가 간혹 잠에서 깨어날 때마다 세상은 언제나 달라져 있었으니까.

장장 수십여 년간을 잠들어 있던 적도 있으니 두말해서 무엇하랴.

다만 세월이 흐를수록 짧아지는 그 주기 속에서, 어둠 속의 존재는 조금씩 깨닫고 있었다.

영원히 닿을 수 없을 것처럼 생각했던 그 날이, 어느덧 자신의 코앞으로 성큼 다가왔다는 것을.

화아아악.

서늘한 바람이 주위를 휩쓸었다. 이내 광풍(狂風)이 되어 휘몰아쳤다.

짙은 어둠 속을 희미하게 밝히고 있는 횃불을 꺼트리고, 땅과 지붕을 뒤흔들었다.

그리고 고요한 호수에 격랑이 일어난 듯한 그 급격한 변화는, 어둠 속 존재가 자신이 눈을 뜬 이유를 깨달았다는 증거이기도 했다.

북천(北天).

네 번째 하늘이 무너졌다. 또 하나의 충실한 종이 사라졌다.

하지만 곧 천하의 모두가 놀라게 될 그 사실 앞에서, 어둠 속 존재는 홀로 웃고 있었다.
```

## Final English reading copy

```markdown
# Chapter 978

Every now and then, I find myself realizing that I’ve changed.

In the middle of this miserable fight, where I have to risk my life every moment, I keep moving forward with an inexplicable joy in my heart.

“Jin Taekyung!”

A shout like a lion’s roar lashed at my ears.

Beyond the wind whipping around me, I brought White Flame down on the blood-red light bursting from the North Heaven Demon Lord’s fingertips.

*Shhk!*

The enormous Palm Force split in two along the path of my spearhead.

Leaving behind the tremendous impact and explosion as the deflected Palm Force shook the cliffs on either side, I planted my foot on the ground once more.

*Tap.*

The flames that should have burst forth from Flamefire Path were nowhere to be seen.

The tips of my feet, infused with the Slaughter Saint’s teachings, felt lighter than ever, and my body shot forward at such speed it was like a flash of light.

Like a beam that had suddenly struck from far across the gorge.

*Shwaaa!*

Compressed air tore apart. The North Heaven Demon Lord swung a fist, seething with rage and internal energy, at the arrow of light that had overtaken even sound and closed in.

*BOOOOM!*

Contact. Then an explosion.

Within the distant, swelling flash of light, I saw it clearly: the beam the Bow Saint had shot fading beneath the dark red glow.

And I saw the North Heaven Demon Lord’s eyes, reflecting my figure as I closed in, already right in front of him, without missing that opening.

*I can see it.*

The world slowed in an instant.

Everything around me was sharp and vivid.

His lips moving slowly, as though he were trying to say something.

His eyes, so red there wasn’t a trace of white left in them.

And the condensed Palm Force blocking the spearhead I had thrust forward with all my might.

*Krrrk!*

Two different Forces collided. The blue-white flames meeting in midair mingled with the dark red shadows and sent out a powerful wave of force.

“Just… this much.”

His voice came in broken fragments.

The North Heaven Demon Lord glared at me, gripping my spearhead in one hand. Streams of blazing red seemed to pour from his eyes.

“Did you think you could defeat me—Murong Baek—with this?”

*Zzzzzzt!*

An unprecedented energy flared up like a wildfire, pressing down on the flames carried by my spearhead. The power the North Heaven Demon Lord had gained by burning even his own life came at a steep and tremendous price: a death already set in stone.

Even though all my fatigue and injuries had completely healed after I took down Jamukha, I still couldn’t imagine victory.

But…

*Yeah. This is about what I expected.*

I smiled.

The strength I sensed from the North Heaven Demon Lord was within the range I’d expected.

And the energy crashing down from behind me at a speed like a flash of light was just as immense as his.

*Now.*

There had been no shouted warning, no Sound Transmission.

But I knew. He knew, too.

Even if we couldn’t see each other, we knew each other too well.

So, without the slightest fear or hesitation, we moved as the thought flashed through our minds.

*Slip.*

The instant I let go of the spear shaft and turned halfway around—

A streak of flame, hidden behind my body—a frame massive enough to be called a giant—filled the space I’d left and exploded.

*Gooooong.*

Like the breath of a fire dragon from legend, pure white hellfire blazed across the darkness.

It burned away the dew lingering in the dawn air, vaporizing it as it rushed toward the North Heaven Demon Lord.

Fire. King.

His lips moved ever so slightly, forming a soundless cry. His eyes, heated by the scorching air, wavered, losing their focus.

Confusion and fear he couldn’t hide.

And those emotions instinctively showing on the North Heaven Demon Lord’s face meant that someone else had appeared—not me or Jeok Cheongang.

*Shwaaa!*

Behind the North Heaven Demon Lord, two gently curved blades traced a beautiful arc.

The strike carried an energy every bit as deadly as the furious flames crashing straight at him, though utterly different in nature.

“……!”

In the slowed world, the North Heaven Demon Lord’s eyes flew wide.

Jeok Cheongang’s Flame-Extinguishing Divine Fist was coming from the front. From behind, the Bow Saint’s two curved blades—whose shape had changed—were coming down on him.

Two Supreme Peak masters unleashed a terrifying combined attack, leaving him neither time nor room to dodge. He had no choice left.

*BOOM! KAAAAAABOOM!*

In an instant, all the darkness that had covered the gorge lifted.

A blood-red glow burst out, wrapping around the North Heaven Demon Lord’s entire body.

*Krrrrrk!*

The world shook. A relentless wave of force swept in every direction, and the ground crumbled beneath the three combatants.

*Crack! Krrrk!*

The ground split like a spiderweb, unable to withstand the tremendous pressure.

As I had done at the last moment, the North Heaven Demon Lord twisted his body and changed direction. His whole frame shuddered violently like a tree caught in a typhoon.

His face twisted like a Fiend’s as he caught Jeok Cheongang’s fist in one hand and the Bow Saint’s two curved blades in the other.

*No. He was already a Fiend. Had been for a long time.*

No matter how many years a monster spent wearing a human face, its nature didn’t disappear.

The North Heaven Demon Lord—Murong Baek—had crossed a river from which there was no return.

Like so many other monsters who had pursued the Demonic Path for their own reasons, heading off somewhere beyond it.

*Crack—splatter!*

Blood gushed from the flesh and joints of bone, slowly being cut and crushed.

The North Heaven Demon Lord convulsed with pain the likes of which he’d never imagined.

Both his hands, holding off the Fire King and the Bow Saint, were slowly losing their shape even now.

And yet there was one thing that would remain unchanged until the very end: those eyes filled with bitter hatred.

“Why? Why…?”

I could feel all the pain and hatred in the North Heaven Demon Lord’s voice, as if he were grinding the words out through clenched teeth hard enough to draw blood.

And I could feel the sliver of fear he couldn’t quite hide as I slowly approached.

“I… won’t… die.”

The North Heaven Demon Lord’s words broke apart with his gasping breaths. Jeok Cheongang answered, his expression calm.

“Everyone dies. People and monsters alike.”

The blood-red light that seemed about to devour the whole world and the force that had been pressing down on everything around us were nowhere to be seen now.

Even if some remained, they were fading like a lamp before the wind.

*Krrrk.*

The pressure was more than one hand could withstand.

Before the white hellfire Jeok Cheongang drew forth with all his strength, alongside his quiet reply, the North Heaven Demon Lord finally dropped to one knee.

*BOOM!*

The ground caved in deeply. The Bow Saint’s voice reached the North Heaven Demon Lord, his eyes bulging as if they might burst.

“A person is born human, and makes choices by their own judgment. There is no right answer. This is simply… the consequence of your choice.”

What life has a right answer?

Life isn’t multiple choice. It isn’t some test graded with short answers or essays, either.

Whatever life a person has lived, looking back, there will always be at least one thing they regret. That is what human life is.

But both the judgment and the consequences are your own. That’s all.

“Murong Baek, the Divine Spear of the Imugi. No—the North Heaven Demon Lord. It’s time to accept the consequence of your choice.”

There’s a reason and a history behind every martial artist’s sobriquet.

So when I heard the unfamiliar one slip from the Bow Saint’s lips, I had a vague sense that I understood the life Murong Baek had lived.

The imugi.

An imugi that never became a dragon.

And at the same time, an imugi that had wanted to become a dragon more than anyone.

Maybe that was why.

Why he had struggled so desperately to obtain the dragon pearl.

Why he’d remained in the shadow of Dark Heaven, searching for every excuse and justification he could find, all so he could become a dragon soaring freely through the azure heaven.

But knowing something and understanding it are different.

And even if every story he’d told us himself was true, I would never understand Murong Baek, the North Heaven Demon Lord.

No. I would refuse to understand him.

The day I understood him would be the day I became a monster, too, one of those existing across the dark, deep river.

“Before you go, remember this.”

With a quiet voice, I reached out.

The pure white spear shaft the North Heaven Demon Lord had been forced to let go of to face Jeok Cheongang and the Bow Saint flew into my grip as though drawn there.

“Not everyone in the world makes the same choices you did.”

The weak are cast aside, and the strong survive.

That’s how this world has always been—always, without fail.

The law of the jungle existed not just in Murim, but in the modern world, too. And it would continue to exist.

Even if people used other means instead of spears and swords.

But if everyone made the same choice as the North Heaven Demon Lord out of fear of being cast aside, the world would already have become a hellscape.

A place without even the barest sense of decency or benevolence.

A terrible world, endlessly perpetuating itself through one purpose alone: devouring one another, and being devoured.

But not everyone is like the North Heaven Demon Lord. That’s why I think this world is still worth living in.

And I believe, too—

That among the countless people scattered like stars across the night sky, whoever gave such inexplicable power to an unremarkable F-rank Hunter must feel the same way.

“Now, go.”

I didn’t wait for an answer.

I simply thrust my spearhead, wreathed in blue-white flames, into him—quietly and without hesitation.

Into the North Heaven Demon Lord, who was still struggling, refusing to give up even at the last moment, burning every bit of life left in his body.

Into the chest of a monster who had lived not merely to protect what was precious to him, but to seize and hoard what belonged to others.

*Thud.*

The blazing flames pierced through flesh and bone.



* * *



As if someone had lit a candle, the being in the darkness suddenly opened its eyes.

How long had it been asleep?

How much time had passed in that abyssal dream where everything had become a jumble?

It didn’t know.

The question was familiar, and the conclusion was always the same.

It had always been that way for the being in the darkness.

Whenever it woke from time to time, the world had always changed.

It had once slept for decades. What more was there to say?

But as the intervals grew shorter with the passing years, the being in the darkness was gradually beginning to realize:

The day it had thought it would never reach had, at some point, drawn right up to its doorstep.

*Fwoooosh.*

A cold wind swept through the area. Soon, it became a raging gale.

It put out the torches faintly illuminating the thick darkness and shook the ground and roof.

And that sudden change, like a raging current rising in a tranquil lake, was also proof that the being in the darkness had realized why it had opened its eyes.

North Heaven.

The fourth heaven had fallen. Another faithful servant had disappeared.

But as the being in the darkness faced the fact that would soon shock everyone beneath the heavens, it smiled alone.
```
