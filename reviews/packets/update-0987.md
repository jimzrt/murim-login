<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0987.txt",
      "sha256": "fd613c72d40fd33d578783583c0dd2ce1acd4fa08614dfa9a0a849634526e82a",
      "bytes": 12752
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cf655db4698dd7c9d6dee3394a9eb7d46f571546866d88120e827970049767f9",
      "bytes": 1399
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "83842a142e086e1971747d7033b0bdcd2ca92b8fbda91570b0a0873034340cbb",
      "bytes": 759
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "908c94baec7d7c5c05f604ea78fbb9a3a239f4725f00fd61e8b4a1aa504e64d3",
      "bytes": 1018
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e229cd05e12690b577b1a792692965eb3f1bc4c980f80822f28e94b2912b27b0",
      "bytes": 1291
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "fe2c15cfde36aa702da0763f3b9024b37d1a99fd999ab1c00d19710b50e86d51",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01a31c8e350480d5fc6f56874db538d312ebb17cba112c5bed6f9815f652a372",
      "bytes": 272857
    }
  ],
  "estimated_tokens": 9760
}
-->

# Durable State Update — Chapter 987

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
1 and safe_through 987. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 987. Profile updates may replace only one
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
  "chapter": 987,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 987,
    "continuity_sources": [987],
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
    "The Jin Family of Taiyuan is recognized as one of the Five Great Families; the fallen Murong Family is no longer among them.",
    "The System has granted Jin Taekyung a level-up, 10 bonus stat points, increased Fame, and the status of a feudal lord appointed by the Son of Heaven; Jin Wikyung and Jin Mukyung received undisplayed healing effects and bonus buffs.",
    "The Murong survivors’ innocence and whether they can rebuild as a household remain unresolved.",
    "A Murim Alliance envoy has arrived to deliver a message from the Alliance Leader to Jin Wikyung.",
    "The dying Thunderbolt Saber King is transferring his remaining internal energy to Jin Taekyung through the dangerous technique Transmitting Internal Energy Across the Body."
  ],
  "continuity_sources": [
    985,
    986
  ],
  "open_questions": [
    "What is the Alliance Leader’s message to Jin Wikyung?",
    "Will Jin Taekyung survive the dangerous transfer of the Thunderbolt Saber King’s internal energy?",
    "Why did Murong Baek suggest that the Western, Southern, and Eastern Heaven Demon Lords’ plans failed, and what did he mean by implying the situation may have been predetermined or that he was used?",
    "Why has Dark Heaven continued costly schemes without revealing its full strength?"
  ],
  "safe_through": 986,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 주화입마   | **qi deviation**                                 |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마교     | **Demonic Cult**                                 |                                                       |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 기해혈 | **qi-sea acupoint** | Acupoint at the dantian whose destruction releases stored internal energy. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 육부 | **Six Ministries** | The central government ministries. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 986
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 986
- **Aliases:** None
- **Role:** Deceased former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before transferring three jiazi of internal energy to Jin Taekyung and asking him to kill the Western Heaven Demon Lord.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 986
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 986
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃987화



첫 운기조식을 행했던 그 날의 모든 순간을, 나는 지금까지도 똑똑히 기억하고 있다.

기해혈(氣海穴).

하단전이라는 또 다른 이름을 가진 그곳에서 처음으로 마주한 몸 안의 기운은 형편없었다.

기의 바다라는 뜻이 담긴 명칭이 우습게 느껴질 정도로 초라했고, 작은 개울처럼 비좁은 그릇 안에는 한 줌에 불과한 탁한 기운만이 출렁이고 있었을 뿐이었다.

그래.

분명 그랬다.

하지만…….

지금은 다르다.

띠링.



- 돌발 퀘스트, [격체전공]을 시작합니다.

- [격체전공]은 극도의 위험성을 지닌 행위입니다. 공력이 전달되고 흡수하는 과정에 있어 조금이라도 문제가 발생할 시, 주화입마 혹은 사망에 이를 수 있습니다.



서서히 귓가에서 멀어지는 시스템 알림과 함께 육신 깊숙이 스며드는 정신.

그 안의 세상에서 새롭게 깨어난 내 눈 앞에 펼쳐진 광경은, 끝없이 펼쳐진 대해(大海)였다.

콰아아아.

아득하다. 동시에 뜨겁다.

맑고 푸른 물결 대신, 불의 파도가 끊임없이 넘실거린다.

광활하기 그지없는 화염의 바다.

그리고 그 중심에는, 한 마리의 거대한 화룡(火龍)이 칠흑처럼 새카만 암초 위에 똬리를 틀고 누워 있었다.

‘저건…….’

보자마자 본능적으로 알 수 있었다.

온통 불길과 열기만이 가득한 이곳에서, 화룡이 자리 잡은 암초의 존재감은 유난히도 이질적이었으니.

‘천력마(天力魔)에게서 전해 받았던 기운.’

어찌 잊을까.

한때 천하를 떨어 울렸던 마교의 대마두, 천력마는 서천마군을 쓰러트려 달라는 부탁과 함께 내게 공력을 전해 주었다.

비록 수십여 년에 걸쳐 이어진 감금과 고문으로 혹사당한 탓에 그가 지닌 공력의 크기는 과거의 악명에 미치지 못했으나, 어쩌면 그 덕분에 무사히 격체전공이 성공했는지도 몰랐다.

‘과한 힘의 주입은, 그릇을 깨트리는 법이니까.’

그리고 그때 이어받은 천력마의 기운은 지금까지도 여전히 내 안에 남아 있었다.

열화문의 무공으로 비롯된 열양지기(熱陽之氣), 그 자체라 할 수 있는 화룡의 둥지로서.

이는 제법 원만한 공존이자 공생이었지만, 지금 이 순간 나는 본능적으로 깨닫고 있었다.

더 높은 곳으로 오르기 위해서는, 이제는 서로 다른 뿌리를 지닌 두 기운 사이에 맺어진 이 기묘한 관계에 마침표를 찍어야 한다는 것을.

‘깨어나라.’

집중한 정신을 따라 주위가 감응한다.

보이지 않는 울림이 화염의 바다를 휩쓸었다. 그 중심에 우뚝 선 암초 위에 곤히 잠들어 있던 화룡에게 닿았다.

우우웅.

화룡의 거대한 몸뚱어리가 부르르 떨렸다. 마침내 들어 올려진 눈꺼풀 사이로 모습을 드러낸 청백색의 눈동자는, 정확히 나를 향하고 있었다.

세로로 길게 찢어진, 흉포한 맹수의 눈.

하지만 그것에 담긴 감정은 자신의 잠을 깨운 것에 대한 분노가 아닌, 주인을 향한 순종이었다.

당연했다.

화룡도, 암초도, 결국 이 대해에 속한 일부였으니.

몸 안 깊숙이 존재하는 이 광활한 세상의 주인은, 오롯이 나 자신이었으니.

그렇기에 화룡과 눈이 마주친 그 순간, 그 엄청난 열양지기의 집약체는 곧 내 정신과 합쳐질 수 있었다.

화아아악.

따뜻한 온기와 정신이 뒤섞인다.

어느덧 청백색으로 물든 시야 속, 화룡과 하나가 된 나는 망설임 없이 양팔을 떨쳤다.

아니, 덩치만큼이나 거대한 날개를 펼치고 날아올랐다.

콰아앙!

지진이라도 난 듯 뒤흔들리는 암초. 파동과 함께 허공으로 솟아오른 나는 아득한 상공에서 크게 호흡을 삼켰다.

고오옹.

몇 겹으로 응축된 기운이 비명을 내지른다.

내 것이 아니었다면 진즉 전신이 잿더미가 되었을 것만 같은, 실로 끔찍한 열기가 몸속 깊숙한 곳에서 솟구쳐 울대까지 치달았다.

‘지금.’

망설임 따위는 없었다. 마침내 토해진 숨결과 함께 터져 나온 청백색의 화염이 암초를 휘감았다.

세상을 파멸시킬 수도 있는 겁화(劫火) 앞에서, 칠흑처럼 새카만 그것은 형체를 잃고 녹아내리기 시작했다.

더불어 이내, 온 사방에서 넘실거리는 불의 파도에 휩쓸려 솟구쳤다. 앞서 한바탕 겁화를 토해 낸 나는 허공 높이 솟아오른 그것을 향해 입을 벌렸다.

솨아아아.

암초가 녹아든 검붉은 색을 띤 액체를 집어삼킨 그 순간이었다.

‘흡……!’

문득 숨이 막혔다. 마치 보이지 않는 칼날이 오장육부를 사정없이 난자하는 듯했다.

사라진 갈증에 대한 만족감을 느끼기도 전에 정신을 엄습해온 날카로운 통증.

그러나 나는 이를 악물었다.

흔들리는 정신을 다잡고, 다시 목구멍을 타고 튀어나오려는 그것을 온 힘을 다해 삼켜 냈다.

두 번 다시 원래의 모습을 찾을 수 없도록.

이 안에서 새롭게 녹아들 수 있도록.

그렇기에 그 인내과 선택은, 이내 보상받을 수 있었다.

구구궁.

느껴진다.

내 안에서 부풀어 오르는 힘이.

암초. 아니, 천력마의 기운은 소멸한 것이 아니었다.

그것은 흡수인 동시에 또 다른 의미로의 공존이었다.

불완전했던 전과는 달리, 오롯이 하나로 녹아든 완벽한 공존.

그리고 이 놀라운 변화 끝에, 또 다른 무언가가 시작되고 있었다.

쿠르르릉!

화염으로 온통 붉게 물들어 있던 세상이 번쩍였다.

닫혀 있던 하늘을 활짝 열어젖힌 한 줄기의 거대한 번개가, 화염의 바다를 관통했다.

‘아.’

힘의 변화를 오롯이 느끼기도 전에, 나는 진심으로 우러나온 탄성을 흘렸다.

그래.

그것은, 말 그대로의 벽력(霹靂)이었다.

길고도 치열했던 삶의 끝.

죽음의 문턱에 다다른 어느 거인의 상징인 동시에, 나를 통하여 이 세상에 남기고자 한 마지막 유산.

마침내 거궐혈(巨闕穴)을 타고 육신 깊숙이 파고든 그 거대한 번개를 향해, 나는 무언가에 홀린 듯이 다가갔다.

바다와 하늘을 이은 그것을 따라 하염없이 위로, 위로 솟구쳤다.

쐐애애액!

들리지 않는다. 그러나 들리는 듯했다.

맹렬한 바람 소리가.

이제는 오래전부터 내 것처럼 느껴지게 된 화룡의 거대한 몸뚱어리로부터 전해지는 모든 것이.

깊은 곳으로 치달은 의식은 모든 것을 현실처럼 인식했고, 어느덧 대해가 보이지 않을 정도로 높게 솟아오른 나는 마침내 볼 수 있었다.

하늘을 찌를 듯이 우뚝 선, 거대한 산을.

그리고 나는 저 산의 정체를 이미 알고 있다.

‘중단전(中丹田).’

옥당혈(玉堂穴)이라는 이름을 가진 그 산은, 본래의 명칭 그대로 보석처럼 반짝이고 있었다.

단 한 곳. 가장 높은 산봉우리만 빼고.

‘왜? 어째서?’

불현듯 떠오른 머릿속의 의문은, 이내 스스로 찾아낸 답에 의해 지워졌다.

‘아직은 부족하다는 뜻이야.’

중단전을 개방한 지도 벌써 적지 않은 시간이 흘렀지만, 내가 지닌 엄청난 성장 속도에도 최소한의 한계는 있었다.

저 산봉우리는 깨달음의 영역이다.

하늘이 내린 재능과 피나는 노력. 거기에 긴 세월마저 더한 이들만이 들어설 수 있는 영역.

눈부신 속도로 발전에 발전을 거듭한 나로서도 쉽게 넘볼 수 없는 고지(高地).

하지만…….

‘지금이 아니라면, 도대체 언제 다시 도전할 수 있을까.’

나는 수많은 행운을 겪었지만, 천운(天運)은 결코 쉽게 찾아오지 않는다.

하물며 누군가가 죽음을 각오하고 만들어 낸 천운은, 두 번 다시 마주할 수 없는 기회다.

‘가자.’

어쩌면 이 모든 것을 시작한 그 순간부터, 내 안의 망설임은 사라졌을지도 모른다. 시스템의 경고도 의미를 잃었을 것이다.

이미 천력마의 기운을 집어삼킨 나는, 이미 무엇을 해야 하는지 알고 있었다.

치직. 치지지직!

사라지지 않고 계속해서 빛을 뿜어내는 한 줄기의 벽력(霹靂).

그 거대한 빛의 기둥을 향해, 나는 뛰어들었다.

콰아아아아!

눈앞이 새하얗게 물들었다. 천력마의 기운을 흡수했을 때와는 비교도 되지 않는, 끔찍한 격통이 전신의 근육을 쥐어짜고 의식을 증발시켰다.

‘크아아아악!’

모르겠다. 이곳이 어디인지.

뇌리에서 울려 퍼지는 이 처절한 비명이 내 것인지, 아니면 화룡의 것인지.

다만 흐릿해지는 의식 속에서, 천둥 같은 누군가의 고함을 들었을 뿐이었다.

- 갈(喝)!

적천강의 것이 분명한 일갈이 울려 퍼진 그 순간.

“……!”

빠르게 잠겨 가던 의식이 깨어났다.

힘을 잃은 채 축 늘어져 있던 몸뚱어리에 힘이 깃들고, 잊었던 현실의 기억이 되돌아왔다.

내가 누구인지. 이곳이 어디인지.

그리고…….

아직 철없고 모자란 핏덩이를 믿어 준 모두를 위해서, 내가 어찌해야 하는지.

‘버티고, 또 버틴다.’

끊임없이 전신을 찢어발기는 고통을 온 힘을 다해 인내했다.

화룡에 깃든 열양지기 본연의 기운과 조금 전 흡수했던 천력마의 기운을 젖 먹던 힘까지 끌어올려 번개의 기둥을 물어뜯었다.

콰득. 콰드득.

눈앞에 번갯불이 번뜩인다. 한 거인의 모든 것이 담긴 그것은 이제는 고통을 넘어 정신을 마비시키고 있었다.

내게는 참으로 다행스럽게도.

‘시벌, 피똥 한두 번 싸나.’

어느 시점에서부터 나는 미친놈처럼 웃고 있었다.

번개를 물어뜯고, 집어삼키고, 예정된 고통에 까무러칠 듯하면서도 쉬지 않고 그것을 이어 갔다.

시야를 물들이던 그 아득한 섬광이 조금씩 사그라질 때까지.

그리고 마침내, 처음부터 존재하지 않았던 것처럼 완전히 사라질 때까지.

쿠르르릉.

불현듯, 나는 흐릿해진 의식 속에서 깨달을 수 있었다.

중단전과 하단전을 잇고 있던 거대한 번개는 더 이상 존재하지 않는다는 것을.

어디선가 들려온 이 천둥소리가, 내 안에서 울려 퍼지고 있다는 사실을.

‘해냈……다.’

격체전공의 성공을, 진실을 마주한 그 순간.

띠링. 띠링. 띠리리링!

의식의 저 멀리, 맑은 종소리가 쉴 새 없이 울려 퍼지기 시작했다.

그러나 그 소리가 들려온 방향은 아득히 멀어진 하단전의 대해도, 드디어 보석처럼 환한 빛을 내뿜고 있는 중단전의 산봉우리도 아니었다.

나는 고개를 들었고, 보았다.

산봉우리조차 닿지 못한 구름을.

그 구름에 가려져 보이지 않는 또 다른 세상을.

‘상단전(上丹田).’

목이 말랐다. 목적을 이룸과 동시에 실오라기처럼 풀어져 있던 의식이 조금씩 또렷해졌다.

그것은 갈증이었고, 갈망이었다.

‘더, 더, 더……!’

강해지고 싶었다. 나아가고 싶었다.

저 새하얀 구름 위를 뚫고 솟구쳐 올라, 모든 것을 굽어보고 싶었다.

하지만 나는, 목이 타들어 가는 듯한 그 갈증과 갈망을 애써 억눌러야 했다.

이미 한계다.

더 이상의 욕심은 과욕(過慾).

이 찰나의 충동이 가져올 여파를, 나는 이미 알고 있었다.

‘다음에는, 반드시.’

나는 다짐과 함께 온전히 내 것이 된 산과 바다를 굽어보았다.

그리고 마침내 하나로 합쳐진 세 갈래의 기운과 그 거대한 힘의 집합체에 담긴 본질을 처음으로 마주했다.

아니, 그것과 하나가 되었다.

‘아. 아아.’

나는 전율했고, 신음했다.

아득해진 정신 속에서 허우적거렸다.

세 가지의 빛이 뒤섞인 눈부신 광휘에 휩싸인 채, 나를 둘러싼 모든 것을 잊었다.

무아(無我).

그 끝없는 의식의 늪으로 가라앉으며, 환청과도 같은 울림을 들었다.

- 좋은 판단이다. 그때처럼.

생소하게 느껴지면서도, 어디선가 들어 본 것처럼 익숙한 목소리.

그것을 마지막으로, 의식의 끈이 끊겼다.
```

## Final English reading copy

```markdown
# Chapter 987

I still remember every moment of the day I first circulated my qi.

The Qi-Sea Acupoint.

The energy I first encountered inside my body, in the place also known as the lower dantian, was pitiful.

Its name meant “sea of qi,” which felt almost laughable. In that cramped vessel, more like a little stream than a sea, only a handful of murky energy rippled.

That was right.

It had definitely been that way.

But…

Now it was different.

*Ding.*

> **System**
>
> An emergency Quest, **Transmitting Internal Energy Across the Body**, has begun.
>
> **Transmitting Internal Energy Across the Body** carries extreme risks. If anything goes wrong while the internal energy is being transferred and absorbed, it may lead to qi deviation or death.

As the System’s notification gradually faded into the distance, my consciousness sank deep into my body.

The world that spread before my eyes as they opened anew within it was an endless ocean.

*Rooooar.*

It was immeasurable. And hot.

Instead of clear blue waves, waves of fire surged without end.

An ocean of flame, vast beyond measure.

And at its center, a gigantic fire dragon lay coiled atop a reef as black as pitch.

*That’s…*

I knew instinctively the moment I saw it.

In this place, filled with nothing but flames and heat, the reef where the fire dragon had made its home stood out as something especially alien.

*The energy I received from the Heavenly Power Demon.*

How could I forget?

The Heavenly Power Demon, once a great fiend of the Demonic Cult who had shaken the whole world, had passed his internal energy to me and asked me to defeat the Western Heaven Demon Lord.

Though decades of imprisonment and torture had worn him down, leaving him with far less internal energy than his old reputation suggested, perhaps that was why Transmitting Internal Energy Across the Body had succeeded without killing me.

*Put too much power into a vessel, and you break it.*

And the Heavenly Power Demon’s energy, which I’d inherited back then, had remained inside me ever since.

That energy served as the nest of the fire dragon, the very embodiment of Scorching Yang Qi born of the Fire Gate Clan’s martial arts.

It was a fairly harmonious coexistence, even a symbiosis. But in that moment, I instinctively understood.

If I wanted to climb higher, I had to bring this strange relationship between two energies with different roots to an end.

*Wake up.*

The world around me responded to my focused will.

An unseen vibration swept across the ocean of flames. It reached the fire dragon, sleeping peacefully atop the reef at its center.

*Rumble.*

The fire dragon’s massive body trembled. Between its finally lifted eyelids, pale blue eyes appeared—and fixed directly on me.

Slitted vertically, the eyes of a vicious beast.

But the emotion within them wasn’t anger at being woken. It was obedience to its master.

Of course.

The fire dragon and the reef were both, in the end, part of this ocean.

And the master of this vast world deep inside my body was none other than me.

So, the instant our eyes met, that tremendous concentration of Scorching Yang Qi joined with my consciousness.

*Whoosh!*

Warmth and consciousness mingled.

My vision had turned pale blue. One with the fire dragon, I flung out both arms without hesitation.

No—I spread wings as vast as my body and took flight.

*Boom!*

The reef shook as though an earthquake had struck. With a shockwave, I shot into the air and drew a great breath high above.

*Hummm.*

The energy, compressed layer upon layer, screamed.

If it hadn’t been mine, that appalling heat rising from deep inside my body and racing up to my throat would have turned my whole body to ash long ago.

*Now.*

There was no hesitation. With the breath I finally released, pale blue flames burst forth and wrapped around the reef.

Before that hellfire, powerful enough to destroy the world, the pitch-black reef began to lose its shape and melt.

Then it was swept up by the waves of fire surging all around, rising high into the air. Having just breathed out a torrent of hellfire, I opened my mouth toward it.

*Whooosh.*

The moment I swallowed the liquid, its color a dark crimson from the melted reef—

*Gasp…!*

Suddenly, I couldn’t breathe. It was as if invisible blades were savagely carving through my insides.

Before I could feel any satisfaction at the thirst that had finally been quenched, a sharp pain assailed my mind.

But I clenched my teeth.

I steadied my wavering mind and used all my strength to swallow back the energy surging up my throat.

So it could never return to its original form.

So it could melt into me anew.

And for that, my endurance and choice were soon rewarded.

*Rumble.*

I could feel it.

The power swelling inside me.

The reef—or rather, the Heavenly Power Demon’s energy—hadn’t disappeared.

It had been absorbed, and yet in another sense, it was a new kind of coexistence.

Unlike before, when it had been imperfect, now it had melted together into one. A perfect coexistence.

And at the end of this astonishing change, something else was beginning.

*Rrrrrumble!*

The world, all red with flames, flashed.

A massive bolt of lightning split open the closed sky and pierced through the ocean of flames.

*Ah.*

Before I could fully feel the change in my power, a genuine exclamation escaped me.

Yes.

It was lightning, in the truest sense of the word.

The end of a long and fierce life.

The symbol of a giant standing at death’s door, and the final legacy he’d hoped to leave in this world through me.

As that massive bolt of lightning finally entered deep into my body through the Great Palace Acupoint, I moved toward it as if entranced.

I followed it upward and upward, the current joining sea to sky.

*Whooosh!*

I couldn’t hear it. And yet I seemed to hear it.

The sound of the fierce wind.

Everything I felt through the fire dragon’s massive body, which had long since come to feel like my own.

My consciousness raced into the depths, perceiving everything as reality. I had risen so high that the ocean was no longer visible, and at last I saw it.

A gigantic mountain rising like it would pierce the sky.

And I already knew what that mountain was.

*The Middle Dantian.*

The mountain known as the Jade Hall Acupoint glittered like a jewel, just as its name suggested.

There was only one place that didn’t. The very highest peak.

*Why? How come?*

The question surfaced in my mind, but it disappeared as I found the answer myself.

*It means I’m still not ready.*

It had already been quite some time since I opened my Middle Dantian, but even my incredible pace of growth had its limits.

That mountain peak was the realm of enlightenment.

A realm only those with heaven-given talent, blood-soaked effort, and long years behind them could enter.

A lofty height I, too, could hardly aspire to, even after improving at a dazzling pace.

But…

*If not now, when will I ever get another chance to try?*

I’d experienced countless strokes of good fortune, but heavenly fortune never came easily.

And a stroke of heavenly fortune someone had created while prepared to die was an opportunity I’d never see again.

*Let’s go.*

Maybe my hesitation had vanished the moment this all began. The System’s warning no longer mattered.

I’d already swallowed the Heavenly Power Demon’s energy. I already knew what I had to do.

*Crackle. Crackle-crackle!*

A bolt of lightning continued to shine without fading.

I leaped toward its massive pillar of light.

*Rooooar!*

Everything before me turned white. The agony was incomparable to when I absorbed the Heavenly Power Demon’s energy. It squeezed every muscle in my body and vaporized my consciousness.

*Gyaaaah!*

I didn’t know. I didn’t know where I was.

I couldn’t tell whether the desperate scream ringing in my mind was mine or the fire dragon’s.

All I could do, as my consciousness grew hazy, was hear someone’s thunderous shout.

—Hah!

The instant that unmistakably Jeok Cheongang-like shout rang out—

“……!”

My consciousness, sinking fast, awakened.

Strength flowed into my limp, powerless body. Memories of reality, long forgotten, returned.

Who I was. Where I was.

And…

What I had to do for everyone who’d believed in me, a callow, inadequate brat.

*Endure. And keep enduring.*

I bore the unceasing pain tearing through my body with all my strength.

I mustered the Scorching Yang Qi at the fire dragon’s core and the Heavenly Power Demon’s energy I’d just absorbed, down to the last ounce of strength I could summon, and bit into the pillar of lightning.

*Crunch. Crunch.*

Lightning flashed before my eyes. Everything belonging to a giant was contained in that energy. That lightning, holding everything the giant had been, was numbing my mind past the point of pain.

Luckily for me.

*Fuck, it’s not like I’ve never shit blood before.*

At some point, I was laughing like a madman.

I bit into the lightning, swallowed it, and kept going without pause, even as I nearly blacked out from the pain I’d known was coming.

Until the distant flash that had filled my vision slowly dimmed.

And at last, until it vanished completely, as if it had never existed.

*Rumble.*

Suddenly, through my hazy consciousness, I realized:

The massive bolt of lightning that had connected my Middle and Lower Dantians was no longer there.

The thunder I could hear from somewhere was ringing out inside me.

*I did it…*

The moment I faced the truth of Transmitting Internal Energy Across the Body’s success—

*Ding. Ding. Ding-ding-ding!*

From far off in my consciousness, clear chimes began ringing without pause.

But the sound hadn’t come from the ocean of the Lower Dantian, now far in the distance, or from the peak of the Middle Dantian, finally glowing like a brilliant jewel.

I raised my head and saw it.

Clouds the mountain peak couldn’t reach.

Another world, hidden behind those clouds.

*The Upper Dantian.*

I was thirsty. As soon as I achieved my goal, the threadbare strands of my consciousness began to grow clearer.

It was thirst, and it was longing.

*More, more, more…!*

I wanted to grow stronger. I wanted to go farther.

I wanted to pierce through those white clouds, soar above them, and look down on everything.

But I had to force down that burning thirst and longing.

I’d reached my limit.

Any more would be greed.

I already knew what consequences this fleeting impulse would bring.

*Next time. I swear.*

With that vow, I looked down over the mountain and ocean that had become wholly mine.

And for the first time, I faced the essence contained within the three currents of energy, now united, and the vast power they formed together.

No—I became one with it.

*Ah. Ahhh.*

I shuddered and groaned.

I floundered in my distant consciousness.

Enveloped in a dazzling radiance where three lights mingled, I forgot everything around me.

No-self.

As I sank into that endless swamp of consciousness, I heard a voice like a hallucination.

—A wise choice. Just like back then.

A voice that felt unfamiliar, yet strangely familiar, as though I’d heard it somewhere before.

Then the thread of my consciousness snapped.
```
