<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1016.txt",
      "sha256": "7fae39fd1a6d38fe9be5561cd625184f707cf16a9af3262b7a696bd4bb51ceee",
      "bytes": 13409
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e53dd92c486ca01f83e17378d41bfdaefd3c461a4b752c66552d01ce8a5dfc52",
      "bytes": 1327
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "611b5144e394205d82ab664a36e903511377554b9737ac63e0571a7866e56564",
      "bytes": 238256
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cb6e881f46eb8aec089752d4aeec5a704cab372c6cdf09499fdbbc370260c7a7",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "6256b65677f78dbb1ad8ae60657932bc2bf498ba37163d171d64ffe57a59ee5f",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1109e44476cab7882f6e17baa4799c7f3d051782a0778c25c8cbd3b97ced9a2a",
      "bytes": 1408
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "b6722229cb997ba967c94f693b2a58a6494e06f2e8f36df55d82a32e5d614869",
      "bytes": 904
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "10a37256f8227ddbdfa3379b010a79182ed12fd3cb02c2f9675ab34b947d734c",
      "bytes": 733
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "fafad541aec998b8f7a4296cf5d0755bb0288ad2e8ce94a1e5076d492675d48f",
      "bytes": 742
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "5988ae39f9d442b984c608132f0278b805933e117834a689c4cde3cdb0f70909",
      "bytes": 980
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "d822b25c57ada3b7db3ba0899105678e18063f61fc963f508c40d6b61b356abe",
      "bytes": 2461
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e9febd618486b99b8ff4e9220ac86edf486c2abc2fc0dc1a17734b20ec6f79fd",
      "bytes": 276986
    }
  ],
  "estimated_tokens": 11936
}
-->

# Durable State Update — Chapter 1016

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
1 and safe_through 1016. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1016. Profile updates may replace only one
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
  "chapter": 1016,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1016,
    "continuity_sources": [1016],
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
    "Taekyung’s force of roughly three thousand has passed Lanzhou and is approaching the Qilian Mountains; battle is expected soon.",
    "Wolhwa’s latest missive to Taekyung contains unusually affectionate personal language and hopes they meet again.",
    "Namho has an important matter he says he can only disclose to Taekyung now.",
    "The six Baekma Bang men left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Sama Pyo disobeyed Sima Gong’s order to return to Gansu; consequences are unknown.",
    "Sima Gong ordered two martial artists dealt with for making a taboo remark about Sama Pyo’s succession."
  ],
  "continuity_sources": [
    1014,
    1015
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What does Namho need to tell Taekyung, and why can he only tell him now?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?",
    "What consequences, if any, will Sama Pyo face for disobeying Sima Gong’s order?"
  ],
  "safe_through": 1015,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 팔천협    | **Eight Spring Gorge** |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 황하 | **Yellow River** | River along which civilization began. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 순간이동 | **Teleportation** | Spatial-transference magic used by Magic Johnson. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 진상 | **Jinsang** | Koizumi's punning address to Jin, retained for the Korean wordplay. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1015
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1015
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1013
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1015
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1014
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1015
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1015
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 1015
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Wolhwa says she likes Taekyung, whose family she supports through a mutually beneficial alliance with Jin Wikyung, and has sent him an unusually affectionate personal missive alongside her professional intelligence.

## Korean source

```text
＃1016화



처음 만났을 때부터 어렴풋이 느끼긴 했지만, 월화는 도무지 종잡을 수 없는 여자다.

‘아니, 도대체 무슨 바람이 불어서 갑자기 이런 서신을 보낸 거지?’

하청지회(河淸之會).

내가 고사성어에 대해서는 잘 모르긴 하지만, 대충 직역해 봐도 오해의 소지가 다분하다.

강이 맑아지는 것 같은 만남이라니.

최소 썸 타는 사이에서만 쓸 법한 내용 아닌가.

‘찌라시에 박차를 가하겠구만.’

물론 내가 도끼병 환자도 아니고, 고작 이런 서신 한 통으로 괜한 오해를 하지는 않는다.

월화가 내게 보이는 관심은 어디까지나 한 사람의 하오문도로서 국한된 것이지, 결코 이성적인 것과는 아무런 상관이 없다는 사실쯤은 이미 오래전부터 알고 있었으니까.

다만…….

‘내가 아니라, 주 소저가 오해한다는 게 문제지.’

내심 중얼거린 나는 꼬깃꼬깃해진 전서를 다시 인벤토리에 집어넣었다.

좀 찝찝하긴 하지만 지금으로서는 별수 없다.

어차피 결국 시간이 흐르면 자연스럽게 해결될 문제고, 이것보다 훨씬 더 중요한 난제(難題)들이 앞을 가로막고 있었으니.

그리고 지금 이 순간.

화아아악.

서늘한 고원의 바람과 함께 마침내 모두의 앞에 모습을 드러낸 거대한 산맥은, 그 난제에 한 걸음 더 가까워졌다는 이정표와 같았다.

‘저건.’

나도 모르게 크게 뜨이는 두 눈.

아득하고, 눈부시다.

그것이 기련산(祁連山)을 처음으로 목격한 순간 떠오른 감상이었다.

“말로만 들었지. 이거 진짜, 와…….”

혁무진이 넋 나간 목소리로 중얼거렸다.

아니, 비단 녀석뿐만이 아니라 나를 포함한 모두가 그랬다.

깎아지른 듯한 벼랑과 용의 그것처럼 끝없이 이어지는 산맥, 그 사이로 구름을 뚫고 아득히 솟아 있는 봉우리들은 마치 하늘을 떠받치는 듯하다.

그뿐인가.

산맥 곳곳을 새하얗게 물들인 만년설(萬年雪)은, 전혀 다른 새로운 세상에 발을 디딘 듯이 신비로운 분위기를 자아냈다.

하지만 그와는 별개로 벼랑과 벼랑 사이에 보이는 비좁은 협곡은 지옥의 입구처럼 좁고 길었으니, 그야말로 자연이 만들어낸 천애의 요새가 따로 없었다.

‘이 정도면 듣던 것 이상인데.’

산서성의 명운을 몇 번이나 뒤바꾼 팔천협(八天峽)도 지금 보이는 기련산에 비하면 동네 뒷산처럼 느껴질 정도다.

물론 그로 인한 단점 역시 명백했지만.

“너무 넓군.”

송일섬의 짤막한 한 마디에, 나는 조용히 고개를 끄덕였다.

맞다.

기련산이 차지하는 면적은 단순히 넓은 정도를 넘어 광활하다.

장장 수천 리에 걸쳐 이어져 있다는 산맥은 감숙성 서남방에서 시작하여 청해성까지 닿을 정도니, 어설프게 급조한 그물을 넓게 펼쳤다가는 오히려 단숨에 찢겨 나갈 것이다.

상대가 암천이라는 대어(大漁)라면 더더욱.

그렇기에 이미 감숙 무림인들의 삼엄한 경계에 둘러싸인 기련산에 진입한 직후, 잠시 한자리에 모인 수뇌부들은 가장 먼저 이 문제를 화두에 올렸다.

정확히는, 나와 적천강이.

“후방에 배치된 병력치고는 너무 많습니다. 그래서 드리는 말씀인데…….”

“빼. 싹 다.”

내가 미처 말을 끝맺기도 전에 치고 들어온 적천강이 귀를 후비며 덧붙였다.

“말로 들었을 때도 조금 쎄하긴 했지만, 직접 보고 나니 확실해졌다. 대설산과 돈황에 있는 놈들을 죄다 쏟아부어도 이곳을 완벽하게 틀어막는 건 불가능에 가까워. 차라리 싹 다 끌어모아서 다른 전선에 쑤셔 박는 게 상책(上策)이겠지.”

마치 진상 세입자에게 방 빼라고 선언하는 집주인처럼 좌중을 쓸어보던 적천강의 시선이, 문득 한 사람에게서 멈췄다.

“이 정도는 충분히 알고도 남을 놈이라고 생각했는데, 노부가 착각한 것이냐?”

흑야왕 사마공이 부드럽게 웃으며 대꾸했다.

“후한 평가를 내려 주셔서 감사합니다만, 저는 물론 여기 함께 자리하신 여러 문주와 가주들은 감숙 일대에 대해 누구보다 잘 알고 있습니다. 물론 기련산도 포함이지요.”

“누구보다 잘 알고 있다…….”

되새김질하듯 사마공의 말을 작게 뇌까린 적천강이 담담하게 입을 열었다.

“잘 모르면 닥치고 있으라는 뜻으로 들리는군.”

“저희가 감히 어찌, 그것도 다른 사람도 아닌 노 선배께 그런 무례를 범할 수 있겠습니까. 부디 말씀을 거두어 주십시오.”

“고정하십시오. 적 대협.”

“심도 깊은 논의 끝에 결정지은 사안일 뿐입니다.”

사마공의 매끄러운 사죄를 시작으로, 눈치를 살피던 감숙 무림의 문주와 가주들이 차례대로 포권을 취했다.

마치 우두머리를 따르는 졸개들처럼.

그리고 바로 그때였다.

눈 앞에 펼쳐진 광경을 말없이 응시하던 내 시야에, 그들 중 유일하게 허리를 꼿꼿이 펴고 있던 누군가의 모습이 들어온 것은.

‘사마표.’

특유의 속을 알 수 없는 표정을 짓고 있던 녀석과 내 시선이 허공에서 맞닿은 것도 잠시. 이내 사마표 역시 자신의 아버지를 따라 조용히 고개를 숙여 보였다.

스윽.

갑작스럽게 맴도는 침묵 때문일까.

옷깃 스치는 소리가 유난히도 크게 울려 퍼진 그 순간, 풍운검군이 입을 열었다.

“빈도로서는 쉽게 판단하기가 어렵구려. 여기 계신 분들은 하나같이 감숙 무림의 영수(領袖)이시니 올바른 판단을 내렸으리라 믿고 싶지만…… 적 대협께서 하신 말씀 또한 충분히 가능성 있는 판단이라 생각됩니다.”

“충분히 가능성이 있는 정도가 아니라, 십중팔구는 그렇게 될 것 같은데요.”

불쑥 던진 한마디에 사람들의 시선이 쏠렸지만, 나는 조금도 당황하지 않고 말을 이어갔다.

“삼만 하고도 수천에 달하는 아군 병력이 있다고 해도, 세 개나 되는 전선을 유지하기 위해 분산되어 있으면 죽도 밥도 안 돼요. 막말로 뭉치면 살고 흩어지면 죽는다는 말이 괜히 나왔겠습니까?”

“고맙군. 모두가 까맣게 잊고 있던 기본 중의 기본을 알려 줘서.”

피식 실소를 흘리며 입을 연 노호검객을 향해, 나는 어깨를 으쓱해 보였다.

“굳이 그렇게까지 감사하실 필요는 없습니다. 뭐 사람이 오래 살다 보면 가끔 깜빡할 수도 있죠. 그런 것치고는 너무 기본 중의 기본이지만.”

“……!”

“아, 죄송합니다. 제가 너무 말을 건방지게 했나요?”

지금 한 말은 속을 뒤집으려고 한 게 아니라, 진심이다.

얼굴이 붉게 달아오른 노호검객의 모습에 아차 싶긴 했지만, 입술이 자동으로 움직이는 걸 어떡하겠나.

뭐, 그래도 이제는 완전히 한배를 탄 아군인데 이해해 주겠지.

아니면 말고.

“너, 아니 자네…….”

새파란 어린놈의 말대꾸에 피가 거꾸로 솟는지, 적천강의 눈치를 살피며 슬슬 과호흡 증세를 보이던 노호검객을 대신해 대타가 나섰다.

“뭉치면 살고 흩어지면 죽는다라, 맞는 말이로군. 당연히 지금 같은 상황에서는 아니겠지만.”

사형제 좋다는 말이 이래서 나왔나.

나는 적절한 시점에 끼어든 태을무정검을 똑바로 응시했다.

“지금 같은 상황이라면 어떤 걸 말씀 하시는 건지.”

“몰라서 묻는 것이냐, 아니면 알면서도 모른 척하는 것이냐?”

태을무정검이 눈살을 찌푸리며 덧붙였다.

“벌써 잊은 모양이군. 놈들이 어떤 기괴망측한 사술(邪術)을 부리는지.”

태을무정검이 무엇을 말하는지 모르는 사람은 이 자리에 아무도 없다. 물론 나 역시도 마찬가지다.

“이동진(移動陳). 그렇죠. 그게 있었죠.”

고개를 끄덕인 나는 재차 입을 열었다.

마치 무슨 일이라도 있냐는 듯, 담담하기 그지없는 어투로.

“그래서요?”

“뭣이!”

“뭐라?”

동시다발적으로 튀어나오는 반문들.

그러나 처음부터 지금 같은 반응을 예상하지 못했다면, 이런 이야기를 꺼내지도 않았을 것이다.

“이곳까지 오는 길에 문득 한 가지 여쭙고 싶은 게 생각났는데…….”

나는 말꼬리를 흐리며, 좌중을 천천히 쓸어보았다.

“이동진의 존재를 그토록 경계하시는 분들이, 도대체 무슨 이유로 물경 삼만이 넘는 대병력을 전방에 배치하신 겁니까?”

“……!”

일순간, 고요한 침묵이 주위의 공기를 짓눌렀다.

그리고 불현듯이 찾아온 그 침묵은, 잔잔한 눈빛으로 상황을 주시하던 누군가가 입을 열기 전까지 쉽게 사라지지 않았다.

“대의(大義)를 위해서.”

흑야왕 사마공. 또 다시 그다.

모두를 대신해서 입을 연 사마공이 착 가라앉은 음성으로 말을 이었다.

“앞서 자네가 했던 말이 맞네. 어설프게 분산했다가는 이도 저도 아니게 되지. 하여 모두가 머리를 맞대고 고심한 끝에 얻어 낸 결론이 지금의 이 상황일세. 세 개의 전선으로 나누어, 언제든 후방으로 되돌아갈 수 있게 하는 것.”

언뜻 듣기에는 그럴듯한 의견이다.

처음으로 수뇌부가 한자리에 모였을 때도 나왔던 말이기도 했다.

그러나…….

그건 어디까지나 앞서 사용한 표현 그대로 ‘언뜻’ 듣기에만 그럴듯했다.

“되돌아가기에는 거리가 상당한 것 같은데요. 만약 암천이 이동진을 통해 후방으로 나타난다면, 저희가 놈들을 무슨 수로 따라잡겠습니까?”

수만 마리의 메뚜기 떼가 들판을 덮치면 모든 것이 사라지기까지는 한나절도 걸리지 않을 것이다.

암천은 바로 그 메뚜기 떼다.

그리고 며칠씩이나 되는 시간 차이를 좁혀 따라잡기에는, 놈들의 이빨과 날갯짓 속도가 너무나도 흉포하면서도 빠르다.

‘아군이 뒤늦게 도착했을 때면, 이미 감숙성 일대가 초토화되고 암천은 중원으로 향하고 있겠지.’

그렇다면 과연 저들이, 짧게는 수십 년에서 길게는 백 년이 넘도록 감숙성의 터줏대감이었던 그들이 이 사실을 몰랐을까?

‘그럴 리가 없지.’

알고 있었을 것이다. 분명히.

그리고 다음 순간 사마공의 입술 사이로 흘러나온 음성은, 내 짐작을 확신으로 굳혀 주기에 충분했다.

“그렇겠지. 분명히.”

“……!”

“……!”

짧은 그 한마디에 담긴 뜻을 깨달은 나와 적천강은 눈빛을 깊숙이 가라앉혔지만, 이해하지 못한 자도 있다.

바로 지금, 의문 어린 시선으로 사마공을 바라보는 풍운검군처럼.

“사마 문주. 그게 도대체 무슨 말씀이신지…….”

끝맺어지지 못하고 흐려지는 말꼬리.

그러나 풍운검군 역시 종남파라는 거대 방파를 이끄는 일문(一門)의 문주다. 앞서 흘린 음성의 여운이 사라지기도 전에, 문득 어떠한 짐작을 떠올린 그의 얼굴이 딱딱하게 굳었다.

“설마, 이대로 묵과(默過)하겠다는 뜻이오? 설령 놈들이 이동진으로 아군의 전선을 뛰어넘어 후방을 유린하더라도?”

사마공이 담담한 표정으로 대답했다.

“묵과라니, 당치 않소. 다만 우리는 가장 승산이 높은 선택을 한 것뿐이오.”

“잠깐. 그렇다면 후방은 어찌 되는 거요? 남아 있는 양민들과 무인들은?”

“그러니 말하지 않았소. 대의를 위해서라고.”

“사마 문주!”

쾅!

단번에 산산조각 나는 의자.

하지만 고함과 함께 자리를 박차고 일어난 풍운검군의 모습에도, 이어지는 사마공의 목소리에는 한 치의 흔들림도 없었다.

“만약 암천이 사막을 넘어 정면으로 들이닥친다면 우리는 즉시 모든 전력을 그곳에 집중시킬 거요. 이동진을 통해 후방을 점할 수도 있겠지만…… 그것이야말로 놈들에게 있어 최악의 한 수가 되겠지.”

밖에서 안으로 그물망을 찢고 들어간 물고기는 언제든 제 뜻대로 출입할 수 있지만, 순간이동 하듯이 그물망을 통과한다면 그저 갇히는 꼴이 된다.

‘양면전선(兩面前線).’

그것이 사마공의 노림수였다.

효과적이지만, 엄청난 희생을 필요로 하는.

실로 사파다운 기책(奇策).

하지만…….

과연 이것뿐일까.

“지키는 것도, 불태우는 것도 우리의 선택이오. 이곳의 주인은 종남파도, 태원진가도 아니니.”

시린 안광(眼光)을 뿜어내며 풍운검군의 말문을 틀어막은 사마공의 모습을, 나는 깊게 가라앉은 눈빛으로 응시했다.
```

## Final English reading copy

```markdown
# Chapter 1016

I’d vaguely sensed it from the moment we first met, but Wolhwa was impossible to figure out.

*What on earth possessed her to send me a letter like this out of nowhere?*

A Meeting When the Yellow River Runs Clear.[^1]

I didn’t know much about classical idioms, but even a rough, literal translation left plenty of room for misunderstanding.

A meeting like the moment the river runs clear.

Wasn’t that the sort of thing you’d say only to someone you were at least flirting with?

*This is going to give the gossip mill a real boost.*

Of course, I wasn’t delusional enough to get the wrong idea over a single letter like this.

I’d known for a long time that Wolhwa’s interest in me was limited to her being a member of the Lower District Sect. It had absolutely nothing to do with romantic feelings.

But…

*The problem is that Young Lady Ju might misunderstand—not me.*

I muttered to myself and put the crumpled missive back in my Inventory.

It bothered me a little, but there was nothing I could do about it for now.

Time would sort it out eventually. Besides, far more important problems stood in my way.

And at this very moment—

*Whoosh.*

A vast mountain range finally appeared before us, accompanied by the cold wind sweeping across the plateau. It was like a marker telling us we’d taken one more step toward those problems.

*That’s…*

My eyes widened before I knew it.

Vast. Dazzling.

That was what came to mind the first time I saw the Qilian Mountains.

“I’d only heard about them. This is the real thing. Wow…”

Hyuk Mujin murmured, sounding dazed.

But he wasn’t the only one. Everyone was staring in wonder, myself included.

Sheer cliffs and a mountain range that stretched on without end, like the body of a dragon. Between them, peaks rose so high they pierced the clouds, as if holding up the sky.

And that wasn’t all.

The perpetual snow that painted great swaths of the mountains white gave the place an otherworldly air, as though we’d stepped into a completely different world.

Yet the narrow gorges between the cliffs were so long and constricted they looked like the entrance to hell. This was nothing less than a natural fortress, built by nature itself.

*This is even more than I’d heard.*

The Eight Spring Gorge, which had changed Shanxi’s fortunes time and time again, would have looked like a hill behind the village compared to the Qilian Mountains before us.

But the drawbacks were just as obvious.

“It’s too vast.”

At Song Ilseom’s brief remark, I nodded quietly.

He was right.

The Qilian Mountains weren’t merely wide. They were immense.

The range stretched for thousands of *li*, beginning in southwestern Gansu and reaching all the way to Qinghai. If we spread out a hastily assembled net over such a wide area, it would be torn apart in an instant.

Especially if our target was a big fish like Dark Heaven.

So, as soon as we entered the Qilian Mountains—which were already surrounded by the Gansu martial artists’ tight defenses—the leaders gathered in one place to discuss this problem first.

Or, more precisely, Jeok Cheongang and I did.

“There are too many troops stationed in the rear for what they’re meant to do. So, what I’m saying is—”

“Pull them out. All of them.”

Jeok Cheongang cut in before I could finish. He picked at his ear, then added,

“I had a bad feeling when I heard about it, but seeing it in person confirms it. Even if we threw every last man at the Great Snow Mountain and Dunhuang into this, we couldn’t completely seal off this place. Our best move would be to pull everyone together and throw them at another front.”

Jeok Cheongang swept his gaze over the gathering like a landlord telling a troublesome tenant to get out. Then his eyes came to rest on one man.

“I thought you’d know this much already. Was I mistaken?”

The Black Night King, Sima Gong, answered with a gentle smile.

“Thank you for your generous opinion of me. But I, and the many Sect Leaders and Family Heads gathered here, know the Gansu region better than anyone. The Qilian Mountains included, of course.”

“Know it better than anyone…”

Jeok Cheongang quietly repeated Sima Gong’s words, as if turning them over in his mouth, then spoke evenly.

“That sounds like you’re telling me to shut up if I don’t know enough.”

“How could we dare show such disrespect to you, Senior Jeok—not you, of all people? Please, take back your words.”

“Please calm yourself, Great Hero Jeok.”

“It’s simply a matter we decided after thorough discussion.”

After Sima Gong’s smooth apology, the Sect Leaders and Family Heads of Gansu Murim, who’d been watching for a cue, took turns clasping their hands in salute.

Like lackeys following their boss.

And that was when, as I silently watched the scene before me, I noticed the only one among them sitting with his back straight.

*Sama Pyo.*

For a moment, his unreadable expression met my gaze. Then Sama Pyo quietly lowered his head, following his father’s lead.

*Swish.*

Perhaps it was the sudden silence that made the sound of clothing brushing together ring unusually loud.

The Wind-and-Cloud Sword Lord spoke.

“It’s difficult for this poor Daoist to make a judgment so easily. Everyone here is a leader of Gansu Murim, and I would like to believe you’ve reached the right decision. But… what Senior Jeok has said also seems entirely possible.”

“Not just possible. I’d say it’s more than likely.”

At my sudden remark, everyone turned to look at me. I continued without the slightest embarrassment.

“Even if we have thirty thousand allied troops and several thousand more, splitting them up to maintain three separate fronts means we won’t be worth a damn anywhere. There’s a reason people say you survive by sticking together and die when you scatter.”

“Thank you. For reminding us all of the most basic principle, which everyone here had somehow completely forgotten.”

The Roaring Fury Swordsman spoke with a derisive chuckle. I shrugged at him.

“You really don’t have to thank me that much. People forget things from time to time when they get old. Though this is a pretty basic principle.”

“……!”

“Oh, sorry. Was that too cheeky?”

I hadn’t said it to get under his skin. I meant it.

Seeing the Roaring Fury Swordsman’s face turn red, I realized I might’ve gone too far—but what could I do when the words just came out on their own?

Well, we were all on the same boat now. He’d understand.

Or not.

“You—no, you…”

Maybe the cheek of a young punk talking back had made his blood boil. The Roaring Fury Swordsman glanced at Jeok Cheongang, and seemed to be starting to hyperventilate. Someone else stepped in for him.

“Stick together to live and scatter to die. That’s true enough. But not in a situation like this.”

I guess that’s what having fellow disciples was good for.

I looked straight at the Taeeul Merciless Sword, who’d stepped in at just the right moment.

“What kind of situation do you mean?”

“Are you asking because you don’t know, or because you know and are pretending you don’t?”

The Taeeul Merciless Sword frowned and continued.

“You seem to have forgotten already what kind of monstrous dark arts they wield.”

Nobody here failed to understand what the Taeeul Merciless Sword meant. I certainly hadn’t.

“The Moving Formation. Right. They have that.”

I nodded, then spoke again in a perfectly calm voice, as if nothing were wrong.

“So?”

“What!”

“What did you say?”

Questions burst out from all sides at once.

But if I hadn’t expected this kind of reaction, I wouldn’t have brought it up in the first place.

“On the way here, I thought of something I wanted to ask…”

I let the words trail off and slowly looked around the gathering.

“If you’re so wary of the Moving Formation, why did you station an army of over thirty thousand in the front in the first place?”

“……!”

For an instant, a quiet silence pressed down on the air around us.

It didn’t lift until someone, who’d been watching the situation with calm eyes, suddenly spoke.

“For the greater good.”

The Black Night King, Sima Gong. Him again.

Speaking on everyone’s behalf, Sima Gong continued in a low, steady voice.

“What you said earlier was right. If we spread ourselves out carelessly, we’ll accomplish nothing. So we put our heads together and considered it carefully, and this is the conclusion we reached: divide our forces among three fronts, so they can return to the rear at any time.”

At first glance, it sounded reasonable.

It was the same proposal that had come up when the leaders first gathered.

But…

That was only true, as I’d just said, *at first glance*.

“It seems like a long way to go back. If Dark Heaven appears in the rear through the Moving Formation, how are we supposed to catch up with them?”

If a swarm of tens of thousands of locusts descended on a field, it wouldn’t take even half a day for everything to disappear.

Dark Heaven was that swarm of locusts.

And their fangs and wings were too savage and fast for us to make up a delay of several days and catch them.

*By the time our allies arrived, Gansu would already be laid waste, and Dark Heaven would be heading for the Central Plains.*

But did those men really not know this? Men whose families had been fixtures in Gansu for decades, even more than a century?

*Of course they knew.*

They had to.

And the next words that came from Sima Gong’s lips were enough to turn my suspicion into certainty.

“They would. Certainly.”

“……!”

“……!”

At that brief reply, Jeok Cheongang and I understood what he meant, and our gazes grew intent. But not everyone understood. The Wind-and-Cloud Sword Lord, for one, was looking at Sima Gong with a puzzled expression.

“Lord Sima. What exactly do you mean by that…?”

His words trailed off unfinished.

But the Wind-and-Cloud Sword Lord was the leader of the Zhongnan Sect, a great sect in his own right. Before Sima Gong’s words had even faded, a suspicion occurred to him, and his face stiffened.

“Are you saying we’ll just let it happen? Even if they use the Moving Formation to bypass our lines and ravage the rear?”

Sima Gong answered with an even expression.

“Let it happen? That’s an absurd accusation. We’ve simply chosen the option with the best odds of victory.”

“Wait. Then what happens to the rear? The common people and martial artists who remain there?”

“That’s why I said it. For the greater good.”

“Lord Sima!”

*Crash!*

The chair shattered in an instant.

But even as the Wind-and-Cloud Sword Lord shouted and sprang to his feet, Sima Gong’s voice didn’t waver in the slightest.

“If Dark Heaven crosses the desert and attacks us head-on, we’ll immediately concentrate every force there. They could use the Moving Formation to take the rear… but that would be the worst move they could make.”

A fish that tore through a net from the outside could come and go as it pleased. But if it passed through the net as if by teleportation, it would only end up trapped inside.

*A two-front war.*

That was Sima Gong’s plan.

Effective, but one that would demand enormous sacrifice.

A truly unorthodox scheme.

But…

Could that be all there was to it?

“Whether we defend this place or burn it to the ground is our choice. Zhongnan Sect doesn’t own this land. Neither does the Jin Family of Taiyuan.”

Sima Gong’s icy gaze silenced the Wind-and-Cloud Sword Lord. I watched him, my own gaze sinking deep.

[^1]: The Yellow River running clear is an exceptionally rare, auspicious event; here, the phrase conveys the hope of meeting again.
```
