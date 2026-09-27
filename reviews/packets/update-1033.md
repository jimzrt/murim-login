<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1033.txt",
      "sha256": "922a7201d84ac09a6fa571806d9018644b00e9286e9cfba309e1ef54a91856cc",
      "bytes": 12864
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "beb94d6768a0d58036efc967a8b6aa5d84c63ed240c26f72e6d58b73b50d2ebe",
      "bytes": 1285
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8de2f0fc116939d47330b96a3507fe99d2df5348d01698219fb77d850bdf09bc",
      "bytes": 240120
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "af1b3d2448e1f5d10dd82d70131ddca3e0897b458ae64ad4a849c9a8f0fafa67",
      "bytes": 932
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5c44d317784f9e3d3843a6b13bfc2a41c861df45dee4ed662d49ef4b8b7fcd35",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f06c3200747a5df2a91b466f8f6fd99d4c638007b024aef4fe2eb697a6df2a5e",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "238b8eea33da6151b9b815b5939523df63d48ded12ce376ad6c99533db7d03bd",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f3988e1f6ef52dd9c144d63c310736a9c9c2d54c6c10c02be87079691e1c649d",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "f34e5c906e7115df1e1667db963dd544f31c5ba0f407f269610d789f9feeae39",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7bef61cf3c1189d52da85c19602897ae067265e940f6ef0566c1baf640ee2182",
      "bytes": 279224
    }
  ],
  "estimated_tokens": 10914
}
-->

# Durable State Update — Chapter 1033

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
1 and safe_through 1033. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1033. Profile updates may replace only one
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
  "chapter": 1033,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1033,
    "continuity_sources": [1033],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord calls the seven soulless Death Knights Black Ghosts; they have grown stronger and can recover from seemingly fatal injuries.",
    "The Black Ghosts feel neither fear nor pain; one is the Black Axe Fiend, a great fiend who served the Heavenly Demon and was believed to have died.",
    "The Zhongnan Sect’s forces are fighting Dark Heaven’s followers on the snowy plain; two Black Ghosts have broken the sect’s formation.",
    "The Wind-and-Cloud Sword Lord’s lifelong sword was shattered by a Black Ghost.",
    "Jin Taekyung and Jeok Cheongang are fighting on the battlefield as a wave of magical power sweeps across it."
  ],
  "continuity_sources": [
    1031,
    1032
  ],
  "open_questions": [
    "Who are the seven Death Knights, what is their rank, and who commands them?",
    "What is the Lord of Heaven’s identity and purpose?",
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?",
    "How did the Black Axe Fiend return from the dead, and who is the other Black Ghost present?"
  ],
  "safe_through": 1032,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 사파     | **unorthodox faction**                           |                                                       |
| 일격     | **One Strike**                         |
| 감숙     | **Gansu**              |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1032
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung, and he admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1032
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1032
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1030
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1030
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1031
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1033화



하나의 무공에는 최소 수십여 개의 움직임과 그에 맞는 묘리(妙理)가 담겨 있다.

하지만 어떤 무공을 익혔더라도, 결국 적의 공격에 대응하는 방법은 크게 두 가지로 나뉜다.

막거나, 피하거나.

그리고 지금 이 순간, 내가 택한 방법은 후자였다.

쾅! 콰드드드득!

맹렬한 파공성과 함께 날아든 섬광이 지면을 강타한다.

지진이라도 난 듯 뒤집히는 땅거죽과 어마어마한 충격파.

적게 잡아도 십수 명에 달하는 적들이 그 여파에 휩쓸려 흔적도 없이 사라졌지만, 정작 돌조각 따위의 파편으로 생채기만 입은 나는 등골이 서늘해졌다.

‘빠르고, 강하다.’

제법 먼 곳에서 쏘아진 투창(投槍)이라고는 믿을 수 없을 만큼의 속도와 파괴력.

그런 의미에서 보자면 조금 전의 회피는 내게 있어 선택이 아니라 강요나 다름없었다.

만약 곧바로 맞받아치는 것으로 대응했다면, 그것만으로도 분명 상당한 힘이 소모되었을 테니까.

곁에 있는 적천강 역시 그 사실을 모르지 않았다.

“이미 짐작하고는 있었지만, 확실히 평범한 내력을 지닌 놈들은 아니로군.”

착 가라앉은 음성으로 뇌까린 적천강이 주먹을 말아쥐었다.

그의 시선이 닿은 방향의 끝에는, 저마다의 주인을 실은 채 허공을 밟으며 우리를 향해 다가오는 네 기의 유령마가 있었다.

“넷이라. 앞서 우리를 피해 지나쳐 간 놈들이 몇 명이었지?”

비록 기련산만큼은 못하더라도, 대설산 일대 역시 드넓은 면적을 지닌 곳.

옅은 서리가 뒤덮인 산 밑의 땅은 지금처럼 엄청난 숫자의 적과 아군이 뒤얽힌 대규모 회전(會戰)을 벌일 수 있을 만큼 광활했고, 그 누구보다 앞서 하나의 송곳처럼 적진을 돌파한 나와 적천강으로서는 놈들 모두를 막을 수 없었다.

더군다나 전투에서 승리하는 데 가장 중요한 건, 몸통이 아니라 머리를 베어 내는 것이었으니까.

“제가 본 게 맞으면, 둘이요.”

나는 앞서 창이 날아오기 전, 저 멀리서 전해졌던 굉음과 진동을 떠올렸다.

그리고 그 방향과 거리를 짐작해 보았을 때, 그건…….

“아마도 그 두 놈이, 종남파 쪽으로 향한 것 같습니다.”

물경 삼만에 달하는 아군 중 종남파의 병력은 일천에 불과하지만, 그들 전원이 속가가 아닌 본산의 정예인 데다 세 명의 초절정 고수가 포진해 있는 만큼 강력하다.

적들이 확실히 승리하기 위해서는 그들을 막아 내는 것이 매우 중요할 터였다.

“그럼 지금 나타난 저놈들까지 합쳐서 다섯이로군.”

이미 둘을 놓쳤고, 이제 넷이 나타났다.

그러나 데스 나이트, 아니 흑귀(黑鬼)라 불리는 저 괴물들은 지금까지 확인된 바에 의하면 총 일곱.

나는 백염을 고쳐잡으며 작게 중얼거렸다.

“한 자리가 비네요.”

“그렇다면 나머지 한 놈은.”

“혈검마군의 곁을 지키고 있거나, 사마공이 이끄는 감숙 무림인들 쪽으로 향했겠죠. 만약 후자가 아니라면…….”

나는 조용히 말꼬리를 흐렸지만, 사마공의 수상쩍은 행적에 대해 이미 알고 있던 적천강에게는 더 이상의 설명이 필요 없었다.

“사마공, 그 빌어먹을 사파 놈이 암천과 붙어먹었다는 거겠지.”

그래, 맞다.

단순히 사마공 쪽으로 흑귀가 가지 않았다는 것만으로 확실하게 단정 짓기는 어렵지만, 배신의 가능성이 매우 높아진다는 사실은 부정할 수 없었다.

내가 혈검마군이라면, 이미 아군이라 할 수 있는 사마공에게 구태여 흑귀를 보내진 않을 테니까.

더군다나…….

‘저 정도의 전력이라면, 더더욱 그렇겠지.’

나는 무시무시한 기세를 내뿜으며 가까워지는 흑귀들을 응시했다.

제각각 도, 검, 창, 그리고 쇄겸(鏁鎌)이라 불리는 사슬낫을 든 그들은 전진하는 적들의 머리 위를 뛰어넘어 우리를 향해 쏘아지고 있었다.

하나하나가 일성(一城)을 뒤흔들 정도의 초절정 고수들.

거기에 더해 고통도, 감정도 느끼지 못하는 데다가 엄청난 회복력은 인간을 벗어났다.

아니, 놈들은 이미 완전한 괴물이었다.

지금껏 무림의 그 누구도 접해 보지 못했을 기이한 존재들.

“노야.”

“더 이상 말할 것 없다.”

콰드득!

이 와중에도 영혼 없는 눈으로 달려드는 적의 머리를 일권에 박살 낸 적천강이 말을 이었다.

“저놈들이 어떻게 되먹은 괴물들인지는 몰라도, 죽을 때까지 죽여 버리면 그만이니.”

그의 입술 사이로 나직한 한 마디가 흘러나온 그 순간.

팟.

동시에 지면을 박차고 쏘아진 우리는, 모든 힘을 다해 휘두르고 내뻗었다.

나는 검푸른 강기가 넘실거리는 백염의 창날을, 적천강은 새하얀 불길에 휩싸인 일장을.

화아아악!

휘황한 섬광이 반경 십여 장을 감싸 안고, 사방에서 끊임없이 밀려들던 광신도의 파도가 갈라졌다.

아니, 증발했다.

꽈앙! 드드드드득!

하늘이 쪼개지는 듯한 굉음과 함께 땅이 뒤흔들렸다.

끔찍한 화염신장의 열기로 순식간에 타들어 간 시신들이 힘없이 허물어지고, 창날에 베어 병장기와 함께 조각조각 나뉜 채 갈라져 튕겨 나갔다.

비록 고통도, 감정도 제거된 그들이었으나 지금 이 순간 숨이 끊어진 일백여 명의 적들 모두에게 죽음은 평등하게 찾아왔다.

그리고 삽시간에 죽음으로 뒤덮인 그 공백 사이로.

스아아아.

어스름한 밤안개와도 같은 죽음의 기운을 덧씌우며, 네 마리의 흑귀가 나와 적천강을 향해 짓쳐 들었다.

쏴악!

무시무시한 압력을 불러일으키는 날붙이를 따라 바람이 갈라진다.

제각각 동서남북을 점한 채 일격을 내지르는 놈들의 모습은 정교한 톱니바퀴처럼 완벽하게 맞물렸고, 그렇기에 일말의 빈틈조차 없었다.

하지만…….

‘분명히 있다. 빈틈이.’

나는 마음속으로 뇌까리며, 흐릿한 잔상을 남기며 뻗어 오는 도신과 창날에 맞서 한 걸음을 성큼 내디뎠다.

정확히 목을 노리며 꿰뚫어 오는, 그 섬뜩한 두 줄기의 섬광을 향해서.

죽음의 공포로 서늘해지는 등골과 그럼에도 흔들리지 않는 마음속 확신을 애써 다잡으며.

“이게 무슨 짓……!”

그리고 적천강의 다급한 외침이 울려 퍼진 그 순간.

피핏!

목줄기의 좌우를 아주 미세하게 베어 내며 스쳐 지나간 두 자루의 날붙이에, 찰나의 고통조차 잊은 채 입꼬리를 말아 올렸다.

‘역시.’

내가 공격을 피해 낸 것이 아니다.

조금 전 목숨이 위태로워졌던 절체절명의 순간, 두 마리의 흑귀는 억지로 병장기를 비틀어 경로를 바꾸었다.

이유?

간단하다.

결코 나를 죽여서는 안 되니까.

지금 이 전장에서 그들을 통제하고 있는 우두머리가, 바로 혈검마군이 그렇게 지시했으니까.

‘아마 천산삼노였다면 그러지 못했겠지.’

아니, 정정한다.

그러지 못한 것이 아니라, 그러지 않았을 것이다.

흑귀들과는 달리 감정과 이성이 남아 있는 그들에게는 지시를 이행하는 것보다 자신들의 목숨이 백 배, 천 배는 더욱 소중했을 테니까.

나를 생포하기 위해 저지른 이 자그마한 실수가, 곧 그들의 죽음과 직결된다는 것을 알고 있었을 테니까.

바로 지금처럼.

슈확!

보이지 않던 빈틈, 그러나 스스로 드러낸 그 빈틈을 나는 놓치지 않았다.

퍼걱!

순간 석상처럼 굳어 버린 흑귀의 신형.

정확히 목울대를 관통한 백염의 창날을 타고, 내가 흘려보낸 사 갑자의 열양지기가 터져 나왔다.

퍼어엉!

폭발하는 화염.

머리가 송두리째 사라져 버린 흑귀의 신형이 말안장에서 굴러떨어지기 전, 동료의 위기를 뒤늦게 알아차린 또 다른 흑귀가 내 목줄기 옆을 스쳐 지나갔던 도신을 비틀어 휘둘렀다.

서걱!

뜨겁다. 풍압만으로도 베여 나간 어깻죽지에서 붉은 핏물이 솟구쳤다.

그러나 잃은 것이 있으면, 얻는 것 또한 있는 법이다.

콰득.

순간 소름이 끼칠 만큼 차가운 감촉.

칠흑색 갑주로 둘러싸인 놈의 손목을 다른 한 손으로 잡아챈 나는, 한 치의 망설임도 없이 쥐어 짜내듯 비틀었다.

까득. 우드득.

섬뜩한 파육음과 함께 짓뭉개지는 살과 뼈.

흑귀가 죽음을 딛고 새롭게 거듭나는 과정에서 더욱 강한 힘을 얻었다면, 나는 무수한 죽음의 위기를 넘기며 인간의 한계를 넘어섰다.

그렇기에 지금 이 순간, 이 자리에 존재하는 괴물은 놈들뿐만이 아니다.

우지지직!

병장기를 쥔 손목을 그대로 뽑아 버린 나는, 멍하니 굳어 버린 놈을 향해 주먹을 뻗었다.

콰앙!

산산조각 나는 흑색 갑주와 함께 고약한 탄내를 풍기며 나가떨어지는 몸뚱어리.

그러나 나는 안다.

놈들이 어느 정도의 괴물인지.

놈들에게 추가로 주어진 저주받은 생명력이, 얼마나 끈질기고 끔찍한 것인지.

저벅.

이미 또 다른 흑귀 두 마리와 뒤얽혀 싸우고 있는 적천강을 뒤로한 채, 나는 어느덧 비틀비틀 일어나는 흑귀들을 향해 걸음을 내디뎠다.

“그래, 어디 한번 가려 보자.”

스아아아.

전신을 휘감으며 피어오르는 거무스름한 안개로 무참하게 뽑혀 나간 팔을, 화염에 의해 녹고 바스라진 뼈와 살을, 심지어는 사라진 목까지 재생시키는 괴물들을 향해.

“어떤 놈이 더 괴물인지.”

슈화아악, 서걱!

화룡일미(火龍一尾).

눈이 부시도록 흰 창날을 휘감으며 불길처럼 타올라, 벽력처럼 안개를 가로지른 일격이 검푸른 파도가 되어 놈들을 베어 갈랐다.



* * *



“엄청나군. 아주 대단해!”

마치 생일날 마음에 드는 장난감을 선물 받은 어린아이처럼, 혈검마군은 한껏 상기된 얼굴로 눈 앞에 펼쳐진 전장을 바라보았다.

차차차창!

높은 언덕 위에서부터 저 멀리 펼쳐진 설원까지.

수백여 장을 빽빽하게 뒤덮은 도산검림(刀山劍林)이 춤추고 있다. 번뜩이는 섬광이, 오직 한 가지 목적을 위해 끊임없이 달구고 식혀졌던 그 날붙이들이 마침내 자신의 역할을 해내고 있었다.

퍼걱!

끄아아아악!

온 사방에서 빗발치는 고함과 비명 사이, 붉디붉은 핏물이 분수처럼 모두의 머리 위에 흩뿌려진다.

들숨 한 번에 수십의 생명이 사라지고, 날숨 한 번에 그 빈자리가 채워진다.

그리고 지금 이 순간에도 죽음의 연쇄가 끝없이 이어지는 그 참혹한 현장은, 오랜 세월 동안 사막 너머에만 머물러야 했던 누군가의 향수를 자극하기에 충분했다.

“이거야. 바로 이거라고…….”

반쯤 넋이 나간 목소리로 중얼거린 혈검마군의 눈동자는 어느덧 몽롱하게 젖어 있었다.

얼마나 그리웠던가.

어찌나 바래 왔던가.

이제는 까마득해져 버린 과거, 천마라 불리던 이의 곁에서 십만 마도를 이끌고 천하를 가로질렀던 적이 있었으나 혈검마군에게 있어 그 시절의 기억은 퍽 즐겁지 않았다.

혈검마군은 그때에도 피에 미친 한 마리 사냥개였을 뿐이었고, 천마는 그런 그에게 별다른 지휘권을 주지 않았으니까.

하지만 이제는 다르다.

새로운 주인은 혈검마군에게 수만 명의 생사 여탈권을 안겨 주었다.

그 어떤 경우에서도 진태경을 죽여서는 안 된다는, 아주 간단한 하나의 조건만을 전하며.

‘이토록 전폭적인 신뢰를 보여 주시다니.’

무려 일곱이나 되는 흑귀를 내주었다는 것이 바로 그 결정적인 증거다.

그리고 그와 더불어…….

‘저들까지 있는 한, 이 전투는 어떤 경우에서도 결코 질 수 없다.’

문득 전장에서 눈을 뗀 혈검마군은 얼마 떨어지지 않은 곳에서 삼엄한 호위를 받고 있는 백의인들을 바라보았다.

흑귀들에 비해서도 결코 뒤떨어지지 않는, 어쩌면 오히려 더욱 강력한 전력이 될 수도 있을 그들을.
```

## Final English reading copy

```markdown
# Chapter 1033

Every martial art contains at least dozens of movements, each with its own underlying principles.

But no matter what martial art you’ve learned, there are ultimately only two ways to deal with an enemy’s attack.

Block it, or dodge it.

And in this moment, I chose the latter.

KWA-BOOOOM! KRRRUNCH!

A flash of light came hurtling in with a fierce whistle and slammed into the ground.

The earth’s surface flipped over as if an earthquake had struck, and a tremendous shock wave swept through the area.

At least a dozen enemies were caught in its wake and vanished without a trace. Yet all I’d suffered was a few scratches from flying bits of rock—and my spine still went cold.

*Fast. And powerful.*

It was hard to believe a javelin could move that fast and hit that hard after being thrown from so far away.

In that sense, dodging had hardly been a choice. I’d had no other option.

If I’d counterattacked at once, even that would have cost me a considerable amount of strength.

Jeok Cheongang, standing beside me, knew that too.

“I suspected as much, but those bastards certainly don’t have ordinary internal energy.”

Jeok Cheongang muttered in a low voice and clenched his fist.

In the distance, in the direction of his gaze, four ghost horses were approaching us, each carrying a rider. They stepped through the air as they came.

“Four, huh? How many passed us by earlier?”

The Great Snow Mountain region might not be as vast as the Qilian Mountains, but it was still enormous.

The land at the foot of the mountain, lightly covered in frost, was broad enough for a massive battle like this one, with countless enemies and allies tangled together. Jeok Cheongang and I had broken through the enemy lines ahead of everyone else like a single awl, but we couldn’t stop them all.

Besides, the most important thing in winning a battle was cutting off the head, not the body.

“If I saw right, two.”

I recalled the distant crash and tremor I’d felt before the javelin came flying.

Judging by their direction and distance, they were…

“I think those two headed toward the Zhongnan Sect.”

The Zhongnan Sect had only a thousand soldiers among our army of thirty thousand, but every one of them was an elite of the main sect, not an affiliated branch. With three Supreme Peak masters among them, they were a formidable force.

If the enemy wanted to secure victory, stopping them would be crucial.

“Then that makes five, counting the ones who’ve just appeared.”

We’d already let two slip past, and now four more had shown up.

But the monsters called Death Knights—or Black Ghosts—numbered seven in all, as far as we knew.

I adjusted my grip on White Flame and murmured, “One’s unaccounted for.”

“Then the last one…”

“Either guarding the Blood-Sword Demon Lord, or headed toward the Gansu martial artists led by Sima Gong. Unless it’s the latter…”

I let my voice trail off, but Jeok Cheongang already knew about Sima Gong’s suspicious behavior. No more explanation was needed.

“So that means Sima Gong, that damned unorthodox bastard, has thrown in his lot with Dark Heaven.”

That was right.

The fact that a Black Ghost hadn’t gone to Sima Gong’s side didn’t prove anything on its own, but there was no denying the likelihood of betrayal had risen sharply.

If I were the Blood-Sword Demon Lord, I wouldn’t bother sending a Black Ghost to Sima Gong if he was already an ally.

And besides…

*With power like that, all the more reason.*

I watched the Black Ghosts draw closer, radiating a terrifying aura.

They carried a saber, a sword, a spear, and a kusari-gama—a sickle attached to a chain. They sprang over the heads of the advancing enemy soldiers and shot toward us.

Each one was a Supreme Peak master powerful enough to shake an entire city.

On top of that, they felt neither pain nor emotion, and their ability to recover was beyond human. No—they were already complete monsters.

The likes of which no one in Murim had ever encountered.

“Old Master.”

“Nothing more to say.”

KRRUNCH!

Even now, Jeok Cheongang smashed the head of an enemy charging at him with soulless eyes in a single punch. Then he continued,

“I don’t know what kind of monsters those things are, but all we have to do is keep killing them until they’re dead.”

The instant those words slipped quietly from his lips—

Pop.

We kicked off the ground and shot forward, swinging and thrusting with all our strength.

I drove the spearhead of White Flame, its dark-blue Force surging around it. Jeok Cheongang thrust out a palm wreathed in pure white flames.

FWOOOOSH!

A brilliant flash enveloped everything within a radius of more than ten *jang*. The waves of fanatics that had been flooding in from every direction split apart.

No—they evaporated.

KWAANG! KRRRUNCH!

The ground shook with a crash that sounded as if the sky itself had split.

Bodies charred in an instant beneath the Flame Divine Palm’s terrible heat crumpled lifelessly. Others were cut apart along with their weapons, then flung in pieces through the air.

Even though they’d been stripped of pain and emotion, death came equally to the hundred or so enemies whose lives ended in that moment.

And through the gap in the battlefield, blanketed in death in an instant—

Ssshh…

Four Black Ghosts came rushing toward Jeok Cheongang and me, shrouded in a deathly energy like twilight fog.

SHWING!

The wind split around the blades as they swept through the air with crushing force.

Each of them took one of the four directions and struck. Their attacks meshed like the teeth of finely crafted gears, leaving not even the slightest opening.

But…

*There is an opening. There has to be.*

I took a bold step forward against the sword blade and spearhead rushing toward me, leaving faint afterimages.

Toward those two chilling flashes, aimed straight at my neck.

I steadied the conviction in my heart even as fear of death chilled my spine.

“What are you—!”

And just as Jeok Cheongang’s urgent shout rang out—

Pshk!

The two blades grazed the sides of my neck, cutting them so slightly that I felt no more than a moment’s pain. I curled up the corners of my mouth.

*Just as I thought.*

I hadn’t dodged their attacks.

In the life-or-death moment just now, the two Black Ghosts had forced their weapons to twist and change course.

Why?

Simple.

They weren’t allowed to kill me.

Their commander on this battlefield—the Blood-Sword Demon Lord—had given them that order.

*The Three Elders of Tianshan wouldn’t have been able to do that.*

No, I take that back.

They wouldn’t have done it.

Unlike the Black Ghosts, they still had their emotions and reason. Their own lives would have mattered a hundred, a thousand times more to them than carrying out an order.

They would have known that making even a tiny mistake like this to capture me would lead straight to their deaths.

Just like now.

SHWOOOSH!

I didn’t miss the opening that had been invisible until they exposed it themselves.

THUD!

The Black Ghost’s body went rigid, like a statue.

As White Flame’s spearhead pierced its throat, the four jiazi of Scorching Yang Qi I’d poured into it erupted.

KABOOOM!

Flames exploded.

Before the Black Ghost’s body, its head blown clean off, could fall from the saddle, another Black Ghost belatedly realized its comrade was in danger. It twisted the saber that had just passed beside my neck and swung it at me.

SHNK!

Hot. Even the force of the wind sliced into my shoulder, and red blood gushed from the wound.

But when you lose something, there’s always something to gain, too.

KRRUNCH.

A touch so cold it sent a shiver through me.

I seized the wrist of the Black Ghost, its body encased in jet-black armor, with my other hand. Without hesitation, I twisted it as if to wring it out.

CRACK. KRRUNCH.

Flesh and bone crushed with a sickening, wet sound.

If the Black Ghosts had gained greater strength by dying and being reborn, then I’d surpassed human limits by surviving countless brushes with death.

So the Black Ghosts weren’t the only monsters standing here.

KRRRUNCH!

I tore off its wrist, weapon still gripped in its hand, and punched the Black Ghost as it stood frozen in confusion.

KWAANG!

The body went flying, trailing a foul, burnt stench as its black armor shattered.

But I knew.

I knew what kind of monsters they were.

I knew how tenacious and dreadful the cursed life they’d been given was.

Step.

Leaving Jeok Cheongang behind as he fought two other Black Ghosts, I walked toward the ones now staggering back to their feet.

“Fine. Let’s see how this goes.”

Ssshh…

The monsters were wrapped in a rising, dusky mist that regenerated their arms, torn brutally away; their flesh and bones, melted and crumbled by the flames; even their missing necks.

“Let’s see which of us is the bigger monster.”

SHWOOOOSH—SHNK!

Fire Dragon’s Single Tail.

The dazzling white spearhead blazed like a flame. Its strike cut through the mist like a bolt of lightning, turning into a dark-blue wave that cleaved through the Black Ghosts.

* * *

“Magnificent. Absolutely magnificent!”

Like a child who’d just been given a toy he loved on his birthday, the Blood-Sword Demon Lord watched the battlefield spread before him, his face flushed with excitement.

CLANG-CLANG-CLANG!

From the high hill to the snowy plain in the distance, a mountain of sabers and a forest of swords stretched for hundreds of *jang*. They danced. Those gleaming blades, forged and tempered for one purpose alone, were finally playing their part.

THUD!

“AAAGH!”

Shouts and screams poured in from every direction as crimson blood sprayed over everyone’s heads like a fountain.

Dozens of lives vanished with a single breath in—and the gaps they left were filled with a single breath out.

Even now, death followed death without end across the horrific battlefield. It was enough to stir the nostalgia of someone who’d spent so many years confined to the lands beyond the desert.

“This is it. This is what I wanted…”

The Blood-Sword Demon Lord murmured in a half-dazed voice. His eyes had grown hazy and moist.

How he’d missed it.

How he’d longed for it.

In the distant past, he’d led a hundred thousand followers of the Demonic Path across the land at the side of the one called the Heavenly Demon. But those memories weren’t especially pleasant for the Blood-Sword Demon Lord.

Even back then, he’d been nothing more than a hunting dog mad for blood, and the Heavenly Demon had given him little authority to command.

But now things were different.

His new master had given the Blood-Sword Demon Lord the power to decide the lives and deaths of tens of thousands.

All he’d been given was one simple condition: under no circumstances was he to kill Jin Taekyung.

*To show me such absolute trust…*

The decisive proof was the seven Black Ghosts he’d been given.

And besides…

*With them there, there’s no way we can lose this battle.*

The Blood-Sword Demon Lord finally looked away from the battlefield and turned his gaze toward the white-robed figures under heavy guard not far away.

They were no less powerful than the Black Ghosts. If anything, they might be an even greater force.
```
