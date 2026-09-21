<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0604.txt",
      "sha256": "c0bf933ada2fbe50d18bf357a2ca1432d30775c72874dc0a5fbba3305cb8d343",
      "bytes": 13402
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0979c623b3623399b11071e2901360a55ee52c573e5fb01aa7c6ec7de5e7884c",
      "bytes": 1686
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d81d7edd24906e3aee66aaa9a41def52d8be239d693519df1ebd48b41b2895c7",
      "bytes": 187002
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "b3e055212feb5275e033504a00f95a2db0b4518de3283263b63435137bdd215c",
      "bytes": 727
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "196bc54879c741b8cebc2334323b564cf76aaf867c7ba475cf15a6b8fbce9e8f",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "80cf9763f8cb5bae26d4dcf55d5b3e3bcf841cd90be855e68d9ea4df91a1e1f8",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8125d7defe3534c40169a1da247207a8f918e90a63db23c8a4370ea764776e46",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d03567fa57b1dd2b7055bfd9eb1605126baf93cd9b1c5a14b1f96b20d53b7963",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d34b676f508146881354cb897ae87fbe5262bfe87f1e85e7465c5085469a2379",
      "bytes": 1384
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d7c3b059f57eb1c7305459103da54e5e295a5000a3501d63c5aea3f1402ee86c",
      "bytes": 186477
    }
  ],
  "estimated_tokens": 10960
}
-->

# Durable State Update — Chapter 604

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 604. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 604. Profile updates may replace only one
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
  "chapter": 604,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 604,
    "continuity_sources": [604],
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
    "Cheon Taemin has been unconscious for more than twenty years and remains hidden in a secret area within Ares Guild's Area A.",
    "Jin Taekyung has detected another concealed space in Area A, but its entrance, contents, and access method remain unknown.",
    "Lee Jungryong and Song Cheonwoo concealed Cheon Taemin's condition, and Choi Minwoo now controls the Guild power needed to investigate his fate.",
    "Choi Minwoo has publicly identified himself as Cheon Taemin's maternal grandson and only living blood descendant.",
    "Choi Minwoo is Guild Master of the Peace Guild and Vice Guild Master of Ares Guild.",
    "Baek Hanseong and Choi Minwoo have established a cooperative relationship concerning the two Guilds and the government's response.",
    "Go Se-won remains the person closest to the surviving secrets of Ares Guild and has not explained what debt he intends to repay to Jin Taekyung."
  ],
  "continuity_sources": [
    603
  ],
  "open_questions": [
    "How can the newly detected hidden space in Area A be entered, and what does it contain?",
    "What caused Cheon Taemin to lose consciousness and remain in a vegetative state for more than twenty years?",
    "What debt does Go Se-won mean to repay to Jin Taekyung?",
    "How will the authorities ultimately resolve the charges against Jin Taekyung?"
  ],
  "safe_through": 603,
  "temporary_decisions": [
    "Use Team Leader Choi for 최 팀장.",
    "Use Butler Kim for 김 집사.",
    "Use President's Security Service for 청와대 경호실.",
    "Use maternal grandfather for 외조부님.",
    "Use Guild Association for 길드 협회."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 애틀랜타 | **Atlanta** | The U.S. city claimed as the Skeleton King's birthplace. |
| 조지아주 | **Georgia** | The U.S. state claimed as the Skeleton King's birthplace. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 정기 | **vital essence** | Energy the Wudang Sect Leader says the monster absorbs from victims. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 603
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm; he has been unconscious for more than twenty years and is hidden from the world in a secret area within Ares Guild's Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 601
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 603
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 603
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 603
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 603
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

## Korean source

```text
＃604화



띠링.



- [중단전]에 관한 깨달음을 얻었습니다!

- [중단전]이 일부 활성화됩니다!

- [중단전] 활성화 : 10%

- 모든 무공과 공력의 효율이 소폭 증가하며, 때에 따라 한계 이상의 힘을 발휘할 수 있습니다!

- 희귀한 업적, [응애 나 애기 중단전]을 달성했습니다!

- 업적 달성 보상으로 대량의 경험치를 획득했습니다!

- 레벨 업!



‘활성화?’

이건 예상 못 했는데.

중단전을 개방한 건 한 달도 더 된 일이지만, 이런 효용이 있을 줄은 몰랐다.

그리고 뜻밖의 보상을 알리는 시스템 알림에 이어, 기다렸던 소식이 들려왔다.

띠링.



- [기감]의 범위가 확장됩니다!

- 목표 대상을 정확히 파악할 수 없습니다!

- 정체를 알 수 없는 기이한 힘이 느껴집니다!



목표 대상을 파악하는 것에는 실패했지만, 이건 실패가 아닌 성공이다.

이 벽 너머에 무언가가 존재한다는 확신을 얻은 나는, 망설임 없이 벽을 향해 일권(一拳)을 후려쳤다.

꽈앙!

단단한 벽이 터져 나가자 텅 빈 허공이 모습을 드러낸다.

아레스 길드 본사 최상층에 숨겨진 A구역은 각종 결계와 투명 마법. 그리고 중력 마법으로 유지되고 있었다.

당연하게도 정부에서 파견된 조사팀 역시 이 사실을 알고 있었을 것이다.

문제는, 가장 중요한 한 가지를 놓쳤다는 거다.

‘아니, 놓칠 수밖에 없었겠지.’

나는 무너진 벽 너머로 손을 뻗어 허공을 어루만졌다. 아무것도 느껴지지 않는, 말 그대로 텅 빈 허공. 최 팀장의 손에 들린 마나 측정기도 여전히 잠잠하다.

하지만 내게는 확신이 있었다. 이 너머에 반드시 무언가 있으리라는 확신이.

화륵.

삼 갑자의 열양지기가 불꽃으로 화한다. 청백색의 화염이 깃든 두 손을 말없이 내려다보던 나는, 지그시 눈을 감은 채 손을 뻗었다.

‘보이는 것이 전부가 아니다.’

이것은 인지의 문제다. 눈이 아닌 본능과 감각으로, 마음으로 보고 느껴야 한다.

심혈을 기울여 집중하고 아낌없이 공력을 흘려보내자 미약하게나마 열린 중단전이 호응했다.

일렁이던 불꽃이 서서히 가라앉으며 손 전체를 완전히 휘감는다.

압축. 정제(正體).

그리고…….

콰득.

마침내 손아귀에 잡힌 기(氣)의 흐름을, 나는 힘주어 찢어 벌렸다.

촤아아악!

청백색의 화염과 함께 허공이 갈라졌다.

나로서는 알 수 없는 온갖 마법이 강기에 의해 해제되고, 새로운 공간의 틈새가 모습을 드러낸다.

눈앞에서 벌어진 광경을 멍하니 바라보던 스켈레톤 킹과 최 팀장이 중얼거렸다.

“찌, 찢었다.”

“아니, 이걸 도대체 어떻게…….”

“원래 몸이 나쁘면 머리가 고생하는 법이지. 갑시다.”

“……보통은 그 반대 아닙니까?”

“그렇죠. 보통은.”

근데 난 보통이 아니잖아.

아무렇지 않게 대답하는 내 모습에, 최 팀장이 손에 든 마나 탐지기를 등 뒤로 내던졌다.

음. 역시 몸 좋은 게 최고다.



* * *



혹시 모를 상황을 대비해 최상층을 비워 둬서 다행이었다.

그렇지 않았다면 정체를 알 수 없는 아공간(亞空間)으로 진입하는 걸 실시간으로 생중계할 뻔했으니까.

스윽.

세로로 길게 갈라진 틈새 안으로 몸을 내딛자, 그곳에는 완전히 다른 세상이 펼쳐져 있었다.

‘뭐야, 이게.’

사방이 넓고, 높았다. 그리고 내게는 낯선 기품과 화려함이 뒤섞여 있었다.

뒤따라 진입한 최 팀장과 스켈레톤 킹도 순간 할 말을 잃은 채 주위를 둘러보기 바빴다.

“저건…….”

바닥에 깔린 부드러운 융단을 밟으며 걸어간 최 팀장의 눈빛이 가늘게 떨렸다.

드넓은 복도에 걸린 그림을 찬찬히 훑어본 그가 중얼거렸다.

“살바토르 문디.”

나는 불쾌한 목소리로 물었다.

“지금 저한테 문디라고 한 겁니까?”

“그게 아니라, 저 그림 제목입니다. 살바토르 문디요. 레오나르도 다빈치의 걸작인데 한 번도 못 들어 보셨습니까?”

“우리 엄마한테는 가끔 들었는데요. 고향이 경상도시라.”

“…….”

“표정 뭐예요. 지금 경상도 무시합니까? 최 팀장님 지역 감정 있는 분이셨어요?”

“뭐? 지역 감정?”

최 팀장이 한 말이 아니다. 주위를 둘러보던 스켈레톤 킹이 기분 나쁜 표정으로 불쑥 끼어들었다.

“지역 감정은 반드시 없어져야 하지. 그런 의미에서 마계 출신인 이 몸 역시 간악한 인간의 의견에 동조한다.”

“언데드 새끼가 은근슬쩍 뼈다귀 올리는 것 보소. 넌 빠져.”

“아니, 기분 더럽네. 왜 도와줘도 지랄인가?”

“마계로 따지면 지역 감정이 아니라 차원 감정이잖아, 시벌놈아. 말만 들으면 무슨 마계가 지리산 옆에 붙어 있는 줄 알겠네.”

“내가 활동하던 게이트는 부천에 있었다. 물론 나는 미국 조지아주 애틀랜타 출신이지만.”

“미친놈인가, 진짜.”

차원과 국경을 넘나드는 스켈레톤 킹과 입씨름을 하는 사이, 일찌감치 대화를 포기한 채 복도 이곳저곳을 오가며 닫힌 문을 열어 보던 최 팀장이 불쑥 입을 열었다.

“두 분 모두, 그만하시고 이리 와 보십시오.”

스켈레톤 킹이 선비처럼 꼿꼿한 태도로 대답했다.

“이 몸은 언데드의 군주. 지역 감정으로 찌든 인간의 말은 듣지 않는다.”

“줘 터지기 싫으면 따라와.”

나는 헛소리를 지껄이는 녀석의 멱살을 붙들고 걸음을 옮겼다.

그리고 최 팀장의 손짓을 따라 활짝 열린 문 안을 확인한 순간, 왜 그가 나를 불렀는지 깨달았다.

“이건…….”

불 하나 켜져 있지 않았음에도 문 안은 낮처럼 환했다. 바로 진열대 위에 가지런히 놓인 마정석들 때문이었다.

그중 기본이 A급 마정석이었고, 눈대중으로 어림잡아 파악만 개수만으로도 무려 오백여 개에 달했다.

‘이걸 돈으로 환산하면 도대체 얼마지?’

짐작조차 할 수 없을 만큼 천문학적인 가치.

더군다나 맨 윗줄에서 가장 밝은 빛을 토해 내는 다섯 개의 S급 마정석은 돈이 있어도 구하기 힘든 보물이다.

“그럼 이게 전부……?”

말꼬리를 흐리는 나를 향해, 최 팀장이 작게 고개를 끄덕였다.

“이정룡이 빼돌린 것이 분명합니다. 지금까지 확인해 본 바에 의하면 다른 방도 마찬가지예요.”

“이런 미친…….”

“마정석은 물론이고 금괴와 다이아, 채권 등의 현물. 그리고 대격변 이후 사라졌다고 알려진 각종 예술품이 가득합니다.”

최 팀장의 말은 사실이었다. 긴 복도의 양옆에 줄지어 늘어선 문을 열어젖힐 때마다, 막대한 값어치를 지녔거나 값어치를 매기기 힘든 보물들이 모습을 드러냈다.

상상 이상의 스케일에 머릿속 계산기는 이미 박살 난 지 오래다.

‘어느 정도 예상은 했지만…… 정말 많이도 해 처먹었군.’

대격변 이후 게이트와 마정석의 존재는 제2의 오일 머니(Oil Money). 아니, 그 이상으로 자리 잡았고 거대 길드는 막강한 기업을 짓누를만한 부와 위상을 갖게 되었다.

이런 상황에서 이정룡의 부가 막대할 것이라는 사실은 나를 포함한 모두가 짐작하고 있었으나, 밝혀진 것 외에도 숨겨진 재산이 이 정도로 많을 줄은 누구도 몰랐을 것이다.

‘금고.’

순간 머릿속을 스친 단어.

맞다. 이곳은 이정룡이 만들고 석고준에게 물려 준 그들만의 개인 금고다.

그러나 잊지 말아야 할 것은, 이 공간이 막대한 부를 감춘 금고인 동시에 감옥이라는 사실이다.

‘한 사람의 존재를 세상으로부터 숨기기 위한 감옥.’

하지만 단둘뿐이던 간수는 이미 죽음을 맞이했고, 지금 내 옆에는 이 공간의 새로운 주인이 마지막 문을 향해 걸어가고 있었다.

저벅. 저벅.

기나긴 복도의 끝, 굳게 닫힌 문을 향해 나아가는 최 팀장의 걸음걸이에서 숨길 수 없는 떨림이 느껴진다.

“후.”

동요를 가라앉히기 위해 작게 심호흡하는 그를 대신해, 나는 망설임 없이 앞으로 나섰다.

막대한 마나의 흐름이 느껴지는 문을 향해 거침없이 수도(手刀)를 내리긋자 한 줄기 불꽃이 허공을 스쳤다.

서걱! 쿠웅!

각종 마법이 해제되고 합금으로 만들어진 문이 양옆으로 갈라진다.

동시에 그 너머에 웅크리고 있던 어둠과 싸늘한 냉기가 우리를 덮쳤다.

솨아아악.

알 수 없는 오한이 전신을 엄습했다.

이미 한서불침(寒暑不侵)의 경지에 접어든 나도, 심지어는 죽음과 냉기를 근원으로 한 존재인 스켈레톤 킹조차도 몸을 떨었다.

그러나 한 사람만큼은 예외였다.

저벅.

어두운 공간 속, 유난히도 크게 울려 퍼지는 발걸음 소리.

말없이 걸어가는 최 팀장의 뒷모습에서 더 이상의 떨림이나 망설임은 찾아볼 수 없었다.

이십여 년.

아이는 소년이 되었고, 소년은 청년이 되었다.

일찍이 부모를 잃은 아이는 영문도 모른 채 외조부와 헤어졌으며, 마침내 자신의 자리로 돌아와 이곳에 섰다.

자신의 유일한 혈육을 대면하기 위해, 진실을 확인하기 위해.

“그리워했고, 언제나 그리웠습니다.”

저벅.

끊임없이 앞으로 나아가던 발걸음이 어느 순간, 갑작스럽게 멈췄다.

어느덧 그의 앞에는 수많은 전선이 연결되어 있는 커다란 타원형의 기계 캡슐이 놓쳐져 있었다.

마치 SF 영화에 등장할 법한 그 기계는 동면(冬眠)을 위해 마련된 장치처럼 보였고, 살아 있는 사람을 위해 마련된 관과 같았다.

후우.

서늘한 공기 속, 최 팀장의 입술 사이로 뿜어진 입김이 먼지로 뒤덮인 유리를 뿌옇게 물들인다.

잘게 떨리는 긴 손가락이 유리를 쓸어내렸다.

“뵙고 싶었습니다.”

닦여나가는 먼지와 함께, 비로소 한 사람의 얼굴이 드러난다. 인터넷에 떠도는 사진과는 달리 늙고 지쳐 보이는 얼굴.

그러나 서로의 핏줄이라는 것을 증명하듯 빼닮은 노인을 향해, 최 팀장이 나직한 목소리로 말을 이었다.

“외할아버지.”



* * *



최 팀장은 모든 것을 극비에 부쳤다.

적어도 지금 당장은 나와 스켈레톤 킹을 제외한 그 누구도 이와 같은 비밀을 알 수 없었고, 그의 뜻에 나도 적극적인 동의를 표시했다.

물론 사소한 잡음이 있긴 했지만.

“비밀을 지켜 주는 건 어렵지 않지. 하지만 두 가지 조건이 있다.”

스켈레톤 킹은 독립투사처럼 결연한 표정으로 자신의 조건을 읊었다.

“첫 번째. 클럽에 데려다줄 것. 두 번째. 저 안에 있는 S급 마정석을 내게 줄 것.”

최 팀장은 첫 번째 제안을 흔쾌히 수락했지만, 두 번째 제안은 달랐다.

그리고 심도 있게 고민하는 그에게 나는 명쾌한 대안을 제시해 주었다.

“더 좋은 방법이 있긴 해요.”

“뭡니까?”

“지금 S급 마정석이 몇 개죠?”

“아직 다섯 개가 남아 있습니다.”

“그럼 저 새끼를 조지고, 여섯 개로 만듭시다. 비밀도 유지하고 S급 마정석도 추가 확보할 수 있어요.”

“……!”

“……!”

독립투사의 심정으로 제안을 요구했던 스켈레톤 킹은 친일파가 되어 협력했고, 클럽에 데려다주는 것으로 극적인 합의점을 찾았다.

그러나 가장 중요한 한 가지, 천태민의 거취에 관해서는 어쩔 수 없이 누군가의 도움을 빌려야 했다.

“이곳에 외할아버지를 계속 모셔 둘 수는 없습니다. 다른 곳으로 옮겨야 해요.”

“문제는 누구의 눈에 띄지 않고 이동해야 한다는 건데…….”

그건 공간 확장 마법이 걸려 있는 포켓이나 내 인벤토리로도 할 수 없는 일이었다.

불멸의 영웅, 천태민은 엄연히 살아 있는 사람이었으니까.

결국 고민 끝에 나온 답은 하나뿐이었다.

“공간 이동 마법으로 옮겨야 합니다.”

중요한 건 사람이었다.

가장 믿을 만한 사람. 설령 이 사실을 안다 해도 발설하지 않을 사람.

그리고 의식불명에 빠진 천태민과 우리에게 호의적이며 계속해서 도움을 줄 수 있는 사람…….

“딱 한 사람이 떠오르네요.”

“아마 제 생각도 진태경 씨와 같을 겁니다.”

그런 이유로 나는 한 사람에게 전화를 걸었다.

“잠깐 한국 오실 수 있어요?”

- 헤이, 진. 나도 바빠. 지금 변이 게이트가…….

“최 팀장이 보고 싶대요. 뽀뽀 쌉가능.”

- 당장 갈게.
```

## Final English reading copy

```markdown
# Chapter 604

*Ding.*

> **System**
>
> - You have gained enlightenment regarding **Middle Dantian**!
> - **Middle Dantian** is partially activated!
> - **Middle Dantian** activation: 10%
> - The efficiency of all martial arts and internal energy has increased slightly, and you may occasionally exert strength beyond your limits!
> - You have achieved the rare Achievement **Waaah, I’m a Baby Middle Dantian**!
> - You have gained a large amount of EXP as an Achievement reward!
> - Level Up!

*Activated?*

I hadn’t expected this.

It had been more than a month since I opened my Middle Dantian, but I never imagined it would come with benefits like these.

And then, following the System notification announcing an unexpected reward, the news I had been waiting for arrived.

*Ding.*

> **System**
>
> - The range of **Qi Sense** is expanding!
> - The target cannot be identified precisely!
> - An unidentified, strange power is being sensed!

I had failed to identify the target, but this wasn’t a failure. It was a success.

Certain that something existed beyond this wall, I punched it without hesitation.

Boom!

As the solid wall exploded, empty space was revealed.

The hidden Area A on the top floor of Ares Guild headquarters was maintained by various barriers, invisibility magic, and gravity magic.

Naturally, the government investigation team must have known this as well.

The problem was that they had missed the most important thing.

*No. They couldn’t have helped missing it.*

I reached through the collapsed wall and stroked the empty air. It was literally empty—nothing could be felt. The mana detector in Team Leader Choi’s hand remained silent.

But I was certain. Something had to exist beyond this point.

Fwoosh.

Three jiazi of Scorching Yang Qi transformed into flame. I silently looked down at my hands, bluish-white flames flickering over them, then closed my eyes and reached out.

*What you see isn’t everything.*

This was a matter of perception. I had to see and feel with my instincts, my senses, and my heart—not my eyes.

I focused with all my might and poured out my internal energy without restraint. My faintly opened Middle Dantian responded.

The flickering flames gradually settled, completely enveloping my entire hand.

Compression. True Form.

And then…

Crack.

I gripped the flow of qi in my grasp and tore it apart with all my strength.

Shraaak!

The empty air split apart alongside the bluish-white flames.

All kinds of magic beyond my understanding were dispelled by Force, and a gap leading into a new space appeared.

The Skeleton King and Team Leader Choi stared blankly at the scene unfolding before them and muttered.

“He tore it.”

“No, how in the world did you…”

“When your body is bad, your head has to work harder. Let’s go.”

“…Isn’t it usually the other way around?”

“Usually, yes.”

*But I’m not ordinary.*

At my casual answer, Team Leader Choi threw the mana detector in his hand behind him.

Hmm. Having a good body really was the best.

* * *

It was a good thing we had cleared out the top floor in preparation for any unexpected situations.

Otherwise, we might have ended up live-streaming our entry into an unidentified subspace.

Swoosh.

When I stepped into the long vertical gap, a completely different world unfolded before me.

*What the hell is this?*

It was vast in every direction, with a high ceiling. It was also filled with a blend of unfamiliar elegance and extravagance.

Team Leader Choi and the Skeleton King entered behind me and immediately became too busy looking around to speak.

“That’s…”

Team Leader Choi’s eyes trembled faintly as he walked across the soft carpet covering the floor.

He slowly examined the paintings hanging along the vast corridor before muttering.

“Salvator Mundi.”

I asked in an offended voice.

“Did you just call me Mundi?”

“No. That’s the title of the painting. Salvator Mundi. It’s a masterpiece by Leonardo da Vinci. Have you really never heard of it?”

“I’ve heard that from my mom sometimes. Her hometown is in Gyeongsang-do.”[^1]

“…”

“What’s with that expression? Are you looking down on Gyeongsang-do right now? Team Leader Choi, are you one of those people with regional prejudice?”

“What? Regional prejudice?”

Team Leader Choi hadn’t said that. The Skeleton King, who had been looking around, suddenly butted in with an offended expression.

“Regional prejudice must be eliminated. In that spirit, this body, who hails from the Demon Realm, also agrees with the treacherous human’s opinion.”

“Look at this undead bastard trying to bone in on the conversation. Stay out of it.”

“No, this is pissing me off. Why are you cursing me when I’m helping you?”

“If we’re talking about the Demon Realm, that’s dimensional prejudice, you bastard. The way you talk, someone would think the Demon Realm was right next to Mount Jiri.”

“The Gate where I was active was in Bucheon. Of course, I’m from Atlanta, Georgia, in the United States.”

“Are you seriously insane?”

While I was arguing with the Skeleton King across dimensions and borders, Team Leader Choi—who had given up on our conversation early on—suddenly spoke up as he moved around the corridor, opening one closed door after another.

“Both of you, stop arguing and come over here.”

The Skeleton King answered with the stiff posture of a scholar.

“This body is the lord of the undead. I do not listen to the words of a human steeped in regional prejudice.”

“Follow me if you don’t want to get your ass kicked.”

I grabbed the collar of the idiot spouting nonsense and dragged him along.

The moment I followed Team Leader Choi’s gesture and looked inside the wide-open door, I understood why he had called me over.

“What is this…”

Even though not a single light was on, the room was as bright as day. The reason was the Magic Gems neatly arranged on the display shelves.

Even the lowest grade among them was A, and a rough visual estimate put their number at around five hundred.

*How much would all of this be worth in money?*

The value was astronomical—so high I couldn’t even begin to guess.

On top of that, the five S-grade Magic Gems emitting the brightest light from the top row were treasures that would be nearly impossible to obtain even for someone with money.

“So this is all…?”

As my voice trailed off, Team Leader Choi gave a small nod.

“Lee Jungryong definitely stole them. From what I’ve seen so far, the other rooms are the same.”

“This is fucking insane…”

“Not only Magic Gems, but also gold bars, diamonds, bonds, and other valuable assets. There are even countless works of art believed to have disappeared after the Great Cataclysm.”

Team Leader Choi was telling the truth. Every time we threw open one of the doors lining either side of the long corridor, treasures of immense value—or treasures too precious to put a price on—were revealed.

The calculator in my head had long since been smashed to pieces by the scale of it all.

*I had expected something like this to an extent… but he really took a hell of a lot.*

After the Great Cataclysm, the existence of Gates and Magic Gems had become the second Oil Money.[^2] No, they had become something even greater than that, giving the major Guilds enough wealth and influence to crush even powerful corporations.

Under those circumstances, everyone—including me—had assumed Lee Jungryong’s wealth would be enormous. But no one could have known there would be this much hidden wealth beyond what had already been uncovered.

*Vault.*

The word flashed through my mind.

Right. This was the private vault Lee Jungryong had built and passed down to Go Jun.

But there was one thing we couldn’t forget.

This place was both a vault concealing immense wealth and a prison.

*A prison meant to hide one person from the world.*

But the only two guards had already met their deaths, and the new owner of this space was walking toward the final door beside me.

Step. Step.

At the end of the long corridor, Team Leader Choi walked toward the tightly closed door. There was an unmistakable tremor in his steps.

“Hoo.”

He took a small, deep breath to calm himself, but I stepped forward without hesitation in his place.

I swung a hand blade down at the door, which radiated an enormous flow of mana. A streak of flame cut through the air.

Slice! Boom!

The various spells were dispelled, and the alloy door split apart to either side.

At the same time, darkness and bitter cold that had been crouching beyond it swept over us.

Whoooosh.

An inexplicable chill seized my entire body.

Even I, who had already reached the realm of Unaffected by Cold and Heat, shuddered. Even the Skeleton King, an existence born from death and cold, trembled.

But one person was the exception.

Step.

In the darkness, the sound of footsteps rang out unusually loudly.

There was no longer any tremor or hesitation in Team Leader Choi’s back as he walked forward without a word.

More than twenty years.

The child had become a boy, and the boy had become a young man.

The child who had lost his parents early had been separated from his maternal grandfather without understanding why. At last, he had returned to his rightful place and stood here.

To meet his only blood relative.

To confirm the truth.

“I missed you. I always have.”

Step.

His footsteps continued forward until, at some point, they suddenly stopped.

A large oval-shaped mechanical capsule, connected to countless wires, lay before him.

The machine looked like something out of a science-fiction movie. It appeared to be designed for hibernation—a coffin prepared for a living person.

Hoo.

In the chilly air, Team Leader Choi’s breath fogged the dust-covered glass.

His long fingers trembled faintly as they brushed the glass clean.

“I wanted to see you.”

As the dust was wiped away, a person’s face finally emerged. Unlike the photographs circulating online, the face looked old and exhausted.

But the old man looked so much like Team Leader Choi that it proved they shared the same blood.

In a quiet voice, Team Leader Choi continued speaking to him.

“Grandfather.”

* * *

Team Leader Choi kept everything top secret.

At least for the time being, no one besides the Skeleton King and me could know about this secret, and I wholeheartedly agreed with him.

Of course, there was one minor complication.

“Keeping a secret won’t be difficult. But I have two conditions.”

The Skeleton King recited his conditions with the determined expression of an independence activist.

“First, take me to a club. Second, give me one of the S-grade Magic Gems in there.”

Team Leader Choi readily accepted the first proposal, but the second was another matter.

As he considered it seriously, I offered a clear alternative.

“There is a better way.”

“What is it?”

“How many S-grade Magic Gems are there right now?”

“There are still five.”

“Then let’s beat that bastard up and make it six. We can keep the secret and secure an additional S-grade Magic Gem.”

“…!”

“…!”

The Skeleton King, who had demanded his terms with the spirit of an independence activist, became a pro-Japanese collaborator and cooperated, and we reached a dramatic compromise by agreeing to take him to a club.

But there was one crucial matter concerning Cheon Taemin’s future that we couldn’t solve on our own.

“We can’t keep my maternal grandfather here forever. We need to move him somewhere else.”

“The problem is that we have to move him without attracting anyone’s attention…”

That was something even a pocket enhanced with spatial expansion magic—or my inventory—couldn’t accomplish.

The Immortal Hero, Cheon Taemin, was most certainly still alive.

After much deliberation, only one answer remained.

“We have to move him using teleportation magic.”

The key was who that person would be.

Someone we could trust more than anyone else. Someone who wouldn’t reveal the secret even after learning it.

Someone sympathetic to both the unconscious Cheon Taemin and us, and able to keep helping us…

“One person comes to mind.”

“I believe I’m thinking of the same person as you, Mr. Jin.”

For that reason, I called someone.

“Can you come to Korea for a little while?”

—Hey, Jin. I’m busy too. There’s a mutated Gate right now—

“Team Leader Choi wants to see you. Kissing is absolutely on the table.”

—I'll come right now.

[^1]: “Mundi” sounds like *mundi*, a Gyeongsang dialect insult, which is why Taekyung misinterprets the painting’s title as a comment about him.

[^2]: “Oil money” refers to the immense wealth and influence generated by petroleum resources. Here, Taekyung is comparing the economic power of Gates and Magic Gems to—and beyond—that of oil-rich nations.
```
