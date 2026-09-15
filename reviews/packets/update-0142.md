<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0142.txt",
      "sha256": "f6a59d014f3c35f03a0298fd75a811cbce74c4abe2dd71e1fd5d7d8764b2e8d6",
      "bytes": 13726
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f6e1983922754dd18cb954f3e60bd3d758d058818fd02488c9b70cae9d8ea6aa",
      "bytes": 2443
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ad7a3b5333e72ddc67592e3e3a13c4bc6aaaa485af0dfd9b80bdb8f00ce9104",
      "bytes": 30240
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "823df73502430907f51a56a0c3961ef4771dcc38bc2eb46d6b29744b070c201d",
      "bytes": 876
    },
    {
      "path": "characters/Gong Ilhyuk.md",
      "sha256": "e54457260cfe295d0326acdb3ed6aecb3dc1ef1861d602c844acc5b9ee283aa7",
      "bytes": 614
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "aa9633b0db06c395e87caa2f452433e42c78c653381557ee80c42fac7b2a735d",
      "bytes": 682
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "35f7e74444253ea7c06c8c48d3d841bab02aa28dc8c93cfc4ead61b39fb7bfba",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "30e2cd52bec35befeccc1d2d8db3e049b0d13a04fe664bf744adfb51a362301d",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "2e39819c9e202b9d7e61d00872b798375dde30a4bf5e1cb9a97dc8617498768e",
      "bytes": 791
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "697ccebccfb09e1ad4a73a0427e3241e4d170bfaad030d79ec04f5810b56773f",
      "bytes": 468
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "7503b4c108a51e33c1f24bc436812d6d505528a1fb90c6f89ecfe7aab765bb7a",
      "bytes": 630
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61fdb7bfe676c8db5737008d12c92989d55fa82e2c934c435836aea8671f44f5",
      "bytes": 25179
    }
  ],
  "estimated_tokens": 24703
}
-->

# Durable State Update — Chapter 142

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 142. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 142. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 142,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 142,
    "continuity_sources": [142],
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
    "The Jin Family group is attending the City Lord's luncheon at the Shanxi Provincial Office.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and is now recognized by Li Feng as his Martial Uncle.",
    "Cheongpung defeated Gong Ilhyuk with one counter using the Taeeul Miri Palm; Gong Ilhyuk remains hostile and refuses to accept the implications of Cheongpung's identity.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and was still there at least ten years before the current luncheon.",
    "Li Feng saw ten-year-old Cheongpung at Mae Jonghak's hidden residence and witnessed him perform the Plum Blossom Sword Technique.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung's exact parentage or the truth behind his claim that a crane delivered him to Mae Jonghak remains unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown."
  ],
  "continuity_sources": [
    140,
    141
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What was Taekyung about to say after recognizing the Zhongnan Sect from the novel?"
  ],
  "safe_through": 141,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when Cheongpung uses it literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Could Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검법     | **sword technique**                              |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 141
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung was living with him at a hidden Huashan residence by age ten and learned Huashan martial arts; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Gong Ilhyuk.md

# Gong Ilhyuk (공일혁)

- **Safe through:** Chapter 141
- **Aliases:** None
- **Role:** The third member of the Three Hands of Zhongnan and a Zhongnan Sect martial artist from Shaanxi
- **Personality:** Sharp-tongued, mocking, and openly antagonistic toward Li Feng
- **Voice:** Casual, taunting, and deliberately provocative
- **Relationships:** Member of the Zhongnan Sect's Three Hands; Gong Iljung, the Sect Leader and Wind-and-Cloud Sword Lord, is his father's cousin; involved in a ten-year-old humiliating martial grievance with Li Feng

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 141
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province attending the City Lord's luncheon; he interrupts a tense exchange and greets Jin Taekyung as a young hero of the Jin Family of Taiyuan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 140
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 140
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 141
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; bears a humiliating martial grievance involving Gong Ilhyuk

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 141
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 138
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family who summons martial officials and young Murim prodigies to a noon luncheon.
- **Personality:** His personal temperament is not established; his authority is treated as commanding and difficult to refuse.
- **Voice:** No direct speech appears in this chapter.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies.

## Korean source

```text
＃142화



“화산파 속가제자 이풍, 청풍 사숙(師叔)께 인사 올립니다.”

자하신공과 매화검법. 마지막으로 이풍의 입에서 흘러나온 한 단어, 사숙.

이 믿기지 않는 상황에 공일혁의 얼굴이 시커멓게 물들었다.

‘그럼 정말 저놈이?’

검성의 친손자는 아니더라도 한 가지는 확실하다.

어리둥절한 얼굴로 허리만 꾸벅꾸벅 숙이는 저 얼간이가 검성 매종학의 모든 것을 물려받은 후인(後人)이라는 것.

“이, 이럴 리가 없는데. 이건 정말 말도 안 되는…….”

공일혁이 더듬거리며 현실을 부정하던 그때. 간드러진 목소리가 귓가에 닿았다.

“공 대협.”

“아, 도지휘동지.”

홍진을 발견한 공일혁의 안색이 한결 밝아졌다.

종남파는 관(官)과의 연계를 통해 여러 가지 사업을 벌이고 있었고, 홍진은 그 과정에서 알게 된 산서성의 권력자였다.

이 곤경에서 그에게 구원의 손길을 내밀 수 있는 유일한 사람이기도 하다.

“이게 어떻게 된 일인가요?”

홍진의 부드러운 목소리에 공일혁의 마음이 편안해졌다.

“제가 잠시 착각한 모양입니다.”

“착각이라니, 무슨 착각이요?”

“그저 검성의 이름을 팔고 다니는 사기꾼 정도로 생각했는데…….”

“글쎄요, 전 무공 쪽은 영 문외한이지만 사기꾼처럼 보이지는 않던데요?”

“야, 약간의 오해가 있었던 것뿐입니다.”

“오해라…….”

나지막이 읊조리던 홍진이 공일혁을 빤히 바라봤다.

“공 대협.”

“예, 도지휘동지.”

“내가 왜 공 대협을 비롯한 종남파의 분들을 이 자리에 초대했는지 알아요?”

“압니다, 잘 알지요.”

이유는 두 가지다.

첫 번째로는 산서 성주이자 황족인 상산왕과 안면을 트고 새로 벌이는 사업의 재가를 받기 위해서.

두 번째는 홍진의 정적인 이풍의 콧대를 바짝 눌러 주기 위해서다.

“그런데 공 대협도 알다시피 내가 근래 좀 바빴거든요. 그러다 보니 경황이 없어서 전하께 다른 손님이 오신다는 말씀을 못 드렸네?”

“그러시군요.”

콧소리가 빠진 목소리는 건조하기만 할 따름이었다. 공일혁이 불안한 얼굴로 물었다.

“한데 갑자기 그 말씀은 왜…….”

“오늘은 이만 가 줬으면 해요.”

“예?”

“아무래도 불청객이 있으면 전하께서 심기가 불편하시지 않겠어요?”

명백한 축객령이었다. 거기에 더해 불청객이라는 말까지.

공일혁이 항변했다.

“불청객이라니요, 도지휘동지. 그게 대체 무슨 말씀이십니까?”

“어머, 두 번 말해야 하나요? 앞서 했던 말 그대로예요. 전하께 미처 말씀드리지 못했어요.”

홍진은 본래 내관(內官)이다. 상산왕이 갓난아기였던 시절부터 옆을 지켰고 덕분에 산서성부의 실세이자 군부 이인자인 도지휘동지라는 자리까지 꿰찼다.

이처럼 어린 왕의 총애를 한 몸에 받는 그가 고작 미리 말을 못 했다는 이유로 손님을 돌려보낸다니?

“저, 저는 도지휘동지께서 무슨 말씀을 하시는 건지 이해가 잘…….”

당황한 공일혁을 향해 홍진이 싱긋 웃어 보였다.

“공 대협.”

“예.”

“그렇게 안 봤는데, 머리가 좀 나쁘네?”

“……예?”

“아니면 눈치가 없는 건가?”

갑작스러운 폭언에 사방이 고요해졌다. 공일혁을 비롯한 종남삼수의 다른 두 사람이 주먹을 부르르 떨었다.

“말씀이 과하시군요.”

“어머, 그렇게 느꼈다면 내 의도를 제대로 파악한 거예요. 일부러 좀 과하게 한 면이 없잖아 있거든.”

“도지휘동지!”

“목소리 줄여요, 여기 대전이야.”

“갑자기 이러시는 연유가 뭡니까! 설마 방금 일로 제게 실망이라도 하신 겁니까!”

“목소리 줄이라니까. 그리고 난 공 대협한테 실망한 것 없어요. 우리가 친구도 아니고, 서로에게 뭔가를 기대하고 실망할 사이는 아니잖아.”

“그런…… 우리 종남파와의 약조는 잊으신 겁니까?”

“약조? 아, 산서성 쪽에 길을 터 달라는 그거?”

홍진이 피식 웃으며 말을 이었다.

“원래 거래라는 게 그런 거예요. 일이 성사되기 전에는 언제 어그러질지 모르는 거거든. 설마 아직 전하의 재가도 안 떨어진 일을 말 몇 마디로 다 끝났다고 생각한 건 아니죠?”

공일혁은 끓어오르는 분노를 간신히 억눌렀다.

사문인 종남파에는 일이 끝난 것처럼 호언장담해 둔 상태.

이번 일이 성공하면 그에 상응하는 보상을 받겠지만 실패한다면 질책을 피할 수 없다. 그로서는 최대한 눈앞의 내관 놈을 구슬려야만 했다.

“이번 일이 잘만 성사된다면 도지휘동지께도 좋은 일이 아닙니까. 종남파는 결코 은원(恩怨)을 잊지 않습니다.”

은혜면 은혜지, 굳이 원한까지 덧붙인 것은 은근한 협박이었다. 구파일방 중 하나를 적으로 돌릴 수도 있다는 경고.

어린 시절부터 내관으로 지내며 온갖 암투를 지켜본 홍진이 그 말에 서린 속뜻을 못 알아들을 리 없다.

‘쯧쯧. 이래서 무림인들이란.’

홍진은 내심 혀를 찼다.

언행 하나하나가 서투르고 노골적이다.

그에겐 공일혁처럼 어중간하게 닳은 인물보다는 아예 무인답게 과묵하고 뚝심 있는 이풍이 훨씬 까다로운 적수였다.

‘지금 누가 칼자루를 쥐고 있는지도 모르고.’

원하는 목표가 있다면 설설 기어도 모자랄 텐데 협박까지 곁들이다니. 그러나 덕분에 그는 마음을 굳혔다.

“공 대협. 나처럼 여린 사람은 그런 말 들으면 무서워서 같이 일 못 해요.”

“아, 혹시 오해의 소지가 있었다면…….”

공일혁이 몰랐던 척 사과하려던 그때, 지루한 표정으로 두 사람을 지켜보던 진태경이 한마디를 툭 던졌다.

“오해의 소지는 무슨. 지나가던 개도 안 믿겠네.”

“이, 이……!”

“거, 종남파 선배님들. 뭐 얼마나 대단한 사업을 하시는지는 모르겠는데 나중에 따로 얘기하시면 안 됩니까? 안 그래도 밥상 엎어진 것도 서러워 죽겠는데.”

바닥을 뒹구는 음식들을 보며 입맛을 다시는 진태경의 모습에 홍진이 실소를 터트렸다.

“걱정 말아요. 이분들이 나가시면 새로 음식을 들이라 할 테니까. 그렇죠?”

이제는 나가라고 등까지 떠미는 상황. 공일혁이 이를 악물었다.

“도지휘동지. 제 안목이 형편없다는 건 인정합니다. 다만, 부디 오늘 일로 뭘 잃고 얻을지를 잘 생각하십시오.”

“뭘 착각하시는 모양인데, 철저하게 실익을 따져서 내린 결정인걸요?”

“그게 무슨……?”

“일은 계속 진행할 겁니다. 섬서와 산서를 연결하는 전용 무역로와 무역소도 지을 거고 규모도 늘릴 거예요.”

“그럼 더욱더 본문과 손을 잡아야 하지 않겠습니까!”

처절하게까지 느껴지는 외침에 홍진이 눈을 동그랗게 떴다.

“섬서에 있는 문파가 종남파밖에 없나요? 제가 알기로는 종남파보다 훨씬 오래되고 세간의 인식도 좋은 곳이 있다던데.”

“……지금 혹시 화산파를 말씀하시는 겁니까?”

공일혁의 얼굴이 와락 일그러졌다.

화산과 종남은 지난 수백 년간 수없이 신경전을 벌여 온 숙적 관계.

이번 일이 다른 문파도 아니고 화산에게 넘어간다면 가벼운 질책 정도로 끝날 리가 없었다.

“제게 어떻게 이러실 수 있습니까!”

“당연히 이럴 수 있죠. 더 좋은 선택지가 눈앞에 있는데.”

“본문도 결코 화산파에 밀리지 않습니다. 아니, 당대에 이르러서는 오히려 화산파를 넘어섰다고 자부할 수 있습니다.”

“자부할 수 있다라. 사문에 충성하는 모습은 보기 좋아요. 하지만 제 입장에서는 자타공인(自他共認)이라는 말이 더 듣기 좋지 않을까요?”

홍진은 막힘없이 말을 이었다.

“공 대협. 단도직입적으로 물어볼게요. 종남파에도 검성 같은 고수가 있나요?”

“……그건.”

“그럼 저기 있는 소협과 같은 걸출한 후기지수는요?”

“…….”

공일혁을 포함한 종남삼수 전원은 쉽게 입을 열지 못했다.

검성? 종남파의 문주인 풍운검군이 종종 십왕(十王)에 비견되기는 하나 딱 거기까지다.

하물며 청풍 같은 괴물은 듣도 보도 못했다. 특히 선공하고서도 일 합 만에 무릎을 꿇어야 했던 공일혁은 얼굴이 붉어졌다.

“하, 하지만 본문에 소속된 절정 고수들의 숫자는 결코 화산파에 비해 밀리지 않습니다.”

“내 듣자 하니 무림 문파의 힘은 고수가 몇 명이냐가 아니라 ‘어떤’ 고수를 품었느냐에 따라 달라진다고 하더군요.”

정곡을 찌르는 홍진의 한마디에 공일혁은 순간 말문이 막혔다.

그러나 어떻게든, 무슨 수를 쓰든 화산파에게 자리를 뺏기는 것만은 막아야 했다.

“또, 또한 지금까지 관과 협력했던 것 모두 성공적으로 마무리 지었고요. 반면에 화산파는 지금까지 이런 일을 추진해 본 경험이 없습니다. 서투르고 실수가 생길 수밖에 없죠.”

“어머, 그래요?”

싱긋 웃은 홍진이 누군가를 향해 고개를 돌렸다.

“이 첨사, 어떻게 생각해요?”

묵묵히 지켜보고 있던 이풍이 대답했다.

“맞는 말입니다. 화산은 관과 무림을 확실히 구분 짓는 편이지요.”

홍진이 눈살을 찌푸리고, 공일혁의 얼굴에 화색이 돌던 그때 이풍의 묵직한 목소리가 이어졌다.

“하지만 누군가에게나 처음이란 게 존재하지 않겠습니까?”

“이풍, 네놈이!”

홍진이 깔깔 웃었다.

“우리 이 첨사, 진짜 많이 늘었다니까.”

“누구 덕분이지요.”

불과 한 식경 전에도 같은 내용의 대화를 나눴지만 분위기는 그때와 정반대다.

두 사람은 화기애애한 분위기 속에서 대화를 이어 갔다.

“이 첨사가 다리를 놔 줬으면 하는데. 어떻게 생각해요?”

“물론입니다. 사부님께 전서구를 보내지요. 이 소식을 들으면 장문인께서도 좋아하실 겁니다.”

“아, 그리고 여기 귀한 손님이 계시다는 사실도 알려 드리고.”

홍진의 눈짓이 향하는 곳을 바라본 이풍이 슬며시 웃었다.

“그건 태사부께서 좋아하실 소식이고요.”

“시작이 좋네요.”

“제 생각도 그렇습니다.”

어느새 대화에서 완전히 배제된 공일혁은 신형을 부르르 떨었다.

이미 되돌리기에는 너무 와 버린 상황. 그는 분노와 배신감이 섞인 눈빛으로 좌중을 쓸어 봤다.

“감히, 감히 대종남파를 무시하다니.”

“저기, 아까부터 말하고 싶었는데.”

불쑥 끼어든 목소리의 주인공은 진태경이었다. 그가 피식 웃으며 말을 이었다.

“종남파를 무시한 게 아니라, 그쪽을 무시한 겁니다. 몰라서 그렇지, 나 종남파 엄청 좋아해요. 군림…… 아무튼 삼십사 권까지 꼬박꼬박 봤어.”

“그게 무슨 개소리냐! 족보도 없는 태원진가 따위가 끼어들 자리가 아니다!”

진태경이 상처받은 얼굴로 청풍의 옆구리를 찔렀다.

“청 소협. 저 아저씨가 우리 집 족보도 없대.”

“헉, 은인한테요?”

“응. 아무리 선배라지만 말이 너무 심한 거 아니야? 구파일방이라 무서워서 대답도 못 하겠고, 청 소협이 대신 말 좀 해 줘.”

“제, 제가요? 저 그런 거 잘 못하는데.”

“나 은인 아니야? 말만 은인이었어?”

“아뇨, 당연히 아니죠.”

“그럼 내가 알려 주는 대로 말해.”

뭐라 속닥거림이 끝나자 청풍이 머뭇거리며 입을 열었다.

“꺼, 꺼…….”

“청 소협, 더 크게! 당신은 할 수 있어!”

진태경의 응원에 힘을 얻은 청풍이 눈을 질끈 감고 외쳤다.

“꺼져, 이 꼰대 새끼들아!”

“……!”

“……!”

꼰대? 정확히 무슨 뜻인지는 모르겠지만 그건 중요하지 않다. 뒤에 새끼라는 단어가 붙었으니까.

“이런 쳐 죽일……!”

공일혁을 포함한 세 사람이 눈을 부릅떴다.

그들이 누구인가, 종남파의 본산 제자들이다. 사람들의 선망 어린 시선에 익숙해진 그들에겐 씻을 수 없는 치욕이었다.

하지만…….

“으득, 갑시다!”

공일혁은 울분을 참으며 돌아섰다. 이 치욕을 갚아 주기에는 상대도, 장소도 좋지 않다.

‘오늘 일은 언젠가 갚는다. 반드시!’

으스러져라 움켜쥔 주먹에서는 핏방울이 떨어졌다.

거친 발걸음으로 대전을 박차고 떠나는 그의 등 뒤로 진태경과 청풍의 목소리가 따라붙었다.

“이야, 욕 잘하네. 이것도 처음이에요?”

“네, 저 욕 처음 해 봐요!”

“처음치고는 제법 소질이 있는데. 앞으로 나한테 많이 배워요. 세상 살다 보면 쓰기 싫어도 쓸 데 많다?”

“네!”
```

## Final English reading copy

```markdown
# Chapter 142

“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

Zaha Divine Technique. Plum Blossom Sword Technique. And finally, the last word to come from Li Feng’s mouth:

*Martial Uncle.*

Gong Ilhyuk’s face darkened at this unbelievable turn of events.

*Then is that bastard really…?*

Even if Cheongpung wasn’t the Sword Saint’s biological grandson, one thing was certain.

That idiot who kept bowing at the waist with a bewildered expression had inherited everything from Mae Jonghak, the Sword Saint.

“This, this can’t be. It’s impossible. This makes no sense…”

As Gong Ilhyuk stammered and denied reality, a lilting voice reached his ears.

“Great Hero Gong.”

“Ah, Deputy Military Commissioner.”

Gong Ilhyuk’s expression brightened when he spotted Hong Jin.

The Zhongnan Sect had been pursuing various ventures through its connections with the government, and Hong Jin was one of the powerful men of Shanxi Province whom they had come to know in the process.

He was also the only person who could possibly extend a hand of salvation to Gong Ilhyuk in this predicament.

“What happened?”

Hong Jin’s gentle voice put Gong Ilhyuk at ease.

“I must have been mistaken for a moment.”

“Mistaken? About what?”

“I merely thought he was some fraud going around trading on the Sword Saint’s name…”

“Well, I’m no expert in martial arts, but he doesn’t look like a fraud to me.”

“There, there was only a slight misunderstanding.”

“A misunderstanding…”

Hong Jin murmured the word quietly, then stared directly at Gong Ilhyuk.

“Great Hero Gong.”

“Yes, Deputy Military Commissioner.”

“Do you know why I invited you and the others from the Zhongnan Sect here?”

“Yes. Of course I do.”

There were two reasons.

First, to become acquainted with Prince Shangshan, the City Lord of Shanxi and a member of the imperial family, and receive his approval for their new business venture.

Second, to put Hong Jin’s political rival, Li Feng, firmly in his place.

“But as you know, I’ve been rather busy lately. I was so distracted that I forgot to tell His Highness that some other guests would be arriving.”

“I see.”

The nasal quality had vanished from Hong Jin’s voice, leaving it completely dry. Gong Ilhyuk asked anxiously,

“But why are you suddenly bringing that up…?”

“I’d like you to leave for today.”

“What?”

“Wouldn’t the presence of uninvited guests make His Highness uncomfortable?”

It was an unmistakable order to leave. And on top of that, Hong Jin had called them uninvited guests.

Gong Ilhyuk protested.

“Uninvited guests? Deputy Military Commissioner, what exactly do you mean?”

“Oh my, do I have to say it twice? I mean exactly what I said before. I failed to mention your arrival to His Highness.”

Hong Jin was a eunuch. He had remained at Prince Shangshan’s side since the prince was an infant, and thanks to that, he had risen to the post of Deputy Military Commissioner, becoming the power behind the Shanxi Provincial Office and the second-ranking figure in the military.

The young prince favored him above all others. And yet he was sending guests away simply because he had failed to inform His Highness in advance?

“I, I’m not sure I understand what you’re saying, Deputy Military Commissioner…”

Hong Jin smiled sweetly at the flustered Gong Ilhyuk.

“Great Hero Gong.”

“Yes?”

“I didn’t think you were like this, but you’re a little slow, aren’t you?”

“…What?”

“Or are you just bad at reading the room?”

The sudden verbal abuse plunged the hall into silence.

Gong Ilhyuk and the other two members of the Three Hands of Zhongnan trembled as they clenched their fists.

“Your words are excessive.”

“Oh my, if that’s how you feel, then you’ve understood my intentions perfectly. I’ll admit I deliberately went a little too far.”

“Deputy Military Commissioner!”

“Lower your voice. This is the grand hall.”

“Why are you suddenly acting like this? Are you disappointed in me because of what just happened?”

“I said lower your voice. And I’m not disappointed in you, Great Hero Gong. We aren’t friends, after all. We’re not close enough to expect anything from each other or feel disappointed.”

“How could you say that? Have you forgotten your agreement with our Zhongnan Sect?”

“Agreement? Oh, you mean the one about opening a route into Shanxi Province?”

Hong Jin gave a quiet laugh and continued.

“That’s how business works. Until a deal is finalized, it can fall apart at any moment. Surely you didn’t think a few words meant everything was settled when His Highness hasn’t even given his approval yet?”

Gong Ilhyuk barely managed to suppress his rising anger.

He had already boasted to his sect as though the deal were complete.

If the venture succeeded, he would receive a suitable reward. But if it failed, he would be unable to escape a harsh reprimand. For now, he had no choice but to coax the eunuch standing before him.

“If this deal succeeds, wouldn’t it benefit you as well, Deputy Military Commissioner? The Zhongnan Sect never forgets gratitude or grudges.”

The mention of grudges alongside gratitude was an indirect threat.

It was a warning that Hong Jin risked making an enemy of one of the Nine Sects and One Gang.

Hong Jin had spent his childhood and youth as an inner palace official, watching every kind of political struggle. There was no way he could fail to understand the hidden meaning in Gong Ilhyuk’s words.

*Hmph. This is why martial artists are so hopeless.*

Hong Jin clicked his tongue inwardly.

Every one of Gong Ilhyuk’s words and actions was clumsy and blatant.

Compared to a half-polished man like Gong Ilhyuk, Li Feng—quiet, stubborn, and martial artist to the bone—was a far more troublesome opponent.

*He doesn’t even realize who holds the upper hand right now.*

If he had a goal he wanted to achieve, he should have been crawling on the ground to get it. And yet he had added a threat on top of everything else.

That helped Hong Jin make up his mind.

“Great Hero Gong. I’m a delicate person, you see. Hearing words like that frightens me too much to continue working together.”

“Ah, if there was any room for misunderstanding…”

Gong Ilhyuk was about to apologize as though he had no idea what Hong Jin meant when Jin Taekyung, who had been watching the two men with a bored expression, casually tossed out a remark.

“Room for misunderstanding, my ass. A dog passing by wouldn’t believe that.”

“You, you…!”

“Hey, Seniors from the Zhongnan Sect. I don’t know what kind of incredible business you’re running, but couldn’t you discuss it somewhere else later? I’m already miserable enough seeing the entire meal overturned.”

Hong Jin let out a quiet laugh at the sight of Taekyung licking his lips while looking at the food scattered across the floor.

“Don’t worry. Once these gentlemen leave, I’ll have new food brought in. Isn’t that right?”

The situation had now progressed to Hong Jin practically pushing them out the door.

Gong Ilhyuk gritted his teeth.

“Deputy Military Commissioner. I admit my judgment is terrible. But please think carefully about what you will gain and lose from what happened today.”

“You seem to be mistaken. I made this decision after thoroughly weighing the practical benefits.”

“What does that mean?”

“We’ll continue with the project. We’ll build a dedicated trade route and trading post connecting Shaanxi and Shanxi, and we’ll expand the scale as well.”

“Then all the more reason you should join hands with our sect!”

Hong Jin’s eyes widened at the desperate shout.

“Is the Zhongnan Sect the only sect in Shaanxi? As far as I know, there’s a place far older than the Zhongnan Sect—and one with a much better reputation among the public.”

“……Are you talking about Huashan?”

Gong Ilhyuk’s face twisted.

Huashan and the Zhongnan Sect had been bitter rivals, constantly at odds, for the past several hundred years.

If this project went to Huashan instead of some other sect, Gong Ilhyuk knew he would face far more than a light reprimand.

“How could you do this to me?”

“Of course I can. There’s a better option right in front of me.”

“Our sect is by no means inferior to Huashan. In fact, in the current generation, I can proudly say that we’ve surpassed Huashan.”

“‘I can proudly say.’ It’s good to see such loyalty to one’s sect. But from my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?”

Hong Jin continued without hesitation.

“Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?”

“……That is…”

“Then what about a young prodigy as outstanding as that young hero over there?”

“……”

None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer.

The Sword Saint?

The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went.

As for a monster like Cheongpung, no one had ever heard or seen anything like him.

Gong Ilhyuk, who had been the one to attack first and still ended up on his knees in a single exchange, flushed red.

“B-but the number of Peak masters belonging to our sect is by no means inferior to Huashan’s.”

“I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on what kind of masters it possesses.”

Hong Jin’s single remark struck the bull’s-eye, and Gong Ilhyuk was momentarily rendered speechless.

But no matter what it took, he had to prevent the position from being handed to Huashan.

“Also, everything we’ve done in cooperation with the government has been completed successfully. Huashan, on the other hand, has never attempted anything like this. They’re inexperienced. Mistakes are inevitable.”

“Oh my, is that so?”

Hong Jin smiled and turned toward someone.

“Assistant Commissioner Li, what do you think?”

Li Feng, who had been silently observing everything, answered.

“That is true. Huashan does tend to draw a firm line between the government and Murim.”

Hong Jin frowned, and color returned to Gong Ilhyuk’s face.

But Li Feng’s heavy voice continued.

“However, doesn’t everyone have a first time?”

“Li Feng, you bastard!”

Hong Jin burst into laughter.

“Our Assistant Commissioner Li has improved so much.”

“Thanks to you.”

The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite.

They continued their conversation in a warm and friendly atmosphere.

“I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?”

“Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.”

“Ah, and you should also tell him that we have a precious guest here.”

Li Feng followed Hong Jin’s meaningful glance and smiled faintly.

“That is news our Grandmaster will be pleased to hear.”

“It’s a good start.”

“I think so too.”

Gong Ilhyuk, who had been completely excluded from the conversation, trembled from head to toe.

The situation had gone too far to turn back now.

He swept his furious, betrayed gaze across the room.

“How dare you ignore the mighty Zhongnan Sect.”

“Hey, there’s something I’ve been meaning to say.”

The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a quiet laugh and continued.

“It’s not the Zhongnan Sect we ignored. It’s you. You might not know this, but I really like the Zhongnan Sect. *The Reign…* Anyway, I kept up with it all the way through volume thirty-four.”

“What kind of bullshit are you talking about? The Jin Family of Taiyuan is a family without even a proper pedigree! This is no place for the likes of you to butt in!”

Taekyung put on a wounded expression and poked Cheongpung in the side.

“Young Master Cheongpung. That old man says our family doesn’t even have a family tree.”

“What? He said that to my Benefactor?”

“Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself. Could you say something for me?”

“M-me? I’m not very good at things like that.”

“Am I not your Benefactor? Was I only a Benefactor in name?”

“No, of course not.”

“Then say what I tell you.”

After Taekyung whispered something to him, Cheongpung opened his mouth hesitantly.

“G-get, get…”

“Young Master Cheongpung, louder! You can do it!”

Encouraged by Taekyung, Cheongpung squeezed his eyes shut and shouted,

“Get lost, you boomer bastards!”

“……!”

“……!”

*Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*.

“You goddamn bastards…!”

All three men, Gong Ilhyuk included, glared with their eyes wide open.

Who were they?

They were main disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was an insult they could never wash away.

But…

Gong Ilhyuk ground his teeth. “Let’s go!”

Gong Ilhyuk turned away, swallowing his outrage.

This was neither the right place nor the right opponent for him to repay this humiliation.

*I’ll make them pay for this someday. I swear it!*

Blood dripped from the fist he clenched so tightly that his knuckles creaked.

He stormed out of the grand hall, his footsteps heavy and violent.

Behind him came the voices of Jin Taekyung and Cheongpung.

“Wow, you’re good at swearing. Was that your first time too?”

“Yes! It was my first time ever!”

“For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.”

“Yes!”
```
