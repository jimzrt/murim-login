<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0918.txt",
      "sha256": "b5262fa7232f9454606273255214a598562709e09a697febb2205e63e5a04ffa",
      "bytes": 13156
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "12c549e7bce348b5802b6004259f47283426273c40f6f304fb5fb0c905885a48",
      "bytes": 1001
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a63b515f2e07963dba92df6716e73fd64a70a72b09948dfecf483064a6fd7b86",
      "bytes": 231549
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5578768bc95e06b40bfe487c229347ca22aa5a3a13a09bfc389e9c8e008ddfa6",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "d8134ac014170a97232cf2bc385450968065d5723fe8a2610486b327641e24a8",
      "bytes": 731
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "9f074121ee22221a9c942916e8e63f4068b2020e4593a1b81e550a15a69415f4",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a313578d479de43a0d495b2ee9b1c2b18a5da5b83f16c9aa34405a2017aedab9",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6b6515703f916c5144335b57223397cc2d3ddae4335e3c35c6e0e005cf446964",
      "bytes": 1429
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a51c67e64ba55333c9b3736720a89742e307afb9ccc2be9a88e1b0ffe9aad71e",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "26d27df51adc908650a0f3ca4d7f3739b99f0dd2e53b65a9e6c66549a8594f19",
      "bytes": 264815
    }
  ],
  "estimated_tokens": 11027
}
-->

# Durable State Update — Chapter 918

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
1 and safe_through 918. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 918. Profile updates may replace only one
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
  "chapter": 918,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 918,
    "continuity_sources": [918],
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
    "Jin Taekyung is critically injured after saving Jeok Cheongang and appeals to the System; a chime sounds in response.",
    "Jeok Cheongang has pushed beyond his prior limits and is close to defeating the Eastern Heaven Demon Lord.",
    "The Eastern Heaven Demon Lord has lost both arms and a leg, but summons Heaven's Slaughter as a last resort.",
    "A flaming spear interrupts Heaven's Slaughter's attack on Jeok Cheongang; its wielder is not yet identified."
  ],
  "continuity_sources": [
    916,
    917
  ],
  "open_questions": [
    "What does the System’s chime signal, and will it help Taekyung survive?",
    "Can Jeok Cheongang defeat the Eastern Heaven Demon Lord despite Heaven's Slaughter's intervention?",
    "Who threw the flaming spear?",
    "What is So Gyo’s identity and allegiance?"
  ],
  "safe_through": 917,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 살기     | **killing intent**                               |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 대라신선 | **Great Firmament Immortal** | Legendary immortal invoked by Mungyeong as unable to stop the dragon's death. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 은영술 | **concealment techniques** | Stealth arts associated with ninjas. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 천살 | **Heaven's Slaughter** | Name or title used when the Eastern Heaven Demon Lord summons the assassin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 천살 | summoner_to_assassin | Heaven's Slaughter | controlled, familiar command | The Eastern Heaven Demon Lord calls him out as a concealed last resort. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 917
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 917
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a being no longer human, a former Maoshan Sect disciple who commands the dead with a bell.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 910
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 917
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 916
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao, whom Taekyung killed, has been raised among the Eastern Heaven Demon Lord’s undead, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 916
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃918화



솨악!

느려진 세상 속, 한 자루의 비수와 함께 섬광처럼 내리꽂히는 노인의 모습에 동천마군은 직감했다.

‘끝났다.’

그만큼 완벽한 암습이었다.

제아무리 지금의 화왕 적천강이라고 해도 피할 수 없는, 아니 그 어느 때보다 평정심을 잃고 분노한 상태이기에 더더욱 피할 수 없을 일격.

설령 운 좋게 이 공격을 막거나 피하여 죽음을 모면한다 하더라도, 중상은 피할 수 없다는 것이 동천마군의 판단이었다.

그가 천살(天殺)이라 칭한 저 절름발이 노인은, 바로 그 살성과도 비견할 수 있는 중원 최고의 살수 중 한 명이었으니까.

‘황제를 위해 숨겨 둔 검이었건만.’

원통스럽지만 어쩔 수 없었다.

이미 대계(大計)는 수포로 돌아가기 직전.

지금은 살아남는 것이 우선이었다.

앞으로 얼마만큼의 시간이 더 걸리더라도, 무슨 수를 쓰든 복수는 자신의 손으로 끝내야 했으니.

저주받은 핏줄을 이어받은 황가가 몰살당하는 광경을 이 두 눈으로 똑똑히 지켜보고, 비명에 간 스승과 사형제들을 위해 제를 올리기 전까지는 죽을 수 없었다.

그러나 언제 다시 돌아올지 모르는 복수를 시작하기 위해서는 눈앞에 들이닥친 괴물부터 쓰러트려야 했다.

화왕 적천강.

광활한 평원을 휩쓰는 화마(火魔)처럼 미친 듯이 날뛰는 저 괴물을.

‘죽어라.’

동천마군은 확신했다. 동시에 간절히 바랐다.

그리고 노인의 손에 들린 비수가, 잿가루를 발라 빛을 죽인 검신에 실린 강기가 적천강을 베어 가르려던 그 순간.

쐐애애액, 퍼엉!

어디선가 울려 퍼진 파공성이 동천마군의 귓가에 닿았다.

모든 소음을 차단하며 광포하게 헤집었다.

부릅떠진 동천마군의 두 눈동자가, 그의 시야가 소리보다 먼저 목적지에 도달한 청백색 섬광으로 물들었다.

‘이건.’

어디에서나 볼 수 있는, 흔해 빠진 형태의 창 한 자루.

그러나 그것에 실린 빛은 하늘 위의 태양만큼이나 눈 부셨고, 태양보다도 뜨거운 열기는 공기마저 불사르며 나아갔다.

적천강을 향해.

아니, 정확히는 그의 머리 위로 떨어져 내리던 노인을 향해.

“……!”

“……!”

“……!”

그 순간 모두의 움직임이, 그들이 바라보는 세상이 멈췄다.

불현듯 나타난 살수의 존재를 뒤늦게 알아차린 적천강도, 그런 그를 향해 벼락처럼 내리꽂히던 노인도, 그리고 이 모든 광경을 지켜보던 동천마군 역시도.

슈확!

모두가 느릿하게 바람을 가르며 다가오는 창날을 보았다. 창날을 휘감은 청백색 화염에 깃든 힘을 느꼈다.

동시에 깨달았다.

이 창의 주인이 누구인지.

저 끔찍하리만치 강렬한 열양지기가 어떤 뿌리를 지녔는지.

그리고 불현듯 떠오른 이름 석 자가 그들의 뇌리에서 완성되기도 전에, 공간을 지우며 쇄도한 창날은 찰나의 시간을 넘어 목적지에 도달해 있었다.

절체절명의 순간, 황급히 비수의 방향을 틀어 코앞까지 들이닥친 창날을 가로막은 노인을 향해.

후웅, 콰아아아아앙!

비수에서 솟구친 강기와 맞닿은 청백색의 화염이 부풀어 오른다. 천지를 떨어 울리는 굉음과 여파가 사방을 후려쳤다.

콰가가강!

지진이라도 난 것처럼 뒤흔들리는 땅과 미친 듯이 휘몰아치는 바람.

오직 잿가루로 가득한 그 먹먹한 세상 속에서, 동천마군은 마침내 머릿속에서 완성된 한 사람의 이름을 비명처럼 부르짖었다.

“진태경!”

그 순간.

화아아악.

희뿌옇던 세상이 좌우로 갈라졌다.

그 어느 때보다 가볍고 쾌속한 움직임으로 다가온, 머리부터 발끝까지 붉은 피를 뒤집어쓴 혈인(血人)이 새하얀 이를 드러내며 웃었다.

“이름 부르지 마. 정들어.”

그리고 석상처럼 굳은 채 널브러져 있는 동천마군의 발치에서, 넋 나간 얼굴로 우두커니 서 있는 한 사람을 향해 어깨를 으쓱해 보였다.

“이 새끼 이거 아직 정신 못 차린 것 같은데, 이참에 혀도 뽑을까요?”

“…….”

“노야?”

화왕 적천강은, 늙은 스승은 대답하지 않았다.

아니, 대답하지 못했다.

그는 여느 때와 다름없이 돌아온 제자의 모습을 말없이 바라보다가, 이내 크게 소리 내어 웃었다.

어찌나 즐거웠던지 눈물까지 흘려 가며.

동시에 지금껏 전신을 지배하고 있던 모든 분노와 슬픔이 와르르 무너져 내리는 것을 느끼며, 제자의 팔을 힘주어 움켜잡았다.

“고맙다.”

꾸욱.

“이렇게, 이렇게 돌아와 줘서.”

“……!”

피로 말라붙어 있던 혈인의, 아니 진태경의 눈꼬리가 파르르 떨렸다.

고맙다. 돌아와 주어서.

짧은 한마디였지만 그것만으로도 충분했다.

팔을 통해 전해지는 온기, 한 음절 한 음절에 스며들어 있는 스승의 진심을 오롯이 느낄 수 있었다.

그 마음이, 더할 나위 없었다.

그렇기에 더 이상의 대화는 필요하지 않았다.

열화문의 명맥을 이은 두 사내가 나누게 될 이 짧은 이별의 해후(邂逅)는, 곧 적들의 죽음이 될 테니까.

그것이야말로 지난 삼백 년간 열화문이 살아남은 방식이요, 알 수 없는 연으로 사제지간이 된 그들의 방식이었다.

‘막아서는 모든 것을, 부수고 불태운다.’

그것이 무엇이든.

반드시. 기필코.

저벅.

스승과 제자는 동시에 걸음을 옮겼다. 아직 가라앉지 않은 먼지구름과 잿가루 너머로 은밀히 다가온 끈적한 살기(殺氣)가 그들을 휘감았다.

쉬이이익!



* * *



절름발이 노인, 천살(天殺)은 어둠에 녹아든 채 조용히 때를 기다렸다.

불과 십여 장도 떨어지지 않은 거리에서 죽어 나가는 자신의 수하들을 지켜보면서도, 차갑게 가라앉은 그의 눈동자에서는 일말의 동요도 찾아볼 수 없었다.

쉭, 서걱!

재를 발라 빛을 죽인 검신이 목표를 향해 나아가기도 전에 솟구치는 목.

이 광경을 본 이들은 믿지 못할 것이다.

허수아비처럼 쓰러지는 저들 한 사람 한 사람이, 최소 삼십 년을 공들여 키워 낸 특급 살수들이라는 것을.

‘저 아이들과 함께라면, 삼성(三星)도 능히 해치울 수 있으리라 자신했거늘.’

아니, 실제로 가능했을지도 모른다.

그만큼 조금 전 시도했던 그의 암습은 완벽했다. 화왕 적천강이라는 거인을 직접 이 세상에서 지워 버릴 수도 있었다.

난데없이 찾아온 불청객이 아니었다면.

‘열화신룡 진태경.’

천살은 자신도 모르게 흘러나오려는 침음성을 삼켰다.

성공을 코앞에 두고 있던 마지막 순간, 강대한 기운이 깃든 창을 튕겨 내느라 부러진 손목이 욱신거렸기 때문만은 아니었다.

‘진짜 괴물은…… 스승이 아니었군.’

어둠 속에서 똑똑히 보았다.

회복 불능의 부상을 입고 쓰러지던 진태경의 모습을. 내장 조각이 섞인 핏물을 토해 내며 삶의 끝자락에서 꿈틀거리던 죽음의 그림자를.

‘한데, 그런 상황에서 도대체 어떻게?’

죽음을 벗 삼아 강호를 종횡하는 이들이 바로 무림인이다. 그리고 그중에서도 가장 죽음에 가까운 것이 살수다.

그렇기에 천살은 누구보다 잘 알고 있었다.

그는 살수로 길러지던 아주 어린 시절부터 제 손으로 직접, 온갖 방법을 동원해서 누군가를 죽여 왔고 그 업보로 죽음의 문턱까지 도달한 적도 있었으니까.

‘암천의 도움이 아니었다면, 노부는 이미 오래전에 한 줌 흙으로 돌아갔겠지.’

천살이 살아남은 것은 기적과도 같은 일이었지만, 그마저도 조금 전 진태경이 보여 준 것에 비하면 턱없이 부족하게 느껴졌다.

틀림없다. 강기는 정확히 가슴을 관통했다.

살과 뼈를 갈랐고, 혈도를 부숨과 동시에 오장육부까지 스며들어 그 내부마저 갈가리 찢어 놓았다.

이는 설령 대라신선(大羅神仙)의 보살핌이 있거나, 염라대왕이 직접 명부(冥府)에서 이름을 지운다 해도 회복할 수 없는 부상이다.

한데 그랬던 진태경이 살아 돌아왔다.

비록 전신에 핏물을 뒤집어쓴 혈인의 모습이었으나 정작 겉으로 드러난 살갗은 매끈했고, 천무지체로 알려졌을 만큼 완벽한 근골도 확인했다.

뿐인가.

불과 약관을 갓 넘은 나이라고는 믿을 수 없는, 수 갑자에 달하는 막강한 공력 역시 언제 그랬냐는 듯 채워져 있었다.

마치 빈 찻잔에 물을 채워 넣은 것처럼.

이것이 당연하다는 듯이.

‘이건…… 설명할 수 없는 무언가다.’

그야말로 상리(常理)를 초월한 능력.

깊게 가라앉아 있던 천살의 눈동자가 가늘게 떨렸다.

지금 이 순간, 간신히 지키고 있던 평정심이 허물어진 그는 진심으로 갈등하고 있었다.

도주와 임무. 그 두 가지 갈림길에서.

그리고 자신이 암천과 진태경 중, 과연 누구의 손에 의해 죽게 될지에 대해서.

지금으로부터 수십여 년 전, 암천이 죽음의 문턱에서 헐떡이던 그에게 거절할 수 없는 제안을 건넨 것은 결코 순수한 호의가 아니었다.

암천에 의해 벼려진 검.

오직 암천의 지시에 따라 움직이는 인간 백정.

그것이 천살이 생명과 맞바꾼 새로운 정체성이었다. 아무리 도망쳐도 끊을 수 없는 족쇄였다.

임무를 포기하고 도주한다면, 그를 기다리는 것은 징벌뿐이다.

일평생 동안 수많은 살업을 쌓은 그조차 상상할 수 없는, 끔찍한 고통과 죽음.

숨을 수도 없고, 피할 수도 없다.

그것이 암천, 아니 천주다.

‘큭, 큭큭.’

천살은 소리 없이 웃었다.

이미 답이 정해져 있던 문제로 고민하고 있던 스스로가 한심해서였다.

애초에 선택할 수 있는 갈림길 따위는 없었다.

그의 앞에 놓인 길은, 선택지는 처음부터 하나뿐이었다.

‘죽이거나, 죽는 것.’

천살은 조용히 어둠 속에서 움직였다.

숨소리를 지우고, 기척을 없앴다. 자신이 암천의 원조를 받아 공들여 키워 낸 특급 살수들이 도륙당하는 광경을 지켜보며, 적천강과 진태경을 향해 천천히 접근했다.

‘단 하나. 둘 중 한 놈이라도 해치운다면 설령 임무에 실패하여 도주하더라도 살아남을 수 있다.’

대계는 이미 어그러졌다.

하지만 그에 상응하는 무언가를 가져간다면, 그것이 화왕 적천강의 목이라면 다시 한번 기회를 얻을 수 있을 것이다.

아직 이루지 못한 자신의 복수를, 이 질긴 목숨을 이어 갈 수 있는 기회를.

그리고 천만다행히, 언제나 무심했던 저 하늘도 오늘만큼은 천살의 편인 듯했다.

쉬쉬쉭, 서걱!

파공성과 함께 사라지는 또 하나의 생명. 그러나 신들린 듯이 날뛰는 진태경과 달리, 천살의 눈에 들어온 적천강은 지친 기색이 역력했다.

파파팟. 핏!

사방을 점하고 날아든 암기가 적천강의 전신을 스친다. 뒤이어 머리 위에서 내리꽂히는 살수를 일장에 격살시킨 늙은 용의 입술 사이로 가쁜 숨결이 흘러나왔다.

후욱, 훅.

옅은 푸른빛을 띤 채 말라 비틀어진 입술. 연신 가공할 위력의 공격을 쏟아내면서도 조금씩 가늘게 떨리는 신형.

불과 촌각 전 보여 주었던 그 무시무시한 무위를 잊은 듯한 적천강의 모습에, 천살은 마음속으로 작게 뇌까렸다.

‘이미 한계로군.’

어찌 보면 당연한 일이었다.

적천강은 동천마군을 상대로 이미 자신의 한계를 넘어선 무위를 발휘했고, 이전에도 그의 육신은 이미 크고 작은 상처로 가득했었으니까.

그리고 이 빈틈이, 천살에게는 유일한 기회였다.

‘이 일격으로, 반드시 끝낸다.’

천살은 마음을 가라앉혔다. 살인을 앞둔 이라면 누구나 품는 기운 그 자체, 살기마저 지웠다.

인간이 아닌 가축을 죽이며 살심을 품는 자는 그 어디에도 없다.

살수라는 이름의 백정으로 일평생을 살아온 그는, 마침내 혼신의 힘을 다하여 곧장 쏘아졌다.

동시에 깨달았다.

아직 은영술에 휩싸인 자신을 정확히 응시하는 진태경의 모습을 보며. 전신을 꿰뚫는 듯한 그 시선을 느끼며.

‘처음부터 알고 있었…….’

푸욱.

뜨거운 불길이, 그의 가슴을 관통했다.
```

## Final English reading copy

```markdown
# Chapter 918

*Whoosh!*

In the slowed world, the Eastern Heaven Demon Lord knew instinctively as the old man plunged down like a flash of light, dagger in hand.

*It’s over.*

It was an utterly perfect ambush.

An unavoidable strike for even the Fire King Jeok Cheongang as he was now—no, all the more unavoidable because he had lost his composure and was angrier than ever.

Even if he somehow managed to block or dodge it and escape death, the Eastern Heaven Demon Lord judged that severe injuries were inevitable.

The limping old man he had called Heaven’s Slaughter was one of the finest assassins in the Central Plains, comparable even to the Slaughter Saint.

*I kept that sword hidden for the Emperor.*

It was bitter, but there was nothing to be done.

The grand plan was already on the verge of falling apart.

Survival came first now.

No matter how long it took or what means he had to use, he had to finish his revenge with his own hands.

He could not die until he had watched with his own two eyes as the imperial family, heirs to that cursed bloodline, was wiped out—and offered a memorial rite for his Master and fellow disciples, who had met untimely deaths.

But to begin a revenge that might never come again, he first had to bring down the monster bearing down on him.

The Fire King Jeok Cheongang.

That monster rampaging like a fire demon sweeping across a boundless plain.

*Die.*

The Eastern Heaven Demon Lord was certain of it. At the same time, he prayed fervently for it.

And then, just as the dagger in the old man’s hand—its blade dulled by a coating of ash—brought Force to bear, about to cut Jeok Cheongang in two—

*SHWAAAAK! BOOM!*

A sound of something piercing the air rang out from somewhere, reaching the Eastern Heaven Demon Lord’s ears.

It drowned out every other sound as it tore through the air in a furious rush.

The Eastern Heaven Demon Lord’s eyes flew wide. A blue-white flash had reached its destination before its sound did, filling his vision.

*What is that…?*

A spear of a common, unremarkable design—the sort one could find anywhere.

But the light upon it shone as brightly as the sun overhead, and its heat, hotter than the sun itself, burned even the air as it raced onward.

Toward Jeok Cheongang.

No—to be exact, toward the old man falling above his head.

“……!”

“……!”

“……!”

At that moment, everyone’s movements stopped. The world they saw stopped with them.

Jeok Cheongang, who had belatedly realized the assassin had appeared out of nowhere. The old man plunging down at him like a bolt of lightning. And the Eastern Heaven Demon Lord, watching it all unfold.

*Shwoosh!*

They all watched the spearhead cut through the air toward them, moving as if in slow motion. They felt the power within the blue-white flames coiling around its point.

And at the same time, they understood.

Who owned that spear.

What root that horrifyingly intense Scorching Yang Qi came from.

Before the three-syllable name that had suddenly surfaced could even take shape in their minds, the spearhead had raced forward, erasing the space between them, and reached its destination in an instant.

At the life-or-death moment, the old man frantically changed the direction of his dagger and brought it up to block the spearhead that had come within inches of him.

*Whoom—KABOOOOOM!*

Blue-white flames swelled as they met the Force surging from the dagger. A thunderous boom shook heaven and earth, and the shockwave lashed out in every direction.

*KRRRACK!*

The earth shuddered as if struck by an earthquake. Wind whipped about madly.

In that muffled world filled with nothing but ash, the Eastern Heaven Demon Lord finally pieced together one man’s name and screamed it like a wail.

“Jin Taekyung!”

At that moment—

*Fwoooosh.*

The hazy world split apart.

A blood-soaked man, from head to toe, approached with movements lighter and quicker than ever. He showed his white teeth and grinned.

“Don’t say my name. I might get attached.”

Then he shrugged toward one man standing dazed and motionless at the feet of the Eastern Heaven Demon Lord, who was sprawled there, stiff as a statue.

“Looks like this bastard still hasn’t come to his senses. Should I pull out his tongue while I’m at it?”

“……”

“Old Master?”

The Fire King Jeok Cheongang, his old Master, didn’t answer.

No—he couldn’t answer.

He silently gazed at his Disciple, who had come back as he always did. Then he burst out laughing.

He was so delighted that tears came to his eyes.

At the same time, he felt all the anger and sorrow that had held his whole body in its grip come crashing down, and he grasped his Disciple’s arm tightly.

“Thank you.”

*Grip.*

“For coming back. For coming back to me like this.”

“……!”

The blood-dried corner of the blood-soaked man’s eye—no, Jin Taekyung’s eye—trembled.

*Thank you. For coming back.*

It was a brief sentence, but it was enough.

He could feel the warmth conveyed through that arm, and the sincerity that seeped into every syllable of his Master’s words.

That feeling meant everything.

And so, there was no need for them to say anything more.

This brief reunion between the two men who had carried on the Fire Gate Clan’s lineage would soon become the deaths of their enemies.

That was how the Fire Gate Clan had survived for the past three hundred years. It was the way of these two, bound together as Master and Disciple by a connection no one could explain.

*We’ll smash and burn everything in our way.*

Whatever it is.

We will. Without fail.

*Step.*

Master and Disciple moved forward at the same time. Beyond the dust cloud and ash that had yet to settle, a sticky killing intent crept toward them in secret, wrapping around them.

*Whoooosh!*

* * *

The limping old man, Heaven’s Slaughter, blended into the darkness and quietly waited for his moment.

Even as he watched his subordinates die less than a dozen *jang* away, there wasn’t a trace of agitation in his cool, sunken eyes.

*Whoosh. Slice!*

Before the blade dulled by ash could even reach its target, a head sprang into the air.

Anyone who saw this would find it hard to believe.

Each of those men crumpling like straw dummies was an elite assassin he had spent at least thirty years cultivating.

*I thought I could take down even the Three Saints with those children.*

No—perhaps he really could have.

His ambush just moments earlier had been that perfect. He could have erased the giant known as the Fire King Jeok Cheongang from this world with his own hands.

If not for the unwelcome visitor who had appeared out of nowhere.

*Blazing Flame Divine Dragon Jin Taekyung.*

Heaven’s Slaughter swallowed the groan that threatened to escape him.

It wasn’t just the pain in his broken wrist, which had snapped as he deflected the spear filled with immense energy at the last moment before success.

*So the real monster wasn’t the Master…*

He had seen it with his own eyes in the darkness.

Jin Taekyung, falling with an injury beyond recovery. The shadow of death stirring at the edge of his life as he coughed up blood mixed with pieces of his organs.

*And yet, how could he possibly…?*

Those who roam the martial world with death for a companion are martial artists. And among them, assassins stand closest to death.

That was why Heaven’s Slaughter knew better than anyone.

Since the time he had been trained as an assassin, he had killed people with his own hands using every means at his disposal. For the weight of those deeds, he had even reached death’s threshold himself.

*If Dark Heaven hadn’t helped me, this old man would have turned to a handful of dirt long ago.*

Heaven’s Slaughter’s survival was a miracle. But even that seemed insignificant beside what Jin Taekyung had shown just now.

There was no doubt. Force had pierced straight through his chest.

It had split flesh and bone, destroyed his acupoints, and seeped into his organs, tearing them to shreds from within.

This was an injury no one could recover from—not even with the Great Firmament Immortal’s care, or if Yama himself erased their name from the book of the dead.

And yet Jin Taekyung had come back alive.

Though he looked like a man drenched in blood, his exposed skin was smooth, and his perfectly formed Muscles and Bones—the reason he was known as having a Heavenly Martial Physique—were plain to see.

And that wasn’t all.

His formidable internal energy, amounting to several *jiazi*’s worth—impossible to believe in someone who had only just passed the age of twenty—had also filled back up as if nothing had happened.

As if someone had filled an empty teacup with water.

As if it were only natural.

*This is… something I can’t explain.*

An ability that transcended all reason.

Heaven’s Slaughter’s deeply sunken eyes trembled.

Now, his composure—barely held together until this moment—had finally crumbled. He was truly torn between two choices.

Flight and duty.

And he wondered who would kill him: Dark Heaven or Jin Taekyung.

Several decades ago, when Heaven’s Slaughter had been gasping at death’s door, Dark Heaven had made him an offer he could not refuse. It had never been out of pure kindness.

A blade forged by Dark Heaven.

A human butcher who moved only at Dark Heaven’s command.

That was the new identity Heaven’s Slaughter had exchanged his life for. A shackle he could never break, no matter how far he ran.

If he abandoned his mission and fled, punishment was all that awaited him.

A horrible death in unbearable pain, beyond even what a man who had spent his life committing countless murders could imagine.

There was nowhere to hide. Nowhere to run.

That was Dark Heaven—or rather, the Lord of Heaven.

*Heh. Heheheh.*

Heaven’s Slaughter laughed without a sound.

He thought himself a fool for agonizing over a problem whose answer had already been decided.

There had never been a choice to make.

There had only ever been one path in front of him. One option.

*Kill or be killed.*

Heaven’s Slaughter moved quietly through the darkness.

He silenced his breathing and erased his presence. Watching the elite assassins he had carefully raised with Dark Heaven’s help get slaughtered, he slowly approached Jeok Cheongang and Jin Taekyung.

*If I can take down even one of them, I can survive—even if I fail the mission and flee.*

The grand plan had already gone awry.

But if he brought back something of equal value—if he brought back the Fire King Jeok Cheongang’s head—he might be given another chance.

A chance to carry on his unfulfilled revenge, to keep this stubborn life going.

And, to his great fortune, even the heavens, usually so indifferent, seemed to be on Heaven’s Slaughter’s side today.

*Whoosh! Whoosh! Slice!*

Another life vanished with a piercing sound. But unlike Jin Taekyung, who was rampaging as if possessed, Jeok Cheongang looked utterly exhausted to Heaven’s Slaughter.

*Patapat. Splurt!*

Hidden weapons came flying from every direction, grazing Jeok Cheongang’s body. Then, after killing with a single palm strike the assassin who had dropped down from above, the old dragon exhaled raggedly through his lips.

*Huff. Huff.*

His lips were dry and tinged pale blue. His body trembled faintly, even as he continued to unleash attacks of terrifying power.

At the sight of Jeok Cheongang, who seemed to have forgotten the fearsome martial prowess he had displayed only moments ago, Heaven’s Slaughter muttered to himself.

*He’s reached his limit.*

In a way, it was only natural.

Jeok Cheongang had already drawn out martial prowess beyond his limits against the Eastern Heaven Demon Lord, and his body had been covered in large and small wounds even before that.

And that opening was Heaven’s Slaughter’s only chance.

*This strike will end it. No matter what.*

Heaven’s Slaughter calmed his mind. He erased even his killing intent—the very energy anyone about to kill someone would carry.

No one feels murderous intent when killing livestock instead of a human.

After living his whole life as a butcher under the name of assassin, he finally shot straight forward with all his might.

At the same time, he realized.

Though he himself was still cloaked by his concealment technique, he saw Jin Taekyung staring straight at him. He felt that gaze pierce his entire body.

*He knew from the beginning…*

*Puhk.*

A blazing flame pierced his chest.
```
