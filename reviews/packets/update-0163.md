<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0163.txt",
      "sha256": "6ab6d9302c6f72943ea52f5c006fc975412c7789765c3d12cf82ef5543058652",
      "bytes": 15450
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d25567ccd28c03229051ae491db75165bc8de35054f45ca568e97f2f869dc7ea",
      "bytes": 8268
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8954e325f1840d348b98a9f58885f00d67a5f1e807d54c5e083c5e4ed91c59c0",
      "bytes": 39899
    },
    {
      "path": "characters/Black Sand.md",
      "sha256": "b1ed05881e1f06fd105e7fbe3aa7665d6fc656c053e4d1a21aacf74368f2f80a",
      "bytes": 944
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "7fb6deaace5755556b9f3e2888e0100802be3d4fe299bd77e1b921c2ca55e4c9",
      "bytes": 611
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "0085026b4604f9b72d7d431a8a15cc41043c217ab7bcb68be5e43e0b77d3355f",
      "bytes": 667
    },
    {
      "path": "characters/Temur.md",
      "sha256": "3f6cf325bc6cf102efdd29563fae24b3aeafd0425bf907a2c7f1c14d3fa37f4c",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3dd84a9df70d77d64d03013dd541585b2c591c3728499d02ba2ffaf3ebedf04e",
      "bytes": 31272
    }
  ],
  "estimated_tokens": 29721
}
-->

# Durable State Update — Chapter 163

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 163. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 163. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 163,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 163,
    "continuity_sources": [163],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The City Lord's luncheon requirement concluded with Prince Shangshan's Token obtained as the Quest Reward; Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days. Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung completed Beyond the Wall after spending 50 points on Agility and 50 on Strength; the System changed his class to Peak Master, and his weapon resonated with his energy.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is twenty years old, a Peak master raised by Mae Jonghak, knows numerous Huashan martial arts, can use the Zaha Divine Technique and Sword Energy, has no martial title, and teaches Taekyung and Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence for at least ten years; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is Huashan's Lone Crane and the first of the Three Plum Blossom Elites; Chulwoo and Eunhyang are his junior disciples and fellow Elites, and all three are traveling to meet Cheongpung again.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk; the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served him since infancy, and is the power behind the Shanxi Provincial Office.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung is the thirty-five-year-old Lesser Family Head and future Family Head, directing the Jin Family's expansion and branch stabilization while aiming to establish it as a great family.",
    "Taekyung previously failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung has a private training ground in a rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung, and their Wall Lizard Technique training is complete.",
    "Wipeng offered to personally lead useful martial artists against approximately five hundred mounted bandits gathering near Datong; Huashan sent the Three Plum Blossom Elites and reported Mae Jonghak missing.",
    "Cheongpung canceled the second Sword Saint-training Quest by his own decision without penalty, postponing the unfinished duel with Taekyung.",
    "Cheongpung had only ever sparred with Mae Jonghak before leaving Huashan and is adjusting with difficulty to fighting people outside his grandfather's instruction; he considers Taekyung and Jin Mukyung the strongest people he has met since leaving Huashan.",
    "Cheongpung identifies Taekyung's rough, unrefined martial arts and naturally emerging aura as Wildness; Taekyung can increasingly read and imitate Cheongpung's forms during sparring.",
    "Hyuk Mujin has resolved to become strong enough to be remembered as Jin Taekyung's right arm or heart and by the name Hyuk Mujin; he is now Level 50 after recent training and sparring.",
    "Taekyung's Peak breakthrough completed Beyond the Wall, changed his class to Peak Master, raised Jin Family's Cultivation Technique to the ninth stage and Qi Sense to the seventh stage, unlocked trainable Sound Transmission, and awarded Ten-Thousand-Year Cold Iron plus the Find the Craftsman Quest.",
    "Black Sand, Temur, Chinggen, and the Human Butcher gathered to plan the Black Sand alliance's attack on the Jin Family of Taiyuan; an unnamed old man entered, revealed Supreme Peak mastery, and killed the Human Butcher in one move."
  ],
  "continuity_sources": [
    161,
    162
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and did he actually go to the Jin Family after breaking seclusion to find Cheongpung?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?",
    "Who is the unnamed old man who entered the Northern Gaoyuan gathering and demonstrated Supreme Peak mastery?"
  ],
  "safe_through": 162,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally; render 초일류 as “advanced First Rate,” 군문 as “military,” 풍운검군 as “Wind-and-Cloud Sword Lord,” and 오촌 당숙 as “father's cousin.”",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” 광염 as “light-flames,” 검명 as “Sword Cry,” and 창명 as “Spear Cry.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” 환골탈태 as “Bone Transformation,” and 전음 as “Sound Transmission.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” 낙안봉 as “Falling Goose Peak,” 대초원 as “Great Steppe,” 마유주 as “mare's-milk wine,” 게르 as “ger,” and 북부 고원 as “Northern Gaoyuan.”",
    "Render 황하방 as “Yellow River Gang,” 소공문 as “Sogong Sect,” 남부상회 as “Southern Merchant Guild,” 내당주 as “Inner Hall Master,” 내외당 as “Inner and Outer Halls,” 세가 as “great family,” and 한족 as “Han Chinese.”",
    "Render 암향표 as “Dark Fragrance Drift,” 복호권 as “Crouching Tiger Fist,” 천근추 as “Thousand-Catty Drop,” 야성 as “Wildness,” 오행매화보 as “Five-Element Plum Blossom Steps,” 공수납백인 as “Empty-Hand Seizes the Blade,” 매화오품지 as “Plum Blossom Five-Point Finger,” 벽을 넘어서 as “Beyond the Wall,” and 절정 고수 as “Peak Master.”",
    "Retain Taekyung's instant-noodle flavor joke with “mild Neoguri,” “Jin Ramen spicy flavor,” and “Puramyeon spicy flavor”; render 천근거력 as “the force to move a thousand catties,” 인도 as “Human Butcher,” 대칸 as “Great Khan,” 텡게르 as “Tengger,” and preserve the 무공/무공 wordplay as “martial arts” and “empty space.”",
    "Render 흑사 as “Black Sand,” 흑사대 as “Black Sand Band,” 천풍단 as “Heavenly Wind Band,” 천풍단주 as “Heavenly Wind Band Leader,” and 하곡 as “Hequ”; render 참마검 as “horse-chopping sword,” 칠공 as “seven orifices,” and preserve the old man's abrasive vulgar voice."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 참마검 | **horse-chopping sword** | Heavy saber used by the Human Butcher; rendered descriptively. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |

## Exact glossary matches

| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 장법     | **palm technique**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 귀가      | **your family**                                                 |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |

## Listed compact profiles

### Black Sand.md

# Black Sand (흑사)

- **Safe through:** Chapter 162
- **Aliases:** None
- **Role:** Leader of the Black Sand Band, a Han-Chinese mounted-bandit power of one hundred; secretly commands the five-hundred-member Heavenly Wind Band through its leader and organizes the planned attack on the Jin Family of Taiyuan
- **Personality:** Frivolous and warm on the surface but calculating, bold, authoritative, and adept at manipulating dangerous people through humor and grand promises
- **Voice:** Light, teasing, and conversational in ordinary speech; becomes firm and decisive when directing the alliance
- **Relationships:** Commands the Black Sand Band and the subordinate Heavenly Wind Band; recruited the Human Butcher, Temur, and Chinggen into a four-way alliance against the Jin Family of Taiyuan, but the Human Butcher was killed by an unnamed old man during their gathering

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 162
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his fellow chieftain, and Chinggen repeatedly restrains Temur's recklessness; Black Sand recruited both chieftains into a four-way alliance to attack the Jin Family of Taiyuan

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 162
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 162
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and hostile to Han Chinese encroachment
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his fellow chieftain and restrains him from provoking the Human Butcher; both chieftains accepted Black Sand's proposal for a four-way alliance to attack the Jin Family of Taiyuan

## Korean source

```text
＃163화



“뭐라? 북부 고원? 원단까지 사흘밖에 안 남았어?”

“예.”

“허, 참.”

노인은 입을 다물었다. 앞에는 세 우두머리와 이백여 명의 졸개들이 공손히 무릎을 꿇은 채 그의 입만 바라보는 중이었다.

“그 말이 정녕 사실이냐?”

“트, 틀림없습니다.”

“저희가 감히 뉘 안전이라고 거짓을 고하겠습니까.”

“……그렇군.”

필사적인 변명에 노인의 표정이 어두워졌다.

그도 저들의 말이 사실이란 걸 안다. 다만 조금이라도 부정하고 싶었을 뿐이다. 자신이 늙어 가고 있다는 사실을.

‘칠 주야 동안 정신을 놓고 있었단 말이지. 칠 주야…… 점점 길어지고 있군.’

노환 때문이다.

이상한 징후를 느낀 것은 이십여 년 전이었다. 연공 도중 정기신(精氣神)이 어긋나는 것을 깨닫고 세월이 찾아왔음을 알았다.

이미 백수(白壽)에 가까운 나이. 죽음은 두렵지 않지만 정신 나간 노인으로 기억되기는 싫었다.

‘그토록 애썼건만…….’

이제는 한계다. 세월이 내리는 저주는 이 갑자의 공력으로도, 초절정 고수의 강기로도 막아 낼 수 없다.

자그마치 이십 년간이나 노환을 늦춘 것만으로도 만족해야 한다. 노인은 애써 씁쓸한 마음을 털어 냈다.

“술이나 한잔 따라 봐라.”

“저어, 술이 식어서 새로 준비 중입니다.”

조심스러운 흑사의 대답에 노인이 쯧쯧 혀를 찼다.

“어느 세월에? 상관없으니 식은 술이라도 가져와 보거라.”

“예.”

누구의 명인데 토를 달까. 흑사의 눈짓에 힘깨나 쓰게 생긴 마적 두 명이 술동이를 낑낑거리며 가져왔다.

사람 가슴께까지 닿을 만큼 거대한 술동이는 반쯤 식은 마유주로 출렁이고 있었다.

“쯔쯧. 젊은 놈들이 비실거리기는. 너희 밑에 애들 밥 안 챙겨 줘?”

“그, 그럴 리가 있겠습니까.”

“그런데 왜 이리 힘을 못 써? 에잉. 보고 있자니 답답해서 안 되겠다.”

벌떡 일어난 노인이 술동이를 뺏어 들었다. 수백 근은 족히 나가는 술동이가 한 손으로 번쩍 들린다.

뼈밖에 남지 않은 몸뚱어리에서 어찌 저런 힘이 솟구치는지 불가사의할 지경이다. 흑사는 자신의 눈을 찌르고 싶었다.

‘내가 미쳤지. 저런 노괴(老怪)를 그저 정신 나간 노인네라고 생각했으니.’

그나마 말이라도 조심해서 다행이다. 늙은이 운운하며 검까지 휘두르던 인도는 끔찍한 몰골로 죽지 않았나.

흑사는 칠공으로 피를 흘리며 죽는 최후를 원하지 않았다.

“어르신! 제가 하겠습니다!”

“어르신 같은 소리 하고 있네. 헛소리하지 말고 앉아.”

“아닙니다. 마유주는 뜨끈하게 먹어야 제맛이 살아나는 법. 제가 직접…….”

“뜨끈하게, 뭐?”

흑사는 할 말을 잃었다. 다음 순간, 술동이로부터 엄청난 열기가 확 뿜어져 나왔기 때문이다.

열기의 근원지는 술동이를 잡고 있는 노인의 손이었다.

보는 것만으로도 숨이 막히고 소름이 돋는 백염(白炎)은 순식간에 술동이를 달구고 마유주를 덥혔다.

“이, 이건.”

“사, 삼매진화(三昧眞火)?”

테무르와 칭겐, 그리고 이백여 명의 졸개들은 눈앞의 광경에 아연실색했다.

그중에서도 특히 우두머리들이 받은 충격은 엄청났다.

‘이런 미친!’

‘저 정도 크기의 술동이를 삼매진화로?’

‘어마어마한 공력이다. 이 늙은이, 도대체 정체가 뭐야?’

삼매진화는 공력을 태워 일으키는 불로, 심후한 공력이 뒷받침되는 절정 고수라면 어렵지 않게 쓸 수 있다.

하지만 막대한 공력 소모에 비해 화력이 미약해 실전에서 쓰기에는 턱없이 비효율적이었다.

“사발이나 가져와, 큰 걸로.”

그런데 눈앞의 이 노인은 어떤가.

비록 순간이었지만 그들이 느낀 열기는 어마어마했다. 그가 원한다면 사람을 해하는 것은 물론이고 강철도 녹여 버릴 수 있을 듯했다.

‘무공과 공력이 이미 입신지경에 이르렀군.’

‘삼매진화뿐만이 아니야. 공력 자체도 엄청난 열양지기다.’

‘입 벙긋하지 말자. 말 한마디 잘못했다가는…… 죽는다.’

꿀꺽, 마른침을 삼킨 세 사람은 손님을 맞이한 점소이처럼 재빠르게 움직였다.

“소인이 한 잔 올리겠습니다.”

“고기 가져와, 고기!”

“다리만 뜯어 와!”

초원에서는 사신으로 통하는 흑사대의 대주가 마유주를 따르고, 위대한 칸의 후예이자 수백의 기마 전사를 거느린 두 명의 부족장은 탁자를 돌며 야들야들한 다리 부위만 북북 뜯어 대령한다.

금을 주고도 보기 힘든 광경이었다.

“음. 이래서 싸가지 없는 놈들은 맞아야 해. 꼭 혼쭐이 나고서야 예의라는 걸 알게 되거든.”

“맞습니다. 어르신.”

정성껏 발라낸 고기 한 점에 마유주를 곁들이던 노인이 멈칫했다.

“어르신?”

“예, 예. 제가 무슨 실수라도?”

“나이 들어 보이잖아. 꼭 금방 죽을 것 같은 노인네처럼.”

예. 진짜 곧 가실 것 같은데요.

흑사는 튀어나오려던 말을 겨우 참았다. 상대는 경지를 짐작하기 힘든 절대 고수다. 어떻게든 노인의 비위를 맞춰야 했다.

“그럼 형님…….”

“내가 만만하냐?”

“죄, 죄송합니다!”

쿵!

불문곡직하고 바닥에 머리를 박은 흑사는 죽을 맛이었다. 노야는 늙어서 싫고, 형님은 만만해 보인다고 지랄하니 어쩌란 말인가.

엎드려 있는 흑사를 노인이 툭, 발로 찼다.

“일어나라.”

“옙!”

“거기 이마 까진 두 놈도.”

후다닥!

열심히 고기를 발라내고 있던 테무르와 칭겐도 빛의 속도로 달려와 무릎을 꿇었다.

마유주를 쭉 들이켠 노인이 그제야 입을 열었다.

“그래서, 너희는 뭐 하는 놈들이냐?”

마적. 그리고 마적이나 다름없는 유목민.

척 봐도 정파의 고인으로 보이는 노인에게 사실대로 털어놨다가는 어떤 꼴을 당할지 모른다.

세 사람이 필사적으로 눈빛을 교환하던 순간이었다.

빡! 빡! 빡!

“컥!”

“헉!”

“악!”

보이지도 않는 속도로 꿀밤을 한 대씩 쥐어박은 노인이 눈을 부라렸다.

“썅노무 새끼들. 어른이 물어보시는데 눈깔만 굴려?”

“죄, 죄송합니다. 어르신.”

“내가 어르신이라고 하지 말했지. 지금 나 죽으라고 고사 지내냐? 어?”

빠박!

괜히 대답했다가 한 대 더 맞은 흑사는 눈물이 날 것 같았다. 나도 오십이 넘었는데, 수하들도 지켜보고 있는데…….

“제일 나이 많은 놈부터 대답해 봐.”

흑사는 촉촉한 눈빛으로 노인을 바라보며 입을 열었다.

“소인은 그러니까, 마음 맞는 형제들과 말을 벗 삼아 초원을 유랑하는…….”

“쓰레기 같은 마적 놈이지. 틈만 나면 약탈과 살인, 방화를 일삼는.”

“…….”

경멸 가득한 눈빛으로 흑사를 바라보던 노인이 고개를 돌렸다. 테무르와 칭겐이 움찔하며 머리를 숙였다.

“네놈들도 말이 유목민이지 별반 다를 바 없고. 내 말이 틀렸느냐?”

“아, 아닙니다.”

“지당하신 말씀이십니다.”

“그나마 네놈들이 마적보다 나은 점은 약탈, 살인은 해도 여기저기 불을 싸지르는 방화범들은 아니라는 거다. 남의 집에 불 지르는 놈들은 때려죽여도 시원치 않아!”

“……?”

“……?”

“……?”

보통은 살인을 가장 중죄로 여기지 않나?

뭔가 이상한 느낌에 고개를 갸웃거리는 세 사람에게 다시 한번 불벼락이 떨어졌다.

빡, 빡, 빡!

“어쨌든 네놈들이 어디서 굴러먹다 온 놈들인지는 대충 안다. 내가 궁금한 것은 이 근방에서 어느 정도로 영향력이 있냐는 것이다.”

“어흑……. 영향력이라 하시면?”

“말 그대로다. 끗발 좀 되냐?”

정수리를 어루만지던 세 사람이 신중하게 대답했다.

“소인들이 힘을 합치면 당할 자가 많지 않습니다.”

“저희는 대부분 분가(分家) 형태라 많이 쪼개져 있긴 합니다만, 일가 친인척이 모이면 능히 수십 개 부족은 채우고도 남습니다.”

“초원에서 벌어지는 소식들은 빠짐없이 주고받는 편입니다.”

마지막으로 대답한 칭겐의 말에 노인의 눈이 번쩍 빛났다.

“오호, 그거 괜찮군.”

눈치 빠른 칭겐은 노인이 원하는 것이 정보라는 사실을 알아차리고 넙죽 대답했다.

“혹시 정보가 필요하시면 뭐든 알려 드리겠습니다.”

“사람 하나를 찾고 있다. 정확히 어디 있는지는 잘 모르지만…… 아마 그리 멀리 있지는 않을 게야. 가능하겠느냐?”

“예. 혹시 용모나 특징을 알려 주신다면 더욱 쉽습니다.”

“기다려 보거라.”

노인이 품에서 꼬깃꼬깃 접힌 화선지를 꺼냈다. 제법 솜씨 있는 화공이 그린 듯, 찾는 이의 뚜렷한 용모가 그려져 있었다.

“이 정도면 되겠느냐?”

칭겐이 망설임 없이 고개를 끄덕였다.

“물론입니다. 용모파기까지 있으니 금방 수소문해 볼 수 있을 겁니다.”

사방으로 전령을 띄우고 전서응을 날리면 길어도 보름 안에는 파악할 수 있다.

초원이 광활하다 하나 유목민의 눈을 피할 수는 없는 법.

‘게다가 이방인에 관한 소식은 모두 내 귀에 들어온다.’

그러나 자신만만하던 칭겐은 이어지는 노인의 말에 멈칫할 수밖에 없었다.

“절정 고수다. 검과 장법을 주로 쓰는.”

“……절정 고수라 하셨습니까?”

“왜, 더 쉽지 않느냐? 어디서든 눈에 띌 놈이니 금방 알아볼 수 있을 것이다.”

칭겐은 어렵게 입을 뗐다.

“저, 송구하지만 그 정도의 고수라면 진작 저희 형제들이 알아차렸을 겁니다.”

“흐음. 너희 생각은 어떠하냐?”

“소인도 제법 넓은 영역을 관리하고 있습니다만, 그런 고수가 나타났다는 말은 들어 본 적도 없습니다.”

“칭겐이 어렵다면 저로서도 방법이 없습니다.”

가만히 쭈그러져 있던 흑사와 테무르에게도 비슷한 대답을 얻어 낸 노인이 미간을 좁혔다.

“망할 놈. 늙은이를 이렇게 고생시키다니.”

씁쓸함이 느껴지는 노인의 중얼거림을 들은 세 사람의 귀가 쫑긋 섰다.

대관절 무슨 사정이길래 정체불명의 절대 고수가 직접 찾아 나선단 말인가. 그것도 노환을 앓는 몸으로.

‘아들? 아니면 제자?’

태도로 봐서는 혈육이나 제자가 분명한데…….

흑사는 가슴이 뛰는 것을 느꼈다. 삶의 끝자락에 선 노인이 오락가락하는 정신을 붙잡고 누군가를 찾고 있다.

죽기 전에 반드시 만나야 하는 사람. 이렇게라도 반드시 풀어야 할 한 줄기 미련이 있다는 것이다.

‘이거 혹시?’

흑사의 머리가 팽팽 돌아갔다. 어쩌면 오늘 겪은 일생일대의 위기를 기회로 만들 수 있을 것 같았다.

그의 입술이 미세하게 벌어지며 전음(傳音)이 흘러나왔다.

- 이보게, 칭겐.

갑작스러운 전음에도 칭겐은 아무런 반응도 하지 않았다. 역시 약삭 빠른 놈이다.

- 듣고 있소, 대답하시오.

- 저 노인의 제안을 받아들이게. 어서!

- 불가. 나로서는 저 노인이 원하는 자를 찾을 수 없소. 성공한다면 그만한 호의를 받겠지만, 만약 괜한 기대감을 줬다가 실패한다면 원망만 들을 뿐이지. 난 그걸 감당할 생각이 없소. 저 노인과 더 얽히기도 싫고.

- 찾아내게.

- 뭐요?

- 찾아낸다면 저 노인의 무공을 가질 수 있네. 천하를 오시할 만한 무공을!

지금 이 순간, 흑사는 확신에 차 있었다. 제자인지 아들인지 모를 그자를 반드시 찾아내야 한다. 찾아내기만 한다면…….

‘일개 성(城)이 아니라, 천하를 훔칠 수도 있다!’

초절정 고수를 상대로 하는 협박. 흑사의 말뜻을 깨달은 칭겐의 입술이 미세하게 떨렸다.

- 미쳤소? 욕심에 눈이 멀었군!

- 아니, 충분히 가능하네. 자네는 저 늙은이가 두려운 나머지 미처 생각하지 못한 거야.

- 당치 않은 소리. 저자가 그런 협박에 넘어갈 것 같소? 그전에 우리를 찢어 죽일 거요!

- 이미 노환에 정신이 오락가락하는 늙은이일세. 우선 근방을 샅샅이 뒤져 놈을 찾아내고 시간을 끌면 돼. 늙은이가 정신이 헤까닥할 때까지 말일세.

흑사 스스로가 생각해도 완벽한 계획이었다. 정신이 온전치 못할 때의 노인은 어린아이나 다름없다.

그때를 기다렸다가 제압. 회유와 협박으로 저 강대한 무공을 모조리 훔쳐 오는 것이다.

- 뭘 고민하나. 어서 승낙해!

그때, 대답이 들려왔다.

“그래, 어서 승낙하지 않고 뭐 하나?”

흑사는 그대로 몸이 굳었다.

노인이 불그스름하게 빛나는 눈빛으로 그를 바라보고 있었다. 컴컴하고 가라앉은 두 눈동자에서 감히 대항할 수 없는 화염이 줄기줄기 쏟아졌다.

“다 했나?”

“어, 어르신.”

“그리 영특한 놈은 못 되는군. 벌써 세 번째 같은 소리를 하게 만드니.”

퍽.

동시에 노인의 일장(一掌)이 흑사의 복부를 꿰뚫었다. 극에 다다른 열양지기가 장기를 사르고 혈맥을 태웠다.

“어르신이라 부르지 말라고 했잖나.”

털썩. 숯덩이가 되어 쓰러지는 흑사의 모습에 칭겐은 눈을 감았다. 사막의 모래보다 건조한 목소리가 귓가를 파고들었다.

“달포 후에 다시 오지.”

다시 눈을 떴을 때, 노인은 그 어디에도 없었다.



* * *



노인은 끌끌 혀를 찼다.

“달라진 게 없군. 도무지 달라진 것이 없어.”

오랜만에 나온 세상은 여전했다. 악한 놈, 정의로운 놈, 그리고 그 어디에도 속하지 않은 회색들이 뒤섞여 있다.

누가 죽고 살건 간에 빈자리는 반드시 채워진다. 저 마적들도 마찬가지다. 다만 운이 나빴을 뿐.

“그나저나 북부 고원이라…….”

참 멀리도 왔구먼. 중얼거린 노인은 주위를 둘러봤다.

세상의 끝에 닿는 지평선, 푸른 초원과 메마른 땅이 공존하는 이곳에서 그의 발걸음이 향할 곳은 정해져 있었다.

‘이 근방은 저 유목민 놈한테 맡기고, 나는 산서성을 뒤져 봐야겠지.’

노인은 걷기 시작했다. 그의 한걸음에 풍경이 휙휙 스쳐 지나가고 풀들이 허리를 굽혔다.

느긋한 발걸음이었지만 쏘아진 화살처럼 빠르다. 화살이 향하는 곳은 대동(大同). 산서와 고원의 경계선이었다.
```

## Final English reading copy

```markdown
# Chapter 163

“What? The Northern Gaoyuan? There are only three days left until New Year’s Day?”

“Yes.”

“Well, now.”

The old man fell silent. In front of him, the three leaders and more than two hundred underlings knelt respectfully, watching his lips.

“Is that really true?”

“W-We’re certain.”

“How could we possibly dare lie in your presence?”

“…I see.”

The old man’s expression darkened at their desperate excuses.

He knew what they were saying was true. He had only wanted to deny it, if only a little—the fact that he was growing old.

*So I was out of it for seven days and nights. Seven days and nights… It’s getting longer.*

It was because of his old age.

He had first sensed something strange more than twenty years ago. During cultivation, he had realized that his essence, qi, and spirit were falling out of alignment. That was when he knew the years had finally caught up with him.

He was already nearing a hundred. He was not afraid of death, but he did not want to be remembered as a senile old man.

*Even after all that effort…*

He had reached his limit. The curse of time could not be held back even by his two jiazi of internal energy, or by the manifested qi of a Supreme Peak master.

He had managed to delay the effects of old age for no less than twenty years. That alone should be enough to satisfy him. The old man forcibly shook off his bitterness.

“Pour me a drink.”

“Um, the wine has gone cold, so we’re preparing a fresh batch.”

At Black Sand’s cautious reply, the old man clicked his tongue.

“When will that be? Never mind. Bring me the cold wine.”

“Yes.”

Who would dare object to an order from him? At Black Sand’s gesture, two mounted bandits who looked strong enough hauled over a wine jar, groaning with effort.

The enormous jar, tall enough to reach a person’s chest, sloshed with half-cooled mare’s-milk wine.

“Tsk, tsk. Young men these days are so weak. Don’t you feed the people under you?”

“H-How could we not?”

“Then why can’t you even lift this properly? Good grief. Watching you is making me frustrated.”

The old man shot to his feet and snatched the jar away. The jar, which weighed at least several hundred catties, rose effortlessly in one hand.

It was almost impossible to understand how such strength could come from a body that had been reduced to little more than bones. Black Sand wanted to gouge out his own eyes.

*I must be crazy. I thought a monster like that was nothing more than a senile old man.*

At least he had been careful with his words. Hadn’t the Human Butcher died horribly after waving his sword around and calling the man an old geezer?

Black Sand had no desire to die with blood pouring from his seven orifices.

“Elder! I’ll do it!”

“Don’t call me elder. Sit down and stop talking nonsense.”

“No, no. Mare’s-milk wine is best when it’s piping hot. I’ll heat it myself…”

“Piping hot, what?”

Black Sand was at a loss for words.

The next moment, tremendous heat burst from the wine jar.

The source of that heat was the old man’s hand gripping the jar.

White flames, enough to make the mere sight of them suffocating and raise goose bumps, instantly heated the wine jar and warmed the mare’s-milk wine.

“T-That’s…”

“S-Samadhi True Fire?”

Temur, Chinggen, and the more than two hundred underlings were stunned by the sight before them.

The shock suffered by the leaders was especially immense.

*What the hell?*

*He’s using Samadhi True Fire on a wine jar that size?*

*That’s an unbelievable amount of internal energy. Who is this old man?*

Samadhi True Fire was a flame created by burning internal energy. A Peak master with deep internal energy could use it without much difficulty.

However, its firepower was pitiful compared to the enormous amount of internal energy it consumed, making it hopelessly inefficient in actual combat.

“Bring me a bowl. A big one.”

But what about this old man?

The heat they had felt, though momentary, had been tremendous. If he wished, he seemed capable not only of harming people but of melting steel.

*His martial arts and internal energy have already reached a transcendent realm.*

*It’s not only the Samadhi True Fire. His internal energy itself is overwhelmingly Scorching Yang Qi.*

*Don’t say anything. If I put one foot wrong, he’ll kill me.*

The three men swallowed dryly and moved as quickly as waiters receiving an honored guest.

“I’ll pour you a drink, sir.”

“Bring meat! Meat!”

“Just bring the legs!”

Black Sand, the Squad Leader of the Black Sand Band—known across the steppe as a harbinger of death—poured the mare’s-milk wine. The two tribal chieftains, descendants of the Great Khan and commanders of hundreds of mounted warriors, circled the table, tearing off only the tender leg meat and presenting it to the old man.

It was a sight difficult to witness even if one paid for it.

“Mm. This is why rude bastards need to be beaten. They only learn manners after someone teaches them a lesson.”

“You’re absolutely right, elder.”

The old man, who had been eating carefully stripped meat with his mare’s-milk wine, paused.

“Elder?”

“Y-Yes. Did I make some kind of mistake?”

“You’re making me sound old. Like some old man who’s about to die any moment.”

*Yes. You really do look like you’re about to drop dead.*

Black Sand barely managed to swallow the words that nearly escaped him. His opponent was a peerless master whose realm was impossible to gauge. He had to placate the old man somehow.

“Then, big brother…”

“Do I look like a pushover?”

“I-I’m sorry!”

*Bam!*

Black Sand slammed his forehead into the floor without a word. He felt like he was dying. The old man hated being called an elder because it made him sound old, but calling him big brother apparently made him look easy to deal with. What was Black Sand supposed to do?

The old man lightly kicked Black Sand while he was still prostrated.

“Get up.”

“Yes, sir!”

“And you two with the scraped foreheads.”

*Whoosh!*

Temur and Chinggen, who had been diligently stripping meat from the bones, rushed over at the speed of light and knelt.

Only after draining a long gulp of mare’s-milk wine did the old man finally speak.

“So, what kind of people are you?”

Mounted bandits. And nomads who were no different from mounted bandits.

They had no idea what would happen if they told the truth to an old man who clearly looked like a senior of the orthodox faction.

Just as the three men were desperately exchanging glances—

*Smack! Smack! Smack!*

“Ghk!”

“Gasp!”

“Argh!”

The old man struck each of them on the head with a knuckle at a speed too fast to see, then glared.

“You goddamn bastards. An adult asks you a question, and all you do is roll your eyes at each other?”

“I-I’m sorry, elder.”

“I told you not to call me elder. Are you holding some kind of ritual to pray for my death? Huh?”

*Smack!*

Black Sand answered and got hit again for his trouble. He felt tears welling up. He was over fifty, and all his subordinates were watching him…

“Let the oldest one answer first.”

Black Sand opened his mouth while gazing at the old man with moist eyes.

“I, that is, I roam the steppe with my close brothers and horses for company…”

“You’re a worthless mounted bandit. You spend every chance you get looting, murdering, and setting fires.”

“…”

The old man stared at Black Sand with utter contempt before turning away. Temur and Chinggen flinched and lowered their heads.

“You two call yourselves nomads, but you’re no different. Am I wrong?”

“N-No, sir.”

“You speak the absolute truth.”

“The one way you’re better than mounted bandits is that, even though you loot and kill, you aren’t arsonists who set fire to everything in sight. People who burn down other people’s homes deserve to be beaten to death!”

“…”

“…”

“…”

Wasn’t murder normally considered the gravest crime?

The three men tilted their heads at the strange feeling, only to be struck by another storm of blows.

*Smack, smack, smack!*

“Anyway, I have a general idea what sort of places you crawled out of. What I want to know is how much influence you have around here.”

“Ow… What do you mean by influence?”

“Exactly what I said. Do you have any clout?”

The three men rubbed their crowns and answered carefully.

“If we join forces, there aren’t many who could stand against us.”

“Most of us are divided into branch clans, so we are scattered rather widely. But if all our relatives gathered, we could easily fill dozens of tribes and still have people left over.”

“We exchange all the news that occurs throughout the steppe without missing anything.”

The old man’s eyes flashed at Chinggen’s final answer.

“Oh? That’s useful.”

Quick to read the situation, Chinggen realized the old man wanted information and immediately answered.

“If you need information, we’ll tell you anything you wish to know.”

“I’m looking for someone. I don’t know exactly where he is, but… he probably isn’t too far away. Can you do it?”

“Yes. If you could tell us his appearance or any distinguishing features, it would be even easier.”

“Wait here.”

The old man pulled a crumpled sheet of xuan paper from his robes. A skilled artist seemed to have drawn it; the face of the person being sought was clearly depicted.

“Will this do?”

Chinggen nodded without hesitation.

“Of course. With a portrait sketch as well, we should be able to start asking around immediately.”

If they sent messengers in all directions and dispatched messenger eagles, they could learn the answer within fifteen days at the longest.

The steppe was vast, but no one could escape the eyes of the nomads.

*Besides, all news about outsiders reaches my ears.*

But Chinggen’s confidence faltered at the old man’s next words.

“He’s a Peak master. He mainly uses a sword and palm techniques.”

“…Did you say he’s a Peak master?”

“Why? Wouldn’t that make it easier? He’ll stand out wherever he goes, so you should be able to find him quickly.”

Chinggen struggled to speak.

“I-I’m sorry, but if he’s a master of that level, my brothers would have noticed him long ago.”

“Hm. What do you think?”

“I control a fairly wide area myself, but I’ve never heard that a master like that has appeared.”

“If Chinggen can’t do it, I have no way either.”

The old man asked the same question of Black Sand and Temur, who had been sitting quietly with their shoulders hunched, and received similar answers. His brow furrowed.

“Damn that bastard. Making an old man go through all this trouble.”

The three men’s ears perked up at the bitterness in his mutter.

What kind of circumstances could have driven an unidentified Supreme Peak master to search for someone personally? And in a body suffering from old age, no less.

*His son? Or his Disciple?*

Judging by his attitude, it had to be a blood relative or a Disciple…

Black Sand felt his heart pounding. An old man standing at the end of his life was searching for someone while struggling to hold on to a mind that came and went.

Someone he had to meet before he died. He must have had at least one lingering regret that he absolutely had to resolve, even if he had to do it this way.

*Could this be…?*

Black Sand’s thoughts raced. Perhaps he could turn the life-or-death crisis he had faced today into an opportunity.

His lips parted slightly, and Sound Transmission slipped out.

— Chinggen.

Despite the sudden Sound Transmission, Chinggen showed no reaction. As expected, he was a shrewd one.

— Are you listening? Answer me.

— Accept the old man’s offer. Quickly!

— Impossible. I can’t find the person he wants. If we succeed, we may receive a great favor, but if we raise his hopes for nothing and fail, all we’ll gain is his resentment. I have no intention of dealing with that. Nor do I want to become more entangled with that old man.

— Find him.

— What?

— If you find him, you can obtain the old man’s martial arts. Martial arts powerful enough to look down on the entire world!

At that moment, Black Sand was filled with certainty. Whether the person was a Disciple or a son, they had to find him. If they succeeded…

*We could steal not just a single city, but the entire world!*

Black Sand’s plan was an attempt to blackmail a Supreme Peak master. Chinggen’s lips trembled as he grasped what Black Sand meant.

— Are you insane? Greed has blinded you!

— No, it’s entirely possible. You’re too afraid of that old man to think it through.

— Don’t be ridiculous. Do you think he’ll fall for a threat like that? He’ll tear us apart before that happens!

— He’s already an old man whose mind comes and goes because of his age. First, we search the surrounding area thoroughly and find the bastard, then we drag things out. Until the old man’s mind completely goes.

Even Black Sand thought it was a perfect plan. When the old man’s mind was not clear, he was no different from a child.

They would wait for that moment, then subdue him. Through persuasion and threats, they would steal every bit of that powerful martial arts knowledge.

— What are you hesitating over? Accept already!

That was when a reply came.

“Yes, go on and accept. What are you waiting for?”

Black Sand froze.

The old man was staring at him with reddish, glowing eyes. Flames no one could possibly resist streamed from his dark, sunken pupils.

“Are you finished?”

“E-Elder.”

“You’re not particularly bright, are you? You’ve already made me say the same thing three times.”

*Thud.*

At the same time, the old man’s palm pierced Black Sand’s abdomen. Scorching Yang Qi at its utmost burned his organs and seared his blood vessels.

“Didn’t I tell you not to call me elder?”

*Thump.*

Black Sand collapsed as a charred lump. Chinggen closed his eyes. A voice drier than desert sand drilled into his ears.

“I’ll be back in about a month.”

When Chinggen opened his eyes again, the old man was nowhere to be seen.

* * *

The old man clicked his tongue.

“Nothing has changed. Absolutely nothing has changed.”

The world he had returned to after so long was still the same. Evil people, righteous people, and grays who belonged to neither were all mixed together.

No matter who lived or died, the empty place was always filled. The same went for those mounted bandits. They had simply been unlucky.

“Speaking of which, the Northern Gaoyuan…”

He had come a long way. The old man muttered to himself and looked around.

The horizon stretched to the ends of the world. Here, where blue grassland and parched earth existed side by side, the old man already knew where his steps would take him.

*I’ll leave this area to that nomad bastard and search Shanxi Province myself.*

The old man began to walk. With every step, the landscape flashed past and the grasses bowed low.

His stride was leisurely, yet he moved as quickly as a loosed arrow. The arrow’s destination was Datong, on the border between Shanxi and the Gaoyuan.
```
