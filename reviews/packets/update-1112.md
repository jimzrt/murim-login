<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1112.txt",
      "sha256": "218a374928b89164e26b448eff89236818336b08ae2194c0aad2643992fe493a",
      "bytes": 19840
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "503980ff058c2d3cc3162612706701382cb33aa02ca8627f76e37f57416efbeb",
      "bytes": 1294
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf6c4f7b66402118726cc38b45f04e6573af5660df71d2d9f176747ba040720c",
      "bytes": 244327
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "3454379844da72dc1712e8b3b1a36a735096836dbff94b44dbe0d12a9afe9bee",
      "bytes": 748
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7ba6ac8ddb6190ffa6d1aa2ea19a57bd46ce95961fe682b3cb1b64213e5708b1",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "f7f5fb2b985928ed1a6be69e4c5f7087e351d95270b7aece7a63ee64784f66f5",
      "bytes": 554
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "cd8f0b05bea18b4a13eda14c28bae26cba73aabba1c990ec70549aa4a974fc79",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3ba236e304e2ba14469922fd00dd9178922a6b3b986cd2e8dc9146fe93018826",
      "bytes": 1513
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a1660866525396581b2d551a68356acb0b2fbaffb68b3d1c5b9ab9db51a05bcd",
      "bytes": 288524
    }
  ],
  "estimated_tokens": 13456
}
-->

# Durable State Update — Chapter 1112

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
1 and safe_through 1112. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1112. Profile updates may replace only one
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
  "chapter": 1112,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1112,
    "continuity_sources": [1112],
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
    "The West Gate has fallen; more than half its garrison are casualties, and some survivors retreated to the Inner City.",
    "Jin Taekyung and Cheongpung are badly injured in the Inner City; Taekyung may not survive.",
    "The Slaughter Saint stays at the South Gate to support its defense; the Bow Saint’s motives are unclear.",
    "Jeok Cheongang is confronting the Dalai Lama at the North Gate after killing all but the last of the Twelve Secret Monks.",
    "The Blood Lord is heading to the Inner City to kill Taekyung."
  ],
  "continuity_sources": [
    1110,
    1111
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries, and can he receive treatment from the Divine Physician?",
    "What is the Bow Saint hiding, and why did she accept the possibility of Taekyung’s death?",
    "What will happen in the confrontation between Jeok Cheongang and the Dalai Lama?",
    "Can the South Gate hold against the Grand Mage and the four Black Ghosts?",
    "Will the Blood Lord reach Taekyung before he can be treated?"
  ],
  "safe_through": 1111,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 상태               | **Status**                     |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본좌      | **I / this lord** only when deliberately grandiose              |
| 노부      | **this old man / I**                                            |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 오성 | **Oseong** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 새외무림 | **Outer Murim** | Murim beyond the Central Plains. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 광풍사 | **Mad Wind Society** | Faction in the great desert. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 대막 | **great desert** | Desert beyond the scorching sands. |
| 송학 | **Songhak** | Fifth Sect Leader of the Fire Gate Clan. |
| 귀염권 | **Ghost Flame Fist** | Sobriquet of Songhak. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 십이밀승 | **Twelve Secret Monks** | The Potala Palace’s twelve top fighters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 달뢰라마 | 적천강 | hostile leader confronting a rival martial master | donor | formal and controlled | Addresses Jeok as 시주 while blocking his departure for the West Gate. |

## Listed compact profiles

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1111
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace in an unequal alliance with Dark Heaven and commits its forces to ending the Fire Gate Clan, pursuing the Palace’s longstanding grievance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1111
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1090
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1105
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1111
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

## Korean source

```text
＃1112화



‘이건, 꿈인가.’

달뢰라마는 문득 생각했다.

또한 동시에, 그 어느 때보다 간절하게 소원했다.

정말 이 모든 것이 꿈이라면, 끔찍한 악몽이라면 한시라도 빨리 잠에서 깨어나기를.

그리고 두 번 다시 이와 같은 악몽이 찾아오지 않기를.

하지만.

으득.

자신도 모르게 깨문 입술에서 전해지는 통증은, 콧속을 파고드는 피비린내와 사방을 둘러싼 매캐한 연기는 단 하나의 진실만을 속삭이고 있었다.

더없이 참혹하고도, 믿을 수 없는 이 모든 광경이 현실임을.

“실로…… 마구니(魔仇尼)가 따로 없구나.”

달뢰라마는 신음처럼 뇌까렸다.

지금 이 순간, 늙은 중의 눈동자에 비치고 있는 한 사람의 모습은 마치 낡은 경전(經典)에서 튀어나온 악귀의 그것과 다르지 않았다.

제자이자 사형제들로 이루어진 십이밀승은 물론, 든든한 지원군이었던 두 마리의 흑귀마저 불살라 버린 악귀.

“화왕(火王) 적천강.”

분노와 두려움이 뒤섞여 떨리는 음성.

그러나 그에 반해, 노승을 향해 나아가는 악귀의 발걸음에는 한 치의 망설임조차 깃들어 있지 않았다.

화악.

불씨가 흩날리고, 공기가 달아오른다.

일순간 부릅떠진 달뢰라마의 두 눈에, 단숨에 십여 장의 거리를 지우며 쇄도한 적천강의 모습이 가득 담겼다.

그의 손끝을 타고 일렁이는, 새하얀 불길도 함께.

퍼엉!

압축된 공기가 폭발하고, 화염이 바람과 빗물을 집어삼킨다.

콰아아아아!

불의 파도가 휘몰아친다면 이러할까.

끔찍하리만치 강한 열기가 조금 전 자신이 서 있던 공간을 휩쓰는 광경을 보며, 달뢰라마는 서늘해지는 등골을 느꼈다.

“화염신장(火焰神掌)……!”

모를 수가 없었다.

그건 선조들이 남긴 첫 기록으로부터 장장 이백여 년을 이어져 내려온 악귀의 무공이자, 무려 두 명의 초절정 고수가 포함된 십이밀승 전원을 죽음으로 몰고 간 원흉이었으니.

“용케 알아보는군. 노부에 관한 소문이 그 촌구석까지 퍼졌더냐?”

후웅!

머리 위, 나직한 음성과 동시에 울려 퍼지는 파공성.

어느덧 매캐한 연기 사이로 다가온 적천강이 굳게 말아쥔 주먹을 달뢰라마의 정수리를 향해 내리꽂았다.

십이밀승보다 앞서 최후를 맞이한, 두 마리의 흑귀를 잿가루로 만들어 버린 멸염신권(滅炎神拳)을.

콰아아앙!

지면이 뒤흔들린다. 불의 기둥이 솟구치고 넘실거리는 열기는 스친 것만으로도 살갗을 태웠다.

치이익.

인두로 지지는 듯한 통증.

그럼에도 또다시 간발의 차로 공격을 피해 낸 달뢰라마는 온 힘을 다해 쌍장(雙掌)을 뻗었다.

콰드득!

손과 손이, 그 안에 담긴 거대한 기운이 쉼 없이 뒤얽히고 부딪힌다.

그러나 조금 전과 달리, 적천강과 정면으로 격돌한 달뢰라마의 눈빛에는 두려움이 차츰 사라지고 있었다.

‘분명 강하지만, 그뿐이다.’

맞잡은 두 손을 통해 선명하게 전해지고 있었다.

불과 촌각 전까지만 하더라도 믿을 수 없는 신위(神威)를 선보였던 적천강의 기운이, 급격하게 흔들리고 있다는 것이.

그리고 그건 찰나의 두려움에 가려졌던 진실이자, 적천강이 숨기고 싶었던 사실이기도 했다.

희생 없는 대가는 없다.

이미 적천강을 도와 북문을 지키던 공동파의 현천진인은 무려 다섯이나 되는 초절정 고수들의 격전 속에서 극심한 내상을 입고 쓰러진 상태.

설령 적천강이라 한들 그 육신이 멀쩡할 리 없었고, 마침내 이와 같은 사실을 깨달은 달뢰라마는 스산한 눈빛으로 눈앞의 원수를 응시했다.

잠시 두려움에 밀려났던, 분노를 실어.

“대단한 착각을 하고 있군.”

“뭐라?”

“화왕 적천강, 네놈으로 인해 알려진 것이 아니다. 이미 오래전 팔열지옥(八熱地獄)에 떨어졌을 네놈의 선대로부터 알게 된 것이다.”

달뢰라마는 한 음절, 한 음절 씹어뱉듯이 말을 이었다.

“우리 포달랍궁은 단 한시도 잊지 않았느니라. 아니, 영영 잊지 못하게 되었지.”

모든 것은 지금으로부터 이백여 년 전, 핏빛 누더기를 걸친 산발의 괴인이 서장에 발을 디딘 그 날로부터 시작되었다.

포달랍궁에 있어 가장 깊고 치명적인 상처이자, 결코 씻을 수 없는 오욕(汚辱)의 역사로.



‘창도(昌都)의 객잔에 머물고 있다는 그 수상한 이방인을 지금 즉시 데려오라. 도대체 어디에서 온 누구이며, 이곳에 온 목적이 무엇인지 빈승이 친히 심문할 테니.’



이와 같은 명령을 내린 당대의 달뢰라마는 짐작조차 하지 못했다.

제아무리 멋모르는 이방인이라고는 하나, 적어도 서장에서 만큼은 마교(魔敎)와 견줄 만큼의 영향력을 지녔다 자부하는 자신들에게 맞설 간 큰 이가 있으리라고는.

그리고 생포를 위해 객잔으로 파견된 이십여 명의 무승을 모조리 반병신으로 만들어 버린 이방인이, 눈깔을 허옇게 뒤집어 깐 채 역으로 쳐들어오리라는 것도.



‘누구냐. 감히 이 몸 어르신께서 사흘 만에 마주한 밥상을 때려 부수라고 명령한 빡빡이 새끼가.’



어쩌면 그때가 마지막 기회였을지 모른다.

우선 다소 거친 방법으로 이방인과 접촉을 시도한 무승들의 행동에 유감을 표하고.

실로 감격스러운 사흘만의 식사를 방해받은 그를 위해 상다리가 휘어질 만큼의 술과 고기를 준비한 다음.

땔감을 잔뜩 쑤셔 넣은 아궁이처럼 따뜻해진 분위기 속에서 대화를 이어 갔다면.

그러기만 했다면.

하지만 기록된 역사가 증명하듯, 안타깝게도 그런 몽글몽글한 전개는 이어지지 못했다.

이미 밥상을 엎고 무력을 사용하려 한 대가로 스무 명이나 되는 무승들이 반병신이 되어 버린 데다가, 불살(不殺)과 금욕(禁慾)의 원칙을 철두철미하게 지키는 포달랍궁으로서는 당장 이방인을 진정시킬 술과 고기도 없었으니까.

다만 그날 분노에 사로잡힌 이방인이 다짜고짜 쳐들어온 포달랍궁의 본궁(本宮)에는, 상다리가 휘어질 만큼의 술과 고기 대신 누군가의 팔다리를 맨손으로도 부러트릴 수 있는 무승(武僧) 이백 명이 있었다.

자타가 공인하는 서장 제일의 고수였던 당대의 달뢰라마와 그를 가까이에서 보좌하는 십이밀승 중 네 사람도.



‘보아하니 중원에서 제법 이름 높은 무림인 같은데…… 지금이라도 순순히 투항한다면 이십 년 정도의 면벽(面壁)으로 마무리 짓도록 하지. 시주의 생각은 어떤가?’



하지만 이와 같은 달뢰라마의 제안에, 이방인은 단호하게 대답했다.



‘수지가 더럽게 안 맞는군. 거절한다.’

‘허어. 상황을 어렵게 만드는군.’

‘상황을 이 지경으로 만든 건 너희 땡중들이지, 이 몸 어르신께서는 그 어떤 잘못도 저지르지 않았다. 적어도 아직까지는.’

‘……아직까지는?’

‘크흠. 여하튼 잠시 휴식을 취한 뒤 조용히 돌아갈 생각이었다. 적어도 이번만큼은.’

‘……이번만큼은?’

‘어디서 굴러먹다 왔는지 모를 땡중들이 다짜고짜 들이닥친 것부터 마음에 들지 않았지만, 적어도 식사를 마칠 때까지 얌전히 구석에 처박혀 기다렸다면 이 어르신 역시 잠자코 응했을 것이다. 아니, 최소한 억지로 제압하려 하지만 않았어도 지금과 같은 일은 벌어지지 않았겠지.’

‘빈승이 생각하기에도 아주 틀린 말은 아닐세. 허나, 제자들이 범한 약간의 무례를 감안하더라도 시주의 손속은 너무 과했어.’

‘귀중한 밥상을 엎은 것으로도 모자라 무기까지 사용하려 했는데, 그게 약간의 무례다?’



정곡을 찌르는 반문에 달뢰라마는 인정 대신 침묵을 택했고, 이미 승려보다는 무림인에 가까운 그의 모습을 말없이 지켜보던 이방인은 한숨을 푹 내쉬었다.



‘그 말을 듣고 보니 가슴 깊이 후회되는군.’

‘음. 정말인가?’

‘물론. 천지신명께 맹세코.’



그리고 다음 순간 이어진 이방인의 대답이, 그날 모두의 운명을 결정지었다.



‘반병신이 아니라, 아예 죄다 병신을 만들어 버렸어야 했는데.’

‘……시주는 뼛속까지 마구니로군. 어쩌겠나. 이렇게 되어 버린 것을. 부디 우리를 원망 말고 내세에서는 평안하시게.’



그렇게 살계(殺戒)가 열렸다.

양측 모두에서가 아닌, 오직 한쪽에서만 몰아치는 피바람.

그로부터 이백여 년이 넘게 흐른 지금까지도, 아니 포달랍궁이 존속하는 한 천년 후에도 기억될 무시무시한 피바람이.

“그날, 그 자리에서만 일백이 죽고 일백이 불구가 되었다.”

사문의 치욕을 다시금 떠올린 달뢰라마가 쇳소리가 섞인 음성으로 말을 이었다.

적천강을 응시하는 그의 눈빛은 더없이 차가웠고, 흔들리지 않는 음성에는 두려움을 집어삼킨 분노만이 들끓고 있었다.

“선대 달뢰라마께서도 그때 돌아가셨지.”

함께 있던 십이밀승의 네 사람은 간신히 목숨을 건졌지만, 그들 역시 살아남은 무승들처럼 두 번 다시 무공을 쓸 수 없는 몸이 되었다.

“그건 있어서도, 있을 수도 없는 끔찍한 치욕이었다.”

이 모든 것은 불과 반나절 만에 벌어진 참사였고, 서장 곳곳에 흩어져 질서를 유지하던 포달랍궁의 모든 무승은 온 힘을 다해 본궁으로 향했다.

그리하여 마침내 볼 수 있었다.

위풍당당했던 모습을 찾아볼 수 없을 만큼 처참하게 무너진 본궁과 새카맣게 그을린 채 뽑혀 나온 기둥에 휘갈겨 쓴 하나의 글귀를.

[옥황상제 가로되, 밥 먹을 때는 개도 안 건드린다.]

그리고 도무지 그 출처가 의심스러운 글귀 아래에는, 그 내용만큼이나 길고 거창하게 공들여 쓴 작성자의 신분이 적혀 있었다.

“대 열화문 오대 문주. 귀염권(鬼炎拳) 송학.”

지금까지도 길이길이 전해지는 그 저주받을 이름을, 달뢰라마는 잘근잘근 씹어 내뱉었다.

“차라리 그때 놈을 붙잡았다면, 오늘과 같은 일도 없었을 것이다.”

하지만 귀염권 송학이 무승들의 손에 사로잡혀 염라대왕과 안면을 트게 되는 일은 없었다.

포달랍궁에 씻을 수 없는 치욕을 새긴 그는 서장 무림이 펼친 천라지망을 말 그대로 녹여 버린 뒤, 곧장 중원으로 향했다.

열화문의 역대 문주 중 그 누구보다 식사를 중요시했던 그가 사흘이나 끼니를 거르게 할 만큼, 서장에 발을 디딘 결정적 이유를 제공한 대막의 광풍사(狂風社)의 추격을 피했던 것처럼.

그리고 흐뭇한 마음으로, 사문의 본거지인 구화산으로 돌아와 자신의 흥미진진한 발자취를 짧게 기록했다.



본좌는 사조(四祖)이신 삼대 문주를 마음 깊이 존경해 온 바, 그분의 행적을 좇아 천하와 새외무림을 탐방했느니라.

한데 어쩌다 보니 뜨거운 사막 너머에 존재하는 대막의 광풍사와 일전을 겨루고, 포달랍궁의 기둥뿌리를 뽑았느니라.

그러자 서장의 모든 인마가 분노하여 본좌를 쫓았느니라.

허나 본좌가 누구인가.

나 대 열화문 오대 문주 귀염권 송학. 털끝 하나 상하지 않고 놈들을…… 피하여 무사히 중원으로 돌아왔느니라.



물론 귀염권 송학은 몰랐다.

그로부터 이백여 년 뒤, 까마득한 후예가 자신이 남긴 자랑스러운 기록을 발견하고 미친놈이라며 중얼거릴 것이라고는.

그와 더불어 포달랍궁이 이 원한을 그토록 오랫동안 간직하리라고는.

사실, 신경도 쓰지 않았다는 것이 옳은 표현이었다.

“후에 알았다. 놈이 그보다 앞서 사막에서 광풍사의 마적들을 오백 명도 넘게 도륙한 뒤였다는 사실을.”

송학의 말을 빼앗으려다 수뇌부 대다수의 목숨을 빼앗긴 광풍사는 그때의 피해를 감당하지 못해 결국 역사의 뒤안길로 사라졌지만, 포달랍궁은 아니었다.

서장 무림에 한해서만큼은 어떤 적수도 없었던 그들은 조용히 복수를 다짐했다.

용서와 인정을 통해 더 큰 살생을 피하자고 주장했던 학승(學僧)들도 있었으나, 승려보다는 무림인에 가까운 무승들의 분노를 막기에는 턱없이 부족했다.

그렇게 포달랍궁은 차츰 변모했다.

경전보다 무공서를 가까이하기 시작했고, 오성이 뛰어난 아이들만을 받아들여 무승의 숫자를 전폭적으로 늘렸다.

“우리는 맹세했다. 설령 그날의 복수를 이루기도 전에 귀염권이 죽어 흙이 되더라도, 이 손으로 직접 그 마구니들의 명맥을 끊어 놓겠노라고.”

하여 강산이 열 번 가까이 바뀌었을 정도의 시간이 흘렀을 때.

포달랍궁은 과거를 아득히 뛰어넘는 강대한 무력 집단으로 거듭났다.

그들 스스로조차 복수의 때가 왔다고 생각할 만큼.

하지만 지금으로부터 약 일백여 년 전, 포달랍궁의 전통을 따라 어린 나이에 새로운 달뢰라마로 선택받은 그는 그것으로 만족하지 않았다.

“우리는 분명 강해졌으나, 그럼에도 아직 턱없이 부족했다. 사실상 직접 복수를 이루기 위해서는 중원 그 전체를 상대해야 했으니까.”

이방인이었던 송학이 서장에 발을 디딘 그 순간부터 배척받았듯, 포달랍궁 역시 중원에서는 한낱 이방인에 지나지 않았다.

거기에 더해 자칫하면 혈풍(血風)을 불러일으킬 수도 있을 만큼 강력한 무력 집단.

비록 온갖 평지풍파를 일으키며 착실하게 은원(恩怨)을 쌓아온 열화문이라 할지라도, 중원의 무림인들이 서쪽의 위험한 이방인들의 복수를 위해 그들을 찾아 바칠 가능성은 전무했다.

“결국 우리에게 필요한 것은 더욱 강한 힘뿐이었다. 혹은…… 힘을 합쳐 중원과 맞설 동맹이거나.”

콰드드득.

일순간 강해진 힘이, 뒤얽힌 적천강의 손을 조금씩 밀어 내기 시작했다.

팽팽하던 힘의 균형이 마침내 허물어지기 시작한 것이다.

“마교 놈들은 실로 어리석기 그지없었다. 광오한 천마(天魔)는 우리를 나약하다며 비웃었고, 그것이 가장 큰 패착이었지.”

“정마대전…… 허, 그저 낡고 명분 없는 복수심에 사로잡힌 땡중인 줄 알았더니, 이제는 중이라고 부를 수도 없겠군.”

울컥 솟구치는 핏물을 애써 삼키며, 적천강은 조소 어린 눈빛으로 달뢰라마를 응시했다.

“참으로 우습군. 그렇지 않느냐?”

“뭐?”

“지금의 네 모습을 보아라, 이제는 마교보다도 더한 악귀들과 손을 잡은 네놈이 감히 누구를 마구니라 부를 수 있단 말이냐!”

“……!”

일순간, 달뢰라마의 신형이 흠칫 굳었다.

불현듯 일갈을 터트린 적천강에게서 흘러나오는 무시무시한 기세를, 화염이 쏟아지는 그 두 눈동자에 비친 자신의 진정한 모습을 비로소 발견했기 때문이었다.

붉다. 붉었다.

어느덧 달뢰라마의 안광(眼光)은, 그의 발치에 고인 피 웅덩이와 같은 색으로 물 들어가고 있었다.

서서히, 그러나 계속해서.

“하다 하다, 결국 그 같잖은 힘을 위해 금기(禁忌)마저 범했더냐.”

“아, 아니다. 나는……!”

파르르 떨리는 눈동자와 음성.

하지만 그 어떤 말로도 과거의 진실을 부정할 수는 없었다.

단지 강해져야 했다. 어떻게든 더, 더 강한 힘이 필요했다.

암천이 제공하는 수많은 영단과 무공이 그것을 가능케 했다.

아니, 정확히는 마(魔)가 깃든 그 새로운 힘이.

그리고 그 자신조차 잊고 있던, 아니 애써 외면해왔던 오랜 모순을 들켜버린 달뢰라마를 향해, 적천강은 피식 실소를 흘렸다.

“할 말 없으면 주둥이 다물어라. 마두(魔頭)의 혀끝에서 흘러나오는 역겨운 변명은 비위 좋은 노부로서도 참기 힘드니까.”

“놈! 입 닥치지 못할까-!”

화아악!

사방으로 뻗어 나가는 거대한 기파.

극렬한 분노를 장작 삼아, 마침내 몸속 깊은 곳에 잠들어 있던 모든 잠재력과 힘을 쥐어 짜낸 달뢰라마는 전력을 다해 눈앞의 원수를 밀어붙였다.

우드득!

어느덧 확연히 기울어 버린 힘의 저울추.

뼈가 어긋나는 소리와 함께 적천강의 양손에 맺혀있던 불길이 흐릿해진 그때였다.

쌓일 대로 쌓인 부상과 피로를 증명하듯, 핏물이 흘러나오던 그의 입술 사이로 외마디 창룡후(蒼龍吼)가 터져 나온 것은.

“현천(賢天), 지금이다!”

그 순간.

스아아아아.

느려진 세상 속, 온 힘을 다해 적천강의 손을 뿌리친 달뢰라마는 전신의 솜털이 곤두서는 듯한 감각을 느끼며 신형을 돌려세웠다.

그와 동시에 떠올렸다.

잠시 뇌리에서 잊혀져 있던 한 사람의 존재를. 

이미 전투 불능 상태에 빠졌다고 생각했던 공동파 장문인의 모습을.

그리고 저 멀리, 커다란 코끼리의 사체에 기댄 채 가느다란 숨만을 내뱉고 있는 현천진인을 발견하고 얼어붙었다.

아니.

퍼걱!

바로 그 순간 몸속 깊숙이 파고든 끔찍한 열기는, 그 찰나의 시간조차도 허락하지 않았다.

“……!”

벼락에 관통당한 것처럼 잘게 떨리는 육신.

그러나 그 끝에는 한 줌의 핏물도, 외마디 비명도 없었다. 

응당 터져 나왔어야 할 핏물을 증발시킨 화염이, 소리 내어 울부짖는 것조차 잊어버릴 만큼의 아득한 고통을 선사했으니까.

하지만 어쩌면 달뢰라마에게 있어 그 무엇보다 가장 큰 고통은, 지금 이 순간 귓가를 파고드는 원수의 나지막한 음성일지도 몰랐다.

“화왕 적천강 가로되, 반드시 지켜야 할 것이 있는 존재는 설령 축생(畜生)이라 할지라도 건드리지 말지어다.”

포달랍궁의 기둥에 자신만의 글귀를 새겨넣은 옛 선조처럼, 적천강은 흐릿하지만 선명한 목소리로 속삭였다.

적의 등줄기를 관통한 것으로도 모자라 가슴을 뚫고 튀어나온 자신의 손을 힘껏 움켜쥐며.

“그 존재가, 열화문에 속해 있다면 더욱더.”

달뢰라마는 대답할 수 없었다.

세상으로 이어진 모든 감각이 끊어지고, 시야가 완전한 어둠에 가로막히는 그 순간까지도.

“먼저 가거라. 서장의 마구니야. 노부는 아직 지켜야 할 것이 남아 있으니.”

툭.

마침내 힘없이 기울어지는 고개.

염라(閻羅)의 그것처럼 울려 퍼지는 원수의 마지막 음성과 함께, 달뢰라마를 둘러싼 모든 세상이 닫혔다.
```

## Final English reading copy

```markdown
# Chapter 1112

*Is this a dream?*

The Dalai Lama wondered.

At the same time, he wished for it more desperately than ever before.

If all of this really was a dream—a terrible nightmare—then he wanted to wake from it as soon as possible.

And he never wanted a nightmare like this to come again.

But—

*Grind.*

The pain from his bitten lip, the stench of blood seeping into his nostrils, and the acrid smoke surrounding him all whispered the same truth.

That this utterly horrific, unbelievable scene was real.

“Truly…… there’s no mistaking it. He’s a fiend.”

The Dalai Lama muttered like a groan.

At that moment, the figure reflected in the old monk’s eyes was no different from a demon torn from an ancient scripture.

A fiend who had burned to death not only the Twelve Secret Monks—his Disciples and fellow martial brothers—but even the two Black Ghosts who had been such dependable reinforcements.

“Fire King Jeok Cheongang.”

His voice trembled, anger and fear mingling in it.

By contrast, the fiend striding toward the old monk showed no hint of hesitation.

*Whoosh.*

Embers scattered. The air grew hot.

The Dalai Lama’s eyes flew wide open. Jeok Cheongang had closed the distance of more than ten jang in an instant and was rushing straight at him.

White flames flickered at Jeok Cheongang’s fingertips.

*BOOM!*

Compressed air exploded, and the flames swallowed wind and rain.

*KABOOOOOM!*

Was this what a wave of fire looked like?

Watching the searing heat sweep through the place where he had stood just moments ago, the Dalai Lama felt a chill run down his spine.

“Flame Divine Palm……!”

There was no way he wouldn’t recognize it.

It was the fiend’s martial art, passed down for two hundred years from the first record left by his ancestors—and the very thing that had driven all the Twelve Secret Monks, including two Supreme Peak masters, to their deaths.

“You know it, at least. Did word of this old man spread all the way to that backwater?”

*Whoosh!*

A low voice rang out above him, followed by the sound of something tearing through the air.

Jeok Cheongang had already emerged through the acrid smoke. His tightly clenched fist came crashing down toward the crown of the Dalai Lama’s head.

The Flame-Extinguishing Divine Fist—the technique that had reduced the two Black Ghosts to ash before the Twelve Secret Monks met their end.

*KABOOM!*

The ground shook. A pillar of fire shot upward, and the rolling heat burned skin at a mere brush.

*Sizzle.*

The pain was like being seared with a branding iron.

Yet the Dalai Lama dodged the attack by a hair once more, then thrust both palms forward with all his strength.

*Crack!*

Their hands met. The immense qi within them tangled and collided without pause.

But unlike a moment ago, the fear was gradually fading from the Dalai Lama’s eyes as he clashed head-on with Jeok Cheongang.

*He’s strong, but that’s all.*

He could feel it clearly through their joined hands.

Jeok Cheongang’s qi—the same man who had displayed such unbelievable power mere moments ago—was wavering sharply.

And that was the truth his fear had briefly obscured. The truth Jeok Cheongang wanted to hide.

Nothing comes without a price.

Perfected Being Hyeoncheon of the Kongtong Sect, who had helped Jeok Cheongang defend the North Gate, was already down with severe internal injuries after fighting amid a clash between no fewer than five Supreme Peak masters.

Even Jeok Cheongang’s body couldn’t have come through that unscathed. At last realizing this, the Dalai Lama stared at the enemy before him with a baleful gaze.

The fear that had briefly driven out his anger was gone. His anger returned in its place.

“You’re gravely mistaken.”

“What?”

“People don’t know of you because of Fire King Jeok Cheongang. They learned of you from your ancestor—the one who should have fallen into the Eight Hot Hells long ago.”

The Dalai Lama spoke, biting off every syllable.

“Our Potala Palace never forgot. No—we came to a point where we could never forget.”

It had all begun more than two hundred years ago, on the day a wild-haired stranger in blood-red rags set foot in Tibet.

For the Potala Palace, it was the deepest, most devastating wound—and a history of humiliation that could never be washed away.

*Bring in that suspicious foreigner staying at an inn in Chamdo immediately. I will personally interrogate him to find out who he is, where he came from, and why he’s here.*

The Dalai Lama of that era, who had issued this order, could never have guessed what would happen.

They had considered themselves powerful enough in Tibet to rival the Demonic Cult, and had never imagined some clueless foreigner would have the nerve to defy them.

Nor could they have imagined that the foreigner, after turning more than twenty martial monks sent to capture him into cripples, would charge into their palace with his eyes rolled back in his head.

*Who are you? Which bald bastard ordered you to smash the meal this old man finally got after three days?*

Perhaps that had been their last chance.

They could have started by apologizing for the martial monks’ rather rough attempt to make contact with the stranger.

Then they could have prepared enough meat and liquor to make the table sag, to make up for interrupting his deeply gratifying first meal in three days.

And, in an atmosphere warmed like a firebox stuffed with kindling, they could have talked.

If only they had done that.

But, as the recorded history proved, no such heartwarming turn of events had followed.

Twenty martial monks had already been crippled for overturning the man’s table and trying to use their weapons. And the Potala Palace, which rigorously upheld the principles of non-killing and abstinence, had neither liquor nor meat on hand to calm the stranger down.

That day, the stranger had charged straight into the Potala Palace’s main sanctuary in a fit of rage. Instead of enough liquor and meat to make a table sag, there were two hundred martial monks who could break a person’s limbs with their bare hands.

Among them were the Dalai Lama of that era, acknowledged by all as Tibet’s greatest master, and four of the Twelve Secret Monks, who served closely at his side.

*You seem like a fairly well-known martial artist from the Central Plains…… If you surrender peacefully now, I’ll settle this with twenty years of wall-gazing meditation. What do you think, donor?*

But the stranger gave the Dalai Lama a firm answer.

*That’s a terrible deal. I refuse.*

*Good grief. You’re making this difficult.*

*You bald monks made this what it is. This old man hasn’t done a damn thing wrong. At least, not yet.*

*……Not yet?*

*Ahem. Anyway, I was planning to rest for a while and then leave quietly. This time, at least.*

*……This time, at least?*

*I didn’t like it when bald monks I’d never seen before came barging in out of nowhere. But if you’d waited quietly in a corner until I finished eating, I would’ve gone along with it. Hell, if you hadn’t tried to force me down, none of this would’ve happened.*

*I can’t say you’re entirely wrong. Still, even allowing for my Disciples’ slight discourtesy, your response was excessive.*

*They overturned my precious meal and even tried to use weapons. And you call that a slight discourtesy?*

Faced with the pointed question, the Dalai Lama chose silence over admitting the truth. The stranger watched the Dalai Lama, who already seemed more like a martial artist than a monk, then let out a long sigh.

*Hearing you say that, I deeply regret it.*

*Oh? Really?*

*Of course. I swear it to Heaven and Earth.*

The stranger’s next words sealed everyone’s fate.

*I should’ve crippled them all completely instead of leaving them half-crippled.*

*……You’re a fiend to the bone. What can be done now? It’s come to this. Please, don’t hold it against us. May you find peace in your next life.*

And so, the killing began.

A storm of blood swept through—not from both sides, but from only one.

A dreadful storm of blood that would be remembered for more than two hundred years, and would still be remembered a thousand years later, as long as the Potala Palace endured.

“One hundred were killed that day, right there. Another hundred were crippled.”

The Dalai Lama, once more recalling the humiliation of his sect, spoke in a voice edged with iron.

His gaze fixed on Jeok Cheongang was colder than ever. The anger simmering in his unwavering voice had swallowed his fear.

“The previous Dalai Lama died then, too.”

The four Twelve Secret Monks who had been there with him barely survived, but like the martial monks who lived through it, they were never able to use martial arts again.

“It was a terrible humiliation. Something that should never have happened—and could never have happened.”

It had all unfolded in barely half a day. Every martial monk of the Potala Palace, scattered throughout Tibet to maintain order, rushed to the main sanctuary with all their might.

And at last, they saw it.

The main sanctuary, so magnificent in its heyday, lay in utter ruin. One of its charred, uprooted pillars bore a line of writing scrawled across it.

> [The Jade Emperor says: Even a dog should be left alone while it eats.]

And beneath those words, whose source was deeply suspect, the writer had carefully inscribed his credentials at equal length and in grandiose style.

“Fifth Sect Leader of the great Fire Gate Clan. Ghost Flame Fist Songhak.”

The Dalai Lama ground out that accursed name, still passed down to this day.

“If we’d captured him then, none of this would be happening today.”

But Ghost Flame Fist Songhak was never captured by the martial monks and sent off to meet Yama.

After etching an indelible humiliation into the Potala Palace, he melted through the net over heaven and earth laid by Tibet’s Murim and headed straight for the Central Plains.

He’d avoided pursuit by the Mad Wind Society of the great desert—the decisive reason he’d set foot in Tibet in the first place—even though they’d kept him from eating for three days. The man had cared about meals more than any other Sect Leader in the Fire Gate Clan’s history.

Then, with a satisfied heart, he returned to Mount Jiuhua, the Fire Gate Clan’s home, and briefly recorded his thrilling exploits.

> I have always held the Fourth Ancestor, the Third Sect Leader, in the deepest respect. In pursuit of his deeds, I explored the world and the Outer Murim.
>
> As it happened, I fought the Mad Wind Society of the great desert beyond the hot sands, and uprooted the Potala Palace’s very pillars.
>
> All the men and horses of Tibet were enraged and pursued me.
>
> But who am I?
>
> I, Ghost Flame Fist Songhak, Fifth Sect Leader of the great Fire Gate Clan. Without so much as a hair harmed, I…… evaded them and returned safely to the Central Plains.

Of course, Ghost Flame Fist Songhak didn’t know that more than two hundred years later, a distant descendant would find his proud record and mutter that he was a madman.

Nor did he know the Potala Palace would hold on to this grudge for so long.

In truth, he hadn’t cared in the slightest.

“I learned later that he’d already slaughtered more than five hundred of the Mad Wind Society’s mounted bandits in the desert.”

The Mad Wind Society had tried to steal Songhak’s horse—and lost most of its leadership instead. Unable to withstand the damage, it eventually disappeared into the pages of history. The Potala Palace, however, had not.

They had no rivals in all of Tibetan Murim, and quietly resolved to take revenge.

Some scholarly monks argued they should forgive and show mercy to avoid causing even more bloodshed, but they were no match for the fury of the martial monks, who were closer to martial artists than to monks.

And so, the Potala Palace gradually changed.

They began to value books on martial arts more than scriptures and dramatically increased the number of martial monks, accepting only gifted children.

“We swore that even if Ghost Flame Fist died and turned to dust before we could avenge that day, we would cut off the line of those fiends with our own hands.”

By the time the rivers and mountains had changed nearly ten times over—

The Potala Palace had become a formidable military force, far surpassing anything it had been in the past.

So powerful that even they believed the time for revenge had come.

But about a hundred years ago, the boy chosen as the new Dalai Lama at a young age, according to Potala Palace tradition, wasn’t satisfied with that.

“We had certainly grown stronger, but it still wasn’t nearly enough. To exact our revenge ourselves, we would have to face the Central Plains in its entirety.”

Just as Songhak had been treated as an outsider when he set foot in Tibet, the Potala Palace was nothing but a group of outsiders in the Central Plains.

And they were a military force powerful enough to bring about a storm of bloodshed if things went wrong.

Even though the Fire Gate Clan had steadily built up gratitude and grudges by stirring up all manner of trouble, there was no chance the martial artists of the Central Plains would hunt them down and hand them over so dangerous outsiders from the west could take revenge.

“In the end, all we needed was greater strength. Or…… an alliance strong enough to stand against the Central Plains.”

*Crack.*

The strength flowing through their tangled hands surged, slowly forcing Jeok Cheongang’s hands back.

The balance of power that had held steady was finally beginning to collapse.

“The Demonic Cult was truly foolish. The arrogant Heavenly Demon mocked us for being weak. That was his greatest mistake.”

“The Great Faction War…… Hah. I thought you were just a bald monk consumed by an old, unjustified grudge. Now I can’t even call you a monk.”

Jeok Cheongang swallowed a mouthful of blood that surged up and stared at the Dalai Lama with a scornful gaze.

“How ridiculous. Don’t you think?”

“What?”

“Look at yourself. You’ve joined hands with fiends worse than the Demonic Cult, and you dare call anyone else a fiend?”

“……!”

The Dalai Lama’s body jolted to a halt.

The terrible aura flowing from Jeok Cheongang, who had suddenly shouted at him, made him see his true reflection in those eyes pouring flames.

Red. They were red.

The Dalai Lama’s eyes had gradually taken on the color of the pool of blood at his feet.

Slowly, but surely.

“After all that, you even broke a taboo for that pathetic strength.”

“N-no. I……!”

His voice and eyes trembled.

But no words could deny the truth of the past.

He had needed to grow stronger. Somehow, he needed more and more power.

The countless pills and martial arts Dark Heaven offered had made that possible.

No—more precisely, that new power, infused with demonic energy, had made it possible.

Jeok Cheongang let out a quiet laugh at the Dalai Lama, who had just been caught in a contradiction he’d forgotten—or desperately tried to ignore.

“If you’ve got nothing to say, shut your mouth. Even this old man, with a strong stomach, can’t take the disgusting excuses spilling from a fiend’s tongue.”

“You bastard! Shut your mouth!”

*Fwoosh!*

A vast aura surged in every direction.

Using his blazing rage as kindling, the Dalai Lama finally wrung every last bit of power and potential from deep within himself and drove his full strength against the enemy before him.

*Crack!*

The balance of power had tipped decisively.

As the sound of bones shifting rang out and the flames gathered around Jeok Cheongang’s hands began to dim, a single azure dragon’s roar burst from between his bloodied lips, bearing witness to his mounting injuries and exhaustion.

“Hyeoncheon! Now!”

At that moment—

*Shhhhh.*

The Dalai Lama, moving through the slowed world, tore his hands free of Jeok Cheongang’s grip with all his strength. He spun around, feeling the hairs all over his body stand on end.

At the same time, he remembered someone whose existence had briefly slipped from his mind.

The Kongtong Sect Leader—the man he had thought already incapacitated.

Far off, he saw Perfected Being Hyeoncheon leaning against the corpse of a huge elephant, breathing faintly. The Dalai Lama froze.

No.

*Crack!*

At that very moment, the terrible heat that drove deep into his body gave him no time even for that instant.

“……!”

His body trembled as if pierced by lightning.

But not a drop of blood, not a single scream, came from him.

The flames had vaporized the blood that should have burst out and inflicted such distant, unbearable pain that he’d even forgotten how to cry out.

But perhaps the greatest pain of all for the Dalai Lama was the low voice of his enemy, now piercing his ears.

“Fire King Jeok Cheongang says: Never harm a being who has something they must protect, even if that being is a beast.”

Like the ancestor who had carved his own words into a Potala Palace pillar, Jeok Cheongang whispered in a faint yet clear voice.

He clenched his hand, which had pierced through his enemy’s back and burst out through his chest.

“Especially if that being belongs to the Fire Gate Clan.”

The Dalai Lama couldn’t answer.

Even as every sense connecting him to the world went dark, even as darkness swallowed his vision completely.

“Go on ahead, fiend of Tibet. This old man still has something to protect.”

*Thud.*

At last, his head slumped limply.

Along with his enemy’s final words, echoing like Yama’s, the world surrounding the Dalai Lama closed in.
```
