<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0668.txt",
      "sha256": "e41ef8f402072dd734ec40d2d5cf523fe142f348a39016c07e6077e8b57b9b47",
      "bytes": 13173
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a9e60476209d743b7937c812e9f28cb43a5df5d1998a505206cb1ea746595db1",
      "bytes": 2227
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "950eed153fac4a4b4f92f4edd076c261e5fd622c9f275bfb27c22920782260ab",
      "bytes": 202223
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c640d3210b975a1539980977d8488535549ba23cab1e03f1f1c869923d60988b",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "673002f6297c4fff313abc98ba88718521ea0166d39c292065c9d9a694968a4c",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6b715349443301d8d296d0e23a3ad7fa519097b62053965135c91acac1cae53e",
      "bytes": 622
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "b8d99de4c9c8f523d567db56f9e4d7c37fe0303f8cad52f08b24ad8b8c45bc9f",
      "bytes": 795
    },
    {
      "path": "characters/Wonhu.md",
      "sha256": "275bbca6c934e91d92e934a7a3a573591fc39ba69e79bf12192df5b575a63c42",
      "bytes": 415
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "9daf7ffae3413a4971b347940d7454c4e6788e1a436067640f16e94c2c1b9c51",
      "bytes": 806
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "65f391124c1feb898c46644c4d85467fd74fcc5bd2d122f093a1a23d55509acb",
      "bytes": 207599
    }
  ],
  "estimated_tokens": 10607
}
-->

# Durable State Update — Chapter 668

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 668. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 668. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 668,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 668,
    "continuity_sources": [668],
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
    "Jin Taekyung remains imprisoned in the underground prison, with execution scheduled for noon in two days.",
    "The Beast Miao King and Yayul Mok are jointly risking their positions and lives to rescue Jin Taekyung and prevent a war between Nanman and the Central Plains.",
    "Yayul Mok and the Seven Miao Tigers have infiltrated the underground prison disguised as Bai warriors, but the rescue attempt has been discovered at the fourth-floor security checkpoint.",
    "Gisan and Dogok remain near the captured wardens while Wonhu leads the breakthrough with the other Seven Miao Tigers.",
    "Yayul Mok carries an antidote that will release the seal on Jin Taekyung's internal energy.",
    "An unidentified person has seized Yayul Mok at the entrance to a dark corridor.",
    "Twenty tribal chieftains, including Baeksang, support Jin Taekyung's execution as the agenda of tomorrow's final Tribal Grand Council.",
    "The Beast Miao King and Baeksang are sworn brothers whose opposing responses to their children's deaths have driven them apart.",
    "Baeksang remains visibly conflicted and has not summoned the guards to stop the rescue."
  ],
  "continuity_sources": [
    667,
    666
  ],
  "open_questions": [
    "Who seized Yayul Mok in the dark corridor?",
    "Can Yayul Mok and the Seven Miao Tigers reach Jin Taekyung and complete the rescue before the execution?",
    "Will the failed infiltration expose the Beast Miao King and Yayul Mok and trigger war with the Central Plains?",
    "Will Baeksang allow the rescue to proceed and abandon the execution supported by the twenty chieftains?",
    "What precisely happened to Hwi, and which supposed allies were responsible for abandoning him?"
  ],
  "safe_through": 667,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Retain underground prison for 뇌옥 and use Dizziness Acupoint for 훈혈.",
    "Capitalize Will when referring to the System-linked martial concept 의지.",
    "Use Middle Dantian and Three Dantians for 중단전 and 삼단전."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 중원     | **Central Plains**                               |                                                       |
| 일격     | **One Strike**                         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 원후 | **Wonhu** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 운철 | **meteorite iron** | Material whose strength is used as a comparison for the black-wood fishing rod. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 칠묘호 | **Seven Miao Tigers** | The Beast Miao King's personal guard, composed of elite Miao warriors. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 원후 | Young_Palace_Lord_to_elder_personal_guard | Wonhu | formal-commanding | Calls on Wonhu to open a path through the surrounding guards. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 667
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 667
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled for noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 667
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 665
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate, a member of the Fire Dragon Pavilion, and a prisoner in the cell above Jin Taekyung after breaking both wrists of a Nanman attendant who underfed him.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Wonhu.md

# Wonhu (원후)

- **Safe through:** Chapter 667
- **Aliases:** None
- **Role:** Wonhu is the eldest member of the Seven Miao Tigers, the Beast Miao King's personal guard.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Wonhu serves Yayul Cheok as a personal guard.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 667
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and he is risking his position and life alongside his father to rescue Jin Taekyung.

## Korean source

```text
＃668화



인생을 살다 보면, 종종 이해할 수 없는 일이 벌어지고는 한다.

바로 지금처럼.

“어디 가냐. 바쁜 일 있어?”

“……!”

아주 잠깐.

가파르게 흘러가던 시간이 멈춘 듯했다.

전신에 크고 작은 상처를 입은 채 맹수처럼 날뛰던 칠묘호도, 어느덧 뇌옥 복도를 가득 메운 백족 전사들도.

그리고 야율목도 석상처럼 굳은 채, 짙은 어둠 너머에서 나타난 한 사람을 멍하니 바라보았다.

‘어떻게?’

그 순간 모두의 뇌리를 가득 채운 의문은 당연했다.

‘그’는 이곳에 나타날 수도 없고, 나타나서도 안 되는 사람이었으니까.

하지만 뇌옥 안의 모두가 귀신이라도 본 것 같은 얼굴을 하고 있을 때.

‘그’의 단단한 손아귀에 어깨를 붙잡힌 야율목만큼은 이 믿을 수 없는 상황이 사실이라는 걸 깨달았다.

동시에 묻지 않을 수 없었다.

“……네가 왜 거기서 나와.”

넋 나간 눈빛과 얼빠진 목소리. 그러나 그런 야율목에게 돌아온 대답은 이루 말할 수 없이 짧고 간결했다.

“그냥 나왔는데.”

“……?”

“나 여기 갇혀 있었잖아. 그러니까 여기서 나온 거지.”

“……!”

아니, 이게 무슨 개소리야.

야율목을 비롯한 모두는 할 말을 잃은 채 생각했다.

‘그러니까 시발. 뇌옥에 갇혀 있어야 할 새끼가 어떻게 기어 나왔냐고.’

심지어 그냥 얌전히 갇혀 있던 것도 아니다. 만근이 넘는 철구를 장신구처럼 주렁주렁 매달고, 공력까지 금제(禁制)당했다고 했다.

그뿐인가. 사방을 가로막은 쇠창살은 운철(隕鐵)을 섞어 만들기까지 했다. 그야말로 단 한 명의 괴물을 위해 만들어진 감옥이었던 셈이다.

‘그런데 어떻게?’

도무지 이해할 수 없는 불가해(不可解)의 영역.

이 믿을 수 없는 광경에 백족 전사들은 본능적으로 내부자의 배신을 떠올렸고, 야율목과 칠묘호는 자신들이 입수한 정보가 잘못된 건 아닌지 생각했으며, ‘그’는 아무렇지 않게 걸음을 내디뎠다.

저벅.

적막을 깨트리는 발걸음 소리.

마침내 어둠에 잠겨 있던 복도에서 작게 흔들리는 횃불 아래로 걸어 나온 그, 아니 진태경이 눈살을 찌푸렸다.

“어우, 눈부셔. 야, 거기 너.”

진태경의 지목에, 횃불을 번쩍 치켜 들고 있던 백족 전사가 멍청한 표정으로 되물었다.

“저요?”

“어, 그래. 너.”

“왜, 왜요?”

“왜긴, 이 눈치 없는 새끼야. 눈 아프니까 팔 좀 내려. 무슨 발표 하냐? 부모님 없이 횡단보도 건너?”

“아뇨.”

이해할 수 없는 말이었지만 백족 전사는 멍한 얼굴로 대답했다.

왠지 그래야 할 것 같았고, 존댓말을 쓰는 것도 당연하게 느껴졌다.

“이 새끼 아직도 파란불 건너고 있네. 팔 내리기까지 삼 초 준다. 삼 초 뒤에 빨간불 되면 너 뒤지는 거야. 삼.”

“아, 죄송합니다.”

“죄송이고 나발이고 빨리 팔이나 내려. 이.”

“옙.”

화륵.

백족 전사가 잽싸게 팔을 내리자 안 그래도 희미하던 불빛이 더욱 약해졌고, 진태경은 그제야 만족스러운 얼굴로 고개를 끄덕였다.

“흠, 훨씬 낫네. 잘했어.”

“별거 아닙…….”

진태경의 칭찬에 왠지 모를 뿌듯함을 느끼던 백족 전사가 멈칫했다.

‘어?’

뭐지. 이게 아닌데.

그리고 찰나의 순간 찾아온 깨달음과 함께 정체 모를 파공성이 그의 귓가를 파고 들었다.

퍽! 털썩.

치이이익.

힘없이 허물어지는 신형과 함께 웅덩이에 잠긴 횃불. 망설임 없이 멍청한 수하의 턱주가리를 갈긴 백족 전사장이 으르렁거렸다.

“이 머저리 같은 놈.”

그 서늘한 목소리에, 물 흐르듯 진행된 눈앞의 광경을 멍하니 지켜보고만 있던 백족 전사들은 정신이 번쩍 들었다.

‘이게 무슨.’

마치 깊은 잠에서 깨어난 듯한 기분. 동시에 그들은 불현듯 깨달았다.

자신들이 직면한 이 상황은 믿을 수 없게도 사실이며, 아직 전투는 끝나지 않았다는 것을.

그리고……

“이제 알아서 불도 꺼 주네. 고맙게.”

무슨 수를 써서라도 속박에서 풀려난 저 괴물을 제압해야 한다는 것을.

순간 뇌리를 스친 깨달음은 벼락처럼 빨랐고, 뒤이어 터져 나온 외침은 천둥과 같았다.

“쳐라!”

웅혼한 공력이 실린 외침이 뇌옥을 뒤흔들었다. 공격을 지시함과 동시에 가장 먼저 뛰쳐나간 백족 전사장이 벽면을 밟으며 쏘아졌다.

타닥, 쐐애애액!

명문 대파의 절정 고수와 비교해도 뒤떨어지지 않는 쾌속한 움직임.

반 박자 늦게 정신을 차린 칠묘호가 그를 막아서려고 했지만, 사방에서 들이닥치는 병장기가 그것을 방해했다.

쉬쉬쉭, 카캉!

짓쳐 든 공격을 막아 낸 칠묘호의 맏이, 원후(猿猴)가 외쳤다.

“어서 그에게 해약(解藥)을……!”

카가각!

미처 끝까지 이어지지 못한 그의 외침. 그리고 황급히 품 안의 뭔가를 꺼내려는 야율목의 모습을 본 전사장은 확신했다.

‘역시, 아직이구나.’

진태경.

중원에서 온 저 젊은 괴물이 어떻게 뇌옥을 빠져나왔는지는 모르겠으나, 놈은 아직 공력의 금제를 풀지 못한 것이 틀림없었다.

그렇다면…….

‘능히 할 수 있다.’

제아무리 초절정 고수라 한들, 공력을 사용할 수 없다면 조금 뛰어난 범부(凡夫)에 불과하다.

물론 놈이 지금껏 익힌 무공과 깨달은 무리(武理)가 한순간에 사라진 것은 아니겠지만, 병장기조차 들지 않은 적수공권으로 이미 오래전 절정의 경지에 오른 자신을 상대하는 것은 불가능에 가깝다.

‘놈은…… 반드시 내 손으로 잡는다.’

누구도 범접할 수 없을 만큼 큰 공을 세울 수 있다는 출세욕과 승리할 수 있다는 자신감은 그 어느 때보다 전사장의 몸과 마음을 가볍게 만들었다.

동시에 그의 손에 들려 있던 한 자루의 검이 휘황한 빛무리를 뿜어냈다.

츠츠츠츠츠!

예리한 검신을 타고 솟구치는 검기(劍氣). 본능적으로 뒤를 돌아본 야율목의 눈동자가 흔들리는 것을 목격한 전사장은 확신했다.

지금의 일격이, 지금까지의 모든 일생을 통틀어 가장 날카롭고 강맹한 한 수가 되리라는 것을.

‘지금!’

쉬이이이잉!

누구도 흠잡을 수 없는 완벽한 흐름. 완벽한 발검(拔劍).

검신으로부터 발출된 검기가 어둠을 가르며 두 사람을 향해 쇄도했고, 전사장은 환희에 찬 외침을 토해 냈다.

“됐……!”

서걱!

적어도 자신의 검기가 허공을 가르기 전까지는.

‘뭐?’

전사장은 이해할 수 없는 광경에 눈을 깜빡였다.

없다. 검기가 훑고 지나간 자리에는 그 무엇도 남아 있지 않았다.

야율목도, 진태경도.

모든 것이 마치 허깨비처럼 사라져 버렸다.

‘어떻게?’

그리고 다음 순간.

전사장의 마음속에서만 울려 퍼진 의문에 대한 대답이 돌아왔다.

“오. 지금 어떻게, 라고 생각했지?”

“……!”

난데없이 등 뒤에서 들려오는 목소리.

전사장은 등골을 타고 올라오는 소름을 느끼며 몸을 회전시켰다. 수많은 수련 끝에 완전히 몸에 익어 버린 검도 함께.

쉬이이익!

하지만 전사장의 검은 다시 한번 바람을 갈랐다. 아니, 바람을 가를 뻔했다는 것이 보다 정확한 표현이었다.

그그그극.

미미하게 흔들리는 검 끝. 전사장의 텅 비어 버린 머릿속에 다시금 의문이 떠올랐다.

‘이게…… 도대체 뭐지?’

그의 의문은 당연했다.

검기를 한껏 머금은 검신이, 아무런 병장기도 들고 있지 않은 맨손바닥에 가로막혀 나아가지 못하고 있었으니까.

‘아니, 심지어 손으로 막은 것도 아니다.’

고작 일 촌(寸)의 간격. 파르르 떨리는 검신과 손바닥 사이의 허공에서, 보이지 않는 힘이 자신의 검을 밀어 내고 있었다.

천천히. 그러나 강하게.

그그그극.

자신의 검만큼이나 세차게 흔들리는 눈빛으로, 전사장이 목소리를 쥐어 짜냈다.

“허, 허공섭물(虛空攝物)?”

공들여 손질한 검신이 어둠 속에서 빛난다. 그 너머에서 누군가의 새하얀 치아가 슬쩍 드러났다.

“허공섭물이라. 뭐, 비슷하지.”

“어, 어떻게. 분명 공력이 금제 되었을…….”

“비슷하지, 같다고는 안 했는데.”

“뭐?”

“이해하려고 하지 마. 이해할 수도 없겠지만.”

진태경의 말은 잔인한 진실이었다.

전사장은 남은 생을 무공에 전념하더라도 중단전(中丹田)의 입구에조차 도달하지 못할 테니까.

“이, 이 무슨……!”

그것은 평생 무공에 전념한 전사장으로서도 이해할 수 없는 영역이었고, 불행히도 진태경은 열등생을 지도하는 과외 선생처럼 친절한 성격이 아니었다.

“꺼져.”

“……!”

전사장의 부릅뜬 눈동자에, 쇠사슬로 칭칭 감겨 있는 주먹이 비친 그 순간.

퍼억!

지금껏 겪어 보지 못한 엄청난 고통이 복부를 타고 그의 전신을 엄습했다.

“커허헉!”

공력을 회복했다고밖에 생각할 수 없는 강력한 일권(一拳).

인간의 한계를 아득히 뛰어넘은 괴물 같은 근력과 속도를 머금은 그 일격을 버티기에는, 전사장은 그저 조금 더 뛰어난 인간에 지나지 않았다.

쐐애애애액!

느껴진다.

날카로운 파공성과 함께 뒤로 쏘아지는 자신의 몸뚱어리가. 그리고 엄청난 고통 속에 흐릿해지는 의식이.

‘이런 미친…… 괴물.’

그것이 마지막이었다.

이미 의식을 잃은 전사장의 몸뚱어리는 분투를 벌이던 칠묘호를 스친 뒤, 마치 포탄처럼 뇌옥 복도를 가득 메운 백족 전사들을 덮쳤다.

쾅! 우두둑!

“크아악!”

“뭐, 뭐냐!”

한순간에 아수라장이 되어 버린 뇌옥. 곧이어 자신들을 덮친 괴물체의 정체를 깨달은 맥족 전사들이 입을 딱 벌렸다.

“전, 전사장님?”

“아니, 어떻게…….”

퍼져 가던 술렁임은 순식간에 가라앉았다.

백족 내에서도 상당히 높은 위치의 절정 고수이자, 이 자리에 모인 이들 중 최고의 실력자인 그를 처치할 사람은 단 한 명밖에 없었으니까.

“진, 진태경.”

누군가의 입술 사이로 흘러나온 중얼거림. 동시에 수많은 시선이 한 방향을 향해 쏘아졌다.

철벅. 절그럭.

구정물이 고여 있는 웅덩이를 밟으며, 양손에는 철구가 끊긴 쇠사슬을 늘어트린 채 걸어오는 한 사람.

“어, 난데. 누가 나 불렀냐.”

어두운 뇌옥의 분위기와는 정반대로, 진태경의 입가에 서린 웃음은 햇살처럼 밝았다.

마치 먹잇감을 발견한 맹수처럼.

아니, 악귀처럼.

“쇠사슬로 존나 처맞고 싶은 새끼, 손?”

“……!”

“……!”

백족 전사들은 전신을 엄습하는 오한을 느끼며 얼어붙었지만, 비단 모두가 그런 것만은 아니었다.

“놈을 쳐라!”

“숫자는 우리가 훨씬 많다! 놈들을 밀어붙여!”

쉬쉬쉬쉭!

외침과 함께 벽면을 밟으며 쇄도하는 십여 개의 신형.

비록 전사장만큼은 아니지만 한 사람, 한 사람이 절정 고수들로 이루어진 조장들이 나서자, 백족 전사들은 잠시 잃었던 용기를 되찾았다.

아니, 되찾을 뻔했다.

후우우웅!

육중한 파공성을 일으키며 날아든 쇠사슬이.

퍼버버버버벅!

쇄도하던 십여 명의 조장들을 단숨에 후려치기 전까지는.

쾅! 콰과광!

굉음과 함께 뇌옥이 흔들렸다.

침을 꿀꺽 삼키며 자욱하게 솟구친 먼지구름을 바라보던 모두의 귓가에, 나직한 목소리가 파고들었다.

“벌써 여름인가. 웬 파리 새끼들이…….”

“……!”

“……!”

“어쨌든. 다음, 손?”

이번에는 누구도 나서지 않았다.

사신(死神)처럼 우뚝 선 그를 멍하니 바라보던 백족 전사들은 약속이라도 한 것처럼 뒷걸음질 쳤다.

하지만…….

쿵, 쿵.

그들의 등 뒤에 놓인 계단에서 들려오는 어떤 불길한 소리는, 일말의 가능성조차 없애 버렸다.

“아, 맞다. 깜빡하고 말 안 했네.”

씩 웃은 진태경이 계단을 가리켰다.

“큰 거 온다.”

다음 순간.

백족 전사들은 소름 끼치는 포효를 들었다.

“태산이. 배고파아아아아!”

굶주린 맹수. 아니, 태산의 포효였다.
```

## Final English reading copy

```markdown
# Chapter 668

Sometimes, inexplicable things happen in life.

Just like now.

“Where are you going? Got somewhere to be?”

“……!”

For the briefest moment, time seemed to stop in the middle of its steep descent.

The Seven Miao Tigers, who had been rampaging like beasts despite wounds all over their bodies; the Bai warriors, who now filled the underground prison’s corridors; and Yayul Mok—all stood frozen like statues, staring blankly at the person who had emerged from beyond the thick darkness.

*How?*

The question that filled everyone’s mind at that moment was only natural.

Because *he* was someone who could not—and should not—have appeared here.

But while everyone inside the underground prison wore the expression of someone who had seen a ghost, only Yayul Mok, whose shoulder was caught in *his* powerful grip, realized that this unbelievable situation was real.

At the same time, he could not help asking.

“…Why are you coming out of there?”

Yayul Mok’s eyes were vacant, and his voice was dazed. But the answer he received was unbelievably short and simple.

“I just came out.”

“……?”

“I was trapped in here, right? So I came out through here.”

“……!”

*What the fuck is he talking about?*

Yayul Mok and everyone else thought the same thing, left speechless.

*So what the hell? We’re asking how the bastard who was supposed to be locked in the underground prison crawled out.*

He had not merely been sitting quietly in confinement, either. They had said that he had been forced to drag around iron balls weighing more than ten thousand geun like accessories, with his internal energy sealed as well.

And that was not all. The iron bars blocking the prison on every side had even been made with meteorite iron mixed into them.

It was a prison built for one monster alone.

*But how?*

It was a realm of incomprehensibility that no one could possibly understand.

Faced with this unbelievable sight, the Bai warriors instinctively thought of betrayal by an insider. Yayul Mok and the Seven Miao Tigers wondered whether the information they had obtained had been wrong. And *he* casually took a step forward.

Step.

The sound of his footsteps shattered the silence.

At last, the man who had been submerged in darkness—or rather, Jin Taekyung—walked beneath the flickering torchlight and frowned.

“Ugh, that’s bright. Hey, you over there.”

At Jin Taekyung’s pointed finger, the Bai warrior holding his torch high asked with a vacant expression,

“Me?”

“Yeah, you.”

“Wh-why?”

“Why do you think, you clueless bastard? My eyes hurt, so lower your arm. What are you doing, giving a presentation? Crossing a crosswalk without your parents?”

“No, sir.”

The Bai warrior answered with a blank face, even though he could not understand what Jin Taekyung was saying.

Somehow, it felt as though he was supposed to answer that way. Using polite speech also felt perfectly natural.

“This bastard’s still crossing on a green light. I’ll give you three seconds to lower your arm. When it turns red, you’re dead. Three.”

“Ah, I’m sorry.”

“To hell with sorry. Just lower your arm already. Two.”

“Yes, sir.”

Whoosh!

The Bai warrior hurriedly lowered his arm. The already faint torchlight grew even dimmer, and only then did Jin Taekyung nod with a satisfied expression.

“Hmm. Much better. Good job.”

“It was nothing……”

The Bai warrior, who had felt a strange sense of pride at Jin Taekyung’s praise, suddenly froze.

*Huh?*

What? This wasn’t right.

And just as the realization struck him, a mysterious sound of splitting air pierced his ears.

Thwack! Thud.

Sizzle.

The warrior’s body crumpled helplessly, and the torch fell into a puddle.

The captain of the Bai warriors, who had struck his stupid subordinate across the jaw without hesitation, growled.

“You useless fool.”

At that icy voice, the Bai warriors who had merely stood there watching the scene unfold as smoothly as flowing water suddenly came to their senses.

*What is this?*

It felt as though they had awakened from a deep sleep. At the same time, they suddenly realized the truth.

This situation they had found themselves in was unbelievably real.

And the battle was not over yet.

And…

“Now he’s even putting out the fire for us. How considerate.”

They had to subdue that monster who had somehow freed himself from his restraints.

The realization flashed through their minds as quickly as lightning, and the cry that followed was like thunder.

“Attack!”

The shout, filled with powerful internal energy, shook the underground prison.

At the same time as he ordered the attack, the captain of the Bai warriors was the first to leap forward. He kicked off the wall and shot toward Jin Taekyung.

Tap-tap—whoosh!

His movement was so fast that it rivaled a Peak master from one of the major sects.

The Seven Miao Tigers, who had come to their senses half a beat late, tried to block him, but weapons charging in from every direction got in their way.

Swish-swish-swish—clang!

Wonhu, the eldest of the Seven Miao Tigers, blocked the incoming attacks and shouted.

“Quickly, give him the antidote…!”

Clang!

His shout was cut off before he could finish.

Seeing Yayul Mok hurriedly reach inside his robes for something, the captain was certain.

*As I thought. Not yet.*

Jin Taekyung.

He did not know how that young monster from the Central Plains had escaped the underground prison, but there was no doubt that the boy had not yet released the seal on his internal energy.

If so…

*It can be done.*

No matter how powerful a Supreme Peak master was, if he could not use his internal energy, he was nothing more than an exceptionally capable commoner.

Of course, the martial arts he had learned and the martial principles he had realized had not vanished in an instant. But with no weapon in hand, facing someone who had reached the Peak realm long ago while fighting bare-handed was nearly impossible.

*I will capture him with my own hands.*

The desire to make a great achievement that no one else could approach, along with his confidence that he could win, made the captain’s body and mind lighter than ever.

At the same time, the sword in his hand began to emit a dazzling halo of light.

Ssssss!

Sword Energy surged along the sharp blade.

The captain instinctively looked back and saw Yayul Mok’s pupils tremble.

He was certain.

This strike would become the sharpest and most powerful move of his entire life.

*Now!*

Ssshhhiiing!

An utterly flawless flow.

A perfect draw.

The Sword Energy released from the blade sliced through the darkness and rushed toward the two men, and the captain let out a cry of joy.

“It’s done—!”

Slice!

At least, that was true until his Sword Energy cut through the air.

*What?*

The captain blinked at the incomprehensible sight.

They were gone.

Nothing remained where his Sword Energy had swept through.

Not Yayul Mok.

Not Jin Taekyung.

Everything had vanished like an illusion.

*How?*

And then, the next moment.

An answer came to the question that had echoed only inside the captain’s heart.

“Oh. You were just wondering how, weren’t you?”

“……!”

A voice came unexpectedly from behind him.

Feeling goose bumps crawl up his spine, the captain spun around. His sword moved with him, completely ingrained in his body after countless hours of training.

Whoosh!

But the captain’s sword once again cut through the air.

No—that was not quite accurate. It had almost cut through the air.

Grgrgrk.

The tip of the sword trembled ever so slightly. Another question rose in the captain’s emptied mind.

*What… is this?*

His confusion was only natural.

The blade, packed with Sword Energy, had been stopped by a bare palm that held no weapon at all.

*No. He didn’t even stop it with his hand.*

There was barely one inch of space between the trembling blade and the palm.

In that empty air, an invisible force was pushing his sword away.

Slowly.

But powerfully.

With eyes trembling as fiercely as his sword, the captain squeezed out his voice.

“S-Seizing an Object Through Empty Space?”

The carefully polished blade glinted in the darkness.

Beyond it, someone’s white teeth appeared in a faint grin.

“Seizing an Object Through Empty Space? Well, something like that.”

“H-how? Your internal energy was clearly sealed—”

“Something like it. I never said it was the same.”

“What?”

“Don’t try to understand it. You couldn’t even if you tried.”

Jin Taekyung’s words were a cruel truth.

Even if the captain devoted the rest of his life to martial arts, he would never reach the entrance to the Middle Dantian.

That was a realm the captain, who had devoted his entire life to martial arts, could not understand. Unfortunately, Jin Taekyung was not the sort of kind person who would patiently tutor a dunce.

“Get lost.”

“……!”

At the moment the captain’s wide eyes reflected Jin Taekyung’s fist, wrapped tightly in chains—

Bam!

An immense pain he had never experienced before surged through his abdomen and spread across his entire body.

“Guh-heok!”

It was a powerful punch that could only mean Jin Taekyung had recovered his internal energy.

The blow contained monstrous strength and speed that far surpassed human limits. The captain was nothing more than a slightly superior human. He had no chance of enduring it.

Whoosh!

He could feel it.

His body shooting backward with a sharp sound of splitting air.

His consciousness fading amid the overwhelming pain.

*This insane… monster.*

That was his final thought.

The captain’s already unconscious body grazed past the Seven Miao Tigers, who were still fighting desperately, then crashed like a cannonball into the Bai warriors filling the underground prison’s corridor.

Boom! Crack!

“Argh!”

“Wh-what the hell?”

The underground prison became a chaotic mess in an instant.

Soon, the warriors of the Maek people realized the identity of the monster that had crashed into them and stared with their mouths hanging open.

“C-Captain?”

“No, how could…”

The spreading commotion quickly died down.

There was only one person who could have defeated him—the Peak master who held a high position even among the Bai people and was the strongest person gathered here.

“J-Jin Taekyung.”

The name slipped from someone’s lips.

At the same time, countless gazes shot toward one direction.

Splash. Clatter.

One man walked through a puddle of filthy water, the chains whose iron balls had broken off dangling from both hands.

“Yeah, that’s me. Did someone call?”

In complete contrast to the dark atmosphere of the underground prison, the smile around Jin Taekyung’s lips was as bright as sunlight.

Like a beast that had found its prey.

No.

Like a fiend.

“Anyone want to get the shit beaten out of them with a chain? Hands?”

“……!”

“……!”

The Bai warriors froze as a chill swept through their bodies.

But not everyone reacted that way.

“Attack him!”

“We have the numbers! Push them back!”

Swish-swish-swish!

At the shouts, a dozen or so figures charged forward, kicking off the walls.

They were not as strong as the captain, but each squad captain was a Peak master. Once they stepped forward, the Bai warriors regained the courage they had briefly lost.

No.

They almost regained it.

Whoooosh!

A chain flew through the air with a heavy sound of splitting wind.

Bam-bam-bam-bam-bam!

The chain swept through the dozen or so squad captains charging forward, knocking them away all at once.

Boom! Crash-crash-crash!

The underground prison shook with the thunderous impact.

Everyone swallowed hard as they stared at the thick cloud of dust rising into the air.

Then a low voice reached their ears.

“Is it summer already? Why are there so many damn flies…”

“……!”

“……!”

“Anyway. Who’s next? Hands?”

This time, no one stepped forward.

The Bai warriors stared blankly at the man standing tall like the Grim Reaper, then took a step backward as though they had all agreed to do so.

But then…

Boom.

Boom.

An ominous sound came from the stairs behind them, erasing even the slightest possibility of escape.

“Oh, right. I forgot to mention something.”

Jin Taekyung grinned and pointed toward the stairs.

“Something big is coming.”

The next moment—

The Bai warriors heard a chilling roar.

“Taishan. Hungryyyyyyyyy!”

A starving beast.

No—Taishan’s roar.
```
