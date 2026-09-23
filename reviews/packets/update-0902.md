<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0902.txt",
      "sha256": "b8647dc3f9d6edb893b87db25daa8ab3f1d3aa74b88a11847fb6080756594b96",
      "bytes": 13237
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "99dd0cb916f299580dbb8435c47be47cfaedbd689656dcd455c21c05941d7d5c",
      "bytes": 967
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "47bb347a7c127936f379d26c92ebebdffa37c6a718814d982ee32edefbe3a84a",
      "bytes": 759
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "97504749daea4118906ad332fe3f6b371499ab9e5ca88f34aa17522683ebbeeb",
      "bytes": 952
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "21ef60378b93b86ac360c3cd68f19a6f02e07118983e5ec1c398a339a8df4f3a",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "852d5f73b9e4549b425f01d120cf2dd1002fa4e0bfe8e43a35aab4634191e961",
      "bytes": 262237
    }
  ],
  "estimated_tokens": 9269
}
-->

# Durable State Update — Chapter 902

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
1 and safe_through 902. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 902. Profile updates may replace only one
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
  "chapter": 902,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 902,
    "continuity_sources": [902],
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
    "The imperial birthday banquet is underway; the Emperor has arrived after years of seclusion and taken his place on the throne.",
    "The Emperor has forgiven Jin Taekyung for openly mocking him; Taekyung suspects the pardon has a hidden explanation.",
    "Wei Zhong, known as Cang Gong, is the East Depot’s Seal-Holding Eunuch and has recovered enough to attend the banquet.",
    "Wei Zhong and the Emperor have opposing views of the succession, but neither has named his preferred heir.",
    "Prince Shangshan and the pregnant Consort are on their way to the banquet."
  ],
  "continuity_sources": [
    900,
    901
  ],
  "open_questions": [
    "Why did the Emperor forgive Taekyung, and what did Taekyung realize from that response?",
    "Why might the Emperor be smoking opium?",
    "Who does each side regard as the rightful imperial successor?"
  ],
  "safe_through": 901,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 901
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 901
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 901
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃902화



아마도 대국 역사상 최초가 아닐까 싶다.

관직은커녕 호패도 들고 다니지 않는 강호의 무뢰배가, 무려 황제가 주관하는 대연회에서 조정의 고관대작들과 같은 자리에 앉은 것은.

‘최초인 동시에, 앞으로도 없겠지.’

이제 고작 삼 대째 이어져 내려온 짧은 역사를 감안하더라도 충분히 전무후무(前無後無)한 일.

하지만 황실의 체면을 망가트리는 이 조치에 적극적으로 나서서 반박하는 이는 거의 없었다.

굳건한 신념과 용기를 지닌 극소수의 신하들을 제외한다면.

“폐하! 아뢰옵기 황공하오나 저자를 가까이 앉히시는 이 조치는……!”

“황명이다.”

“……실로 옳으신 판단입니다!”

사실, 그 신념과 용기도 황제라는 이름 앞에서는 파도를 만난 모래성처럼 허물어지기 마련이다.

특히 그 황제의 취미이자 특기가 숙청이라면 더더욱.

그리고 그 덕분에 나는 별다른 방해 없이 더 풍성해진 반상 앞에 앉을 수 있었다.

쩝. 쩝쩝. 후루룩.

선명한 사운드와 함께 갖가지 음식을 흡입하는 내 모습에 주위 사람들의 동공이 파르르 떨린다.

특히 라면으로 단련된 신들린 면 치기를 선보였을 때는 곳곳에서 탄식이 터져 나왔다.

“허어어.”

“저런 천하의 상놈을 보았나…….”

“안 그래도 없던 입맛까지 사라지는 광경이군. 저기 보게, 창공 어른께서도 음식에는 손 하나 안 대고 계시잖나.”

마지막으로 들려온 누군가의 말에 슬쩍 고개를 돌리자, 회색빛 눈동자로 나를 지그시 응시하고 있는 창공이 보였다.

음. 너무 심했나.

“다른 이들이 하는 말은 신경 쓰지 말고 계속 들게. 그나저나 그렇게 맛있나?”

창공의 침착한 물음에, 내가 대답했다.

“확시히 마힛헤오.”

“그렇군. 하지만 우선 입에 든 것부터 처리하는 게 좋겠어.”

“에.”

입 안에 꽉 들어찬 음식을 꿀꺽 삼킨 내가 다시 입을 열었다.

“확실히 맛있네요. 반찬 가짓수도 풍성하고.”

창공이 고개를 끄덕였다.

“이미 알아들었네. 그렇게까지 귀가 어둡진 않거든. 그리고 본래 황실의 숙수들은 음식 솜씨가 뛰어나기로 정평이 나 있다네.”

“그런데 왜 안 드십니까?”

“딱히 식욕이 없어. 언제부턴가 그렇게 됐지.”

“흠. 그거 불행 중 다행이네요. 저 때문에 그러시는 줄 알았지 뭡니까.”

“그 부분은 걱정 말게. 젊을 적부터 이래 왔으니까. 다만 이제는 아무리 맛 좋고 귀한 산해진미를 먹어도 모래알처럼 느껴진다는 게 좀 아쉽긴 하지.”

내게서 시선을 뗀 창공은 무표정한 얼굴로 자신의 앞에 놓인 상을 바라보았다.

그야말로 상다리가 휠 정도로 잘 차려진 음식들을 보면서도 그의 손은 시종일관 가지런히 두 무릎 위에 올려져 있었다.

핏기 하나 없는 새하얀, 아니 시체처럼 창백하기까지 한 손.

바로 옆에 있음에도 인기척이 거의 느껴지지 않는 창공을 물끄러미 바라보던 나는, 조용히 입술을 달싹였다.

- 언제 시작할 겁니까?

그 순간.

우우웅.

집중하지 않는다면 느껴지지 않을 만큼 은밀하고 서늘한 기운이 주위를 단단히 틀어막았다.

실로 대단한 솜씨.

빈틈없는 공력의 막으로 소리를 차단한 창공이 입을 열었다.

“신호를 주지.”

“제 생각에는 지금이 적기 같은데요.”

“소교라 불리는 그 여자가 상산왕 전하 곁에 머무르는 한, 섣부르게 경거망동할 수는 없네. 설령 황제의 목을 취하더라도 그분의 신병을 확보하지 못한다면 모든 것이 실패로 돌아갈 테니까.”

“확실히 그것도 그러네요.”

“더군다나 자네의 스승도 아직 대연회장 밖에서 대기 중이지. 화왕은 소교를 쓰러트리기 위해서는 반드시 필요한 인물이야.”

“글쎄요. 제 판단으로는 창공 어르신께서도 제 스승님 못지않은 고수라고 생각됩니다만.”

“노부가 극심한 내상을 딛고 오늘 이 자리에 참석할 수 있던 건 회복하는 과정에서 깨달음이라는 천운이 있었기 때문이지. 중요한 일일수록 확실히 처리해야 하지 않겠나?”

그래, 그렇겠지.

나는 자연스럽게 고개를 끄덕이며 잠시 쉬고 있던 젓가락을 움직였다.

그런 나를 마치 희한한 생물 보듯이 응시하던 창공이 문득 입을 열었다.

“꼭 며칠 굶은 사람 같군.”

“정확하게 보셨습니다. 이틀 동안 거의 아무것도 못 먹었거든요.”

“자네쯤 되는 고수라면 그 정도 굶주림쯤은 감당할 수 있을 텐데.”

“굳이 감당해야 할 이유가 있겠습니까. 싸우기 전에는 든든하게 먹어야 한다는 게 제 지론입니다.”

“떨리지는 않나?”

“떨립니다. 위장이.”

“확실히 스승을 닮아 보통 간담이 아니로군. 듣던 대로야.”

“따로 더 들은 이야기는 없으시고요?”

“그 나이에 전례를 찾아볼 수 없을 만큼 무공이 고강하며, 어떤 위기에서도 살아남을 만큼 임기응변과 생존력이 뛰어나다고 하더군,”

“정확하네요.”

“많이 축약한 거지. 동창의 눈과 귀는 천하 곳곳에 깔려 있고 그들이 전해 오는 소식들은 매번 노부의 예상을 뛰어넘었네. 그중에서도 특히 가장 최근에 들어온 정보는 놀라웠지.”

“뭔지 여쭤봐도 됩니까? 천하의 창공 어른조차 놀라워하신 그 정보가.”

“무림맹의 지원군.”

“아하.”

“정말 예상치도 못했어. 무림맹은 언제 어디에서 나타날지 모르는 암천의 기습에 대처하기 위해 이미 대부분의 전력을 천하 곳곳에 배치한 것으로 알고 있었으니까.”

나는 대답 대신 술잔을 들어 목을 축였다. 천하의 명주답게 향긋한 향이 입안을 가득 채우고, 부드러운 목 넘김이 이어진다.

물론 당연히 동반되어야 할 취기(醉氣)는 그 과정에서 열양지기를 만나 흔적도 없이 사라져 버렸다.

“듣기로는 그자들이 기이하기 짝이 없는 괴력난신(怪力亂神)의 이능을 사용한다던데, 예비대를 편성할 여력이 있었나?”

“여력이 있으니 지원군이 온 것 아니겠습니까.”

“있으니 왔다…… 그래, 그렇겠지.”

창공이 회색빛 눈동자로 나를 지그시 응시하던 그때였다.

“그만.”

웅혼하게 울려 퍼지는 황제의 한마디와 동시에, 대연회장에 울려 퍼지던 아름다운 음율이 씻은 듯이 사라진 것은.

소곤거리며 대화를 나누던 이들도, 가라앉은 얼굴로 술잔을 기울이던 이들도, 이런 분위기 속에서 억지로 연주와 춤을 이어 가던 악공과 무희들도 입을 다물었다.

모두가 움직임을 멈추고, 황제의 목소리와 시선을 따라 고개를 돌렸다.

“이 대륙을, 향후 천년 간 이어질 대국을 이어받을 짐의 후계자가 오고 있나니. 모두 예를 갖춰 맞이하라.”

“……!”

“……!”

명백한 후계자 선포.

모두가 예상했지만, 한편으로는 설마 했던 그 상황을 맞닥트린 대연회장의 사람들은 커다란 충격을 느꼈다.

그러나 바쁘게 움직이는 머릿속과 달리, 그들의 몸은 어느덧 예법에 따라 새롭게 등장한 팔두 마차를 향해 기울어지고 있었다.

둥. 둥둥. 둥둥둥!

고수(敲手)의 힘찬 북소리에 맞춰 대기가 요동친다. 잔잔하게 끓어오르는 분위기 속에서, 마차의 문이 열리고 한 사람이 발을 내디뎠다.

스륵.

화려하기 그지없는 붉은 궁장의 밑단이 지면을 스친다. 넙죽 엎드린 궁인의 등을 사뿐히 밟고 마차에서 내린 여인의 고혹적인 용모에, 어디선가 낮은 탄성이 흘러나왔다.

“허어.”

“이럴 수가.”

눈치 없는 짓이었지만, 한편으로는 이해했다.

그만큼 여인의 용모는 실로 경국지색(傾國之色)이라는 표현이 아깝지 않을 정도였으니까.

‘그러니 사천성주가 그만큼 빠져들었겠지.’

나는 내심 중얼거리며 여인, 아니 애향을 바라보았다.

불과 몇 달 전까지만 하더라도 사천성주의 애첩이었던 그녀는, 왠지 모르게 불안한 얼굴로 자신의 배를 어루만지며 금의위의 철통같은 호위 아래에 걸음을 옮겼다.

그리고 모두의 시선이 그녀를 따라 움직이던 그때, 나는 아직 닫히지 않은 마차의 문에서 뒤이어 내리는 또 다른 한 사람을 볼 수 있었다.

아직까지는 어린아이에 머물러 있는 얼굴.

하지만 여느 청년보다도 당찬 표정과 발걸음.

바로 상산왕 주표였다.



* * *



높게 이어진 계단을 성큼성큼 걸어 올라가는 상산왕을 보며 나는 문득 생각했다.

무슨 말을 해야 할까.

며칠 만에 다시 만난 어린 왕에게, 어떤 첫인사를 건네야 할까.

고민은 그리 길지 않았다.

- 잘 지내셨습니까?

공간을 가로질러 도달한 내 전음에, 상산왕의 발걸음이 우뚝 멈춘다. 그 모습을 보며 내심 피식 웃은 내가 재차 입술을 달싹였다.

- 제가 맡긴 물건은, 여전히 잘 지니고 계시고요?

잠시 멈췄던 걸음이 다시 나아간다. 상산왕은 내 쪽을 바라보지 않았지만, 손등을 덮은 옷소매를 펄럭이는 것으로 답을 대신했다.

그 순간 언뜻 보이는 거무튀튀한 반지.

내가 만독지환(萬毒指環)을 확인한 뒤 고개를 끄덕이던 그때, 창공이 불쑥 입을 열었다.

“다행이군. 전하께서 아직 잘 지니고 계신 것 같으니.”

나는 놀라지 않았다.

창공은 아직 나조차도 엿보지 못한 영역에 도달한 고수. 전음을 훔쳐 듣는 것 정도는 충분히 가능할 거라 여겼기 때문이었다.

“그러게 말입니다. 잃어버리면 어쩌나 했는데, 다행이네요.”

고개조차 돌리지 않고 담담하게 대답하는 나를 물끄러미 바라보는 시선이 느껴졌지만, 창공의 그 시선은 이내 다른 사람을 향해 옮겨 갔다.

‘소교(小嬌).’

그녀가 보인다.

조용한 걸음으로 상산왕의 뒤를 따르는 그녀가.

연검 대신 마치 곡도(曲刀)처럼 비스듬하게 휘어진 두 자루의 병기를 허리춤에 찬 소교는 정확히 나를 바라보며 흐릿하게 웃어 보였다.

“봤나?”

창공의 물음에, 나는 침착하게 대답했다.

“봤습니다.”

“자네를 향해 웃고 있더군.”

“그렇습니까? 저는 창공 어른이라고 생각했는데요.”

“착각일세. 조금 전의 그 시선…… 정확히 자네를 바라보고 있었어.”

“마 태감에게 들어서 알고 계시겠지만, 어느 정도 안면이 있긴 합니다.”

“이유는 그것뿐인가?”

“다른 이유가 뭐가 있겠습니까?”

“천세(千歲)! 천세(千歲)! 천천세(千千世)!”

조정의 대소신료는 물론, 물경 이천에 달하는 금의위가 대국의 후계자를 향해 힘차게 내지르는 함성이 온 사방을 떨어 울린다.

그것이 단지 장단을 맞추기 위한 목적으로 비롯된 것이든, 진심으로 이 상황을 축하하는 것이든 그들 모두는 한 목소리로 외치고 있었고 그 거대한 환호의 중심에는 황제와 애향. 마지막으로 상산왕이 있었다.

그리고 내 옆자리에는, 유일하게 만세를 부르짖지 않는 유일한 사람이 있었다.

“문득 자네의 생각이 궁금해지는군.”

창공은 내 대답을 기다리지 않고 말을 이었다.

“용서받지 못할 불경을 저질렀음에도, 왜 황제는 자네를 용서했을까? 명분과 실리를 동시에 챙기며 상산왕 전하를 축출할 절호의 기회였을 텐데.”

“글쎄요. 잘 모르겠습니다. 제가 좀 단순한 편이라서요.”

“단순하다라, 그럼 갑작스럽게 계획에도 없이 그런 짓을 저지른 것도 전부 자네의 성격에서 비롯된 것인가?”

“그렇다면 그런거고, 아니라면 아닐 수도 있습니다.”

“더 자세히.”

“대계고 나발이고, 여러 사람의 목숨이 걸린 만큼 한 가지를 꼭 확인해봐야 했거든요.”

창공은 더 이상 황제가 서 있는 옥좌를 바라보지도, 그곳을 향해 허리를 굽히지도 않았다. 그는 꼿꼿이 허리를 편 채 회색빛 눈동자로 나를 바라보았다.

“그래서, 확인은 끝났나?”

“예.”

“결론은?”

“아무리 생각해도, 하나뿐이었습니다.”

나는 조용히, 그러나 뜨겁게 달구어진 눈동자로 창공을 응시하며 입을 열었다.

“황제는, 상산왕이 위기에 빠지는 걸 원치 않는다.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 902

This might have been a first in the history of the Great Nation.

A ruffian from the martial world who didn’t even hold an official post—or carry an identity token—sitting at the same table as the court’s high-ranking officials at a grand banquet presided over by the Emperor himself.

*The first, and probably the last.*

Even considering the short history of the Great Nation, which had only lasted three generations so far, it was a feat unlikely ever to be repeated.

Yet almost no one spoke up to object to this measure, which trampled on the imperial family’s dignity.

Not unless they were among the handful of ministers with unwavering convictions and courage.

“Your Majesty! Forgive my boldness, but this measure of seating that man so close to you—”

“It is the imperial decree.”

“……It is indeed a wise decision!”

As a rule, even conviction and courage crumbled like a sandcastle hit by a wave when faced with the Emperor.

Especially when that Emperor’s hobby—and specialty—was purging people.

Thanks to that, I was able to sit down without much fuss in front of an even more lavish spread.

*Smack. Smack-smack. Slurp.*

At the vivid sound of me inhaling one dish after another, the pupils of the people around me trembled.

When I showed off the godlike noodle-slurping technique I’d honed on ramen, groans broke out from all over.

“Good heavens.”

“Have you ever seen such a low-class bastard…?”

“What a sight. It’s enough to kill what little appetite I had. Look over there—even Cang Gong hasn’t touched a single thing.”

At someone’s last remark, I casually turned my head. Cang Gong was gazing steadily at me with his gray eyes.

*Hmm. Was that too much?*

“Pay no mind to what the others say. Keep eating. By the way, is it that good?”

At Cang Gong’s calm question, I answered.

“Definithely delishious.”

“I see. But you should probably finish what’s in your mouth first.”

“Oh.”

I swallowed the mouthful crammed into my cheeks, then spoke again.

“It’s definitely good. There’s a great variety of side dishes, too.”

Cang Gong nodded.

“I understood you the first time. My hearing isn’t that bad. Besides, the imperial chefs have long been renowned for their skill.”

“Then why aren’t you eating?”

“I don’t particularly have an appetite. It’s been that way for some time.”

“Hmm. That’s lucky, at least. I thought it was because of me.”

“Don’t worry about that. I’ve been this way since I was young. Still, it is a little disappointing that even the finest and rarest delicacies taste like grains of sand now.”

Cang Gong took his eyes off me and looked at the table in front of him, his face expressionless.

It was laden with enough food to make the table legs bow under the weight, yet his hands remained neatly on his knees the whole time.

They were so white they had no color in them—or rather, so pale they looked like a corpse’s hands.

I studied Cang Gong, sitting right beside me yet barely giving off any sense of presence. Then I quietly moved my lips.

“When are we going to start?”

At that moment—

*Vrrrm.*

A subtle, chilling qi sealed off the area so tightly that it would have gone unnoticed without careful attention.

A remarkable feat.

Cang Gong had raised a flawless barrier of internal energy to block out sound. He spoke.

“I’ll give the signal.”

“I think now would be the perfect time.”

“As long as that woman called So Gyo remains by Prince Shangshan’s side, we can’t act rashly. Even if we take the Emperor’s head, everything will be for nothing if we can’t secure His Highness.”

“That’s true.”

“Besides, your master is still waiting outside the banquet hall. The Fire King is essential if we’re to defeat So Gyo.”

“Maybe. But I think you’re every bit the master my teacher is.”

“This old man was able to overcome a grave Internal Injury and attend today thanks to the good fortune of gaining insight during my recovery. The more important the matter, the more carefully it must be handled, don’t you think?”

Yeah, that made sense.

I nodded naturally and resumed moving the chopsticks I’d set down for a moment.

Cang Gong, who was watching me as if I were some strange creature, suddenly spoke.

“You look like you haven’t eaten in days.”

“You’ve got that right. I barely ate anything for two days.”

“A master of your caliber should be able to endure a little hunger.”

“Why should I have to endure it? My principle is to eat a hearty meal before a fight.”

“Are you nervous?”

“I am. My stomach is.”

“You really do take after your master. You’ve got quite a nerve, just as I’d heard.”

“Did you hear anything else about me?”

“I heard that, at your age, your martial arts are without precedent—and that your quick wits and survival skills are good enough to see you through any crisis.”

“Sounds about right.”

“That was the abbreviated version. The East Depot has eyes and ears all across the land, and the reports they bring me always exceed my expectations. One of the most recent reports was particularly surprising.”

“May I ask what it was? What could have surprised even Cang Gong?”

“The Murim Alliance reinforcements.”

“Ah.”

“I truly didn’t expect that. I thought the Murim Alliance had already deployed most of its forces throughout the land to deal with sudden attacks by Dark Heaven, which could appear anywhere at any time.”

Instead of answering, I lifted my cup and wet my throat. A fragrant aroma filled my mouth, befitting the finest liquor in the land, followed by a smooth swallow.

Of course, the drunkenness that should have come with it vanished without a trace when it met my Scorching Yang Qi.

“I hear they use the strangest supernatural powers. Did the Alliance really have enough strength left to form a reserve force?”

“They wouldn’t have come if they didn’t.”

“They came because they had enough… Yes, I suppose so.”

Cang Gong was gazing steadily at me with his gray eyes when—

“Enough.”

The Emperor’s resonant voice rang out, and in the same instant, the beautiful music that had filled the grand banquet hall vanished as if it had been washed away.

Those who’d been whispering to one another, those who’d been drinking with solemn expressions, even the musicians and dancers who’d forced themselves to continue performing in that atmosphere—all fell silent.

Everyone stopped moving and turned toward the Emperor, following his voice and gaze.

“The heir who will inherit this continent, the Great Nation that shall endure for the next thousand years, is on his way. Receive him with the proper ceremony.”

“……!”

“……!”

It was an unmistakable declaration of the heir.

Everyone had expected it, and yet had thought it couldn’t possibly happen. Now that they were facing the moment, a great shock swept through the people in the hall.

But while their minds raced, their bodies had already begun to bow according to protocol toward the newly arrived eight-horse carriage.

*Boom. Boom-boom. Boom-boom-boom!*

The vigorous drumbeats of the drum master made the air shudder. In the quietly building tension, the carriage door opened, and someone stepped out.

*Swish.*

The hem of a splendid red palace gown brushed the ground. The woman alighted from the carriage, stepping lightly on the back of a palace attendant who had prostrated himself before her. Her bewitching beauty drew a low gasp from somewhere in the hall.

“Good heavens.”

“This can’t be…”

It was an unwise thing to say, but understandable all the same.

The woman’s beauty was so extraordinary that “beauty capable of toppling a kingdom” hardly seemed an exaggeration.

*No wonder the City Lord of Sichuan Province fell for her.*

I thought to myself as I looked at the woman—or rather, Aehyang.

Until only a few months ago, she had been the City Lord of Sichuan Province’s favored concubine. Now she walked under the unyielding protection of the Embroidered Uniform Guard, uneasily caressing her belly.

And just as everyone’s eyes followed her, I saw another person step out through the still-open carriage door.

A face that still belonged to a child.

Yet his expression and stride were bolder than those of any young man.

Prince Shangshan, Zhu Bao.

* * *

As I watched Prince Shangshan stride up the tall staircase, I wondered what I should say.

What kind of greeting should I offer the young prince, whom I was seeing again after several days?

I didn’t have to think for long.

“Have you been well?”

My Sound Transmission crossed the space between us, and Prince Shangshan’s steps came to an abrupt halt. Seeing him stop, I let out a quiet laugh to myself and moved my lips again.

“Are you still keeping the item I entrusted to you safe?”

After a brief pause, his steps resumed. Prince Shangshan didn’t look my way, but he answered by flicking the sleeve over the back of his hand.

For a moment, I caught sight of a dark, dull ring.

I nodded after spotting the Myriad-Poison Ring, and Cang Gong suddenly spoke up.

“Good. It seems His Highness is still keeping it safe.”

“Sure is. I was worried he might lose it, but I’m glad he hasn’t.”

I answered calmly without even turning my head. I felt Cang Gong’s gaze lingering on me, but it soon shifted to someone else.

*So Gyo.*

I saw her.

She followed quietly behind Prince Shangshan.

Instead of her flexible sword, she wore two weapons at her waist, each curved at an angle like a saber. So Gyo looked straight at me and smiled faintly.

“Did you see that?”

At Cang Gong’s question, I answered calmly.

“I did.”

“She was smiling at you.”

“Really? I thought she was smiling at you, Cang Gong.”

“You’re mistaken. That gaze just now… she was looking straight at you.”

“I’ve met her before, as Eunuch Ma probably told you.”

“Is that the only reason?”

“What other reason could there be?”

“A thousand years! A thousand years! A thousand thousand years!”

The civil and military officials of the court, along with two thousand Embroidered Uniform Guards, roared their cheers toward the heir of the Great Nation, shaking the whole place.

Whether they were merely going along with the occasion or were genuinely celebrating it, they all chanted with one voice. At the center of that immense cheer stood the Emperor, Aehyang, and finally, Prince Shangshan.

And beside me sat the only person who wasn’t crying out “Long live.”

“I find myself wondering what you think.”

Cang Gong continued without waiting for my answer.

“Why did the Emperor forgive you, despite your unforgivable disrespect? It was the perfect chance to remove Prince Shangshan while gaining both a pretext and a practical advantage.”

“I don’t know. I’m a pretty simple guy.”

“Simple, you say? Then was that stunt you pulled all of a sudden, without any plan, simply a result of your personality?”

“If that’s what it was, then it was. If it wasn’t, maybe it wasn’t.”

“Explain.”

“To hell with the grand plan. A lot of people’s lives were at stake, so there was one thing I had to make sure of.”

Cang Gong no longer looked toward the throne where the Emperor stood, nor did he bow toward it. He held himself straight and looked at me with gray eyes.

“So, have you finished checking?”

“Yes.”

“And your conclusion?”

“No matter how I look at it, there could only be one.”

I met Cang Gong’s gaze with eyes that were quiet, yet burning hot, and spoke.

“The Emperor doesn’t want Prince Shangshan to be put in danger.”

“……!”
```
